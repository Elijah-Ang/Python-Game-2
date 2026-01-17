const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);

const readArg = (name) => {
  const prefix = `--${name}=`;
  const direct = args.find((arg) => arg.startsWith(prefix));
  if (direct) {
    return direct.slice(prefix.length);
  }
  const index = args.indexOf(`--${name}`);
  if (index !== -1 && args[index + 1]) {
    return args[index + 1];
  }
  return null;
};

const mode = (readArg("mode") || "shots").toLowerCase();
if (mode !== "shots") {
  throw new Error(`Unsupported mode "${mode}". Only --mode=shots is available.`);
}

const inputPath = readArg("input") || path.resolve(__dirname, "../interaction_audit.json");
const idsArg = readArg("lesson-ids") || readArg("ids");
const sampleRaw = readArg("sample");
const sampleSize = sampleRaw ? Number(sampleRaw) : null;
const auditParam = readArg("audit") === "1";

const rawBaseUrl = process.env.BASE_URL || "http://127.0.0.1:5173/Python-Game-2/";
const baseUrl = rawBaseUrl.endsWith("/") ? rawBaseUrl : `${rawBaseUrl}/`;
const lessonTimeoutMs = Number(process.env.LESSON_TIMEOUT_MS || 15000);
const screenshotDir = path.resolve(__dirname, "../screenshots");

const ensureDir = (dir) => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
};

const formatDuration = (ms) => {
  if (!Number.isFinite(ms)) {
    return "0s";
  }
  const totalSeconds = Math.max(0, Math.round(ms / 1000));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  if (hours > 0) {
    return `${hours}h ${minutes}m`;
  }
  if (minutes > 0) {
    return `${minutes}m ${seconds}s`;
  }
  return `${seconds}s`;
};

const logProgress = (index, total, startTime) => {
  const elapsed = Date.now() - startTime;
  const avg = elapsed / Math.max(1, index);
  const eta = avg * Math.max(0, total - index);
  const percent = total ? Math.round((index / total) * 100) : 100;
  // eslint-disable-next-line no-console
  console.log(`Shots ${index}/${total} (${percent}%) avg ${formatDuration(avg)} ETA ${formatDuration(eta)}`);
};

const parseIds = () => {
  if (idsArg) {
    return idsArg
      .split(",")
      .map((value) => Number(value.trim()))
      .filter((value) => Number.isFinite(value));
  }
  if (!fs.existsSync(inputPath)) {
    throw new Error(`Missing audit metadata at ${inputPath}. Run the data audit first.`);
  }
  const records = JSON.parse(fs.readFileSync(inputPath, "utf-8"));
  return records
    .filter((record) => Array.isArray(record.issues) && record.issues.length > 0)
    .map((record) => record.lesson_id);
};

const applySample = (targets) => {
  if (!sampleSize || !Number.isFinite(sampleSize) || sampleSize <= 0) {
    return targets;
  }
  return targets.slice(0, sampleSize);
};

const waitForAuditReady = async (page, lessonId) => {
  await page.waitForFunction(
    (targetId) => {
      const ready = window.__AUDIT_READY__;
      return ready && ready.lessonId === targetId;
    },
    lessonId,
    { timeout: lessonTimeoutMs }
  );
};

const captureLessonShot = async (page, lessonId) => {
  const root = await page.$("[data-lesson-id]");
  if (!root) {
    return { ok: false, error: "lesson_root_missing" };
  }
  const box = await root.boundingBox();
  if (!box) {
    return { ok: false, error: "lesson_root_not_visible" };
  }
  const clip = {
    x: Math.max(0, box.x),
    y: Math.max(0, box.y),
    width: Math.max(1, box.width),
    height: Math.max(1, box.height)
  };
  const screenshotPath = path.join(screenshotDir, `lesson-${lessonId}.png`);
  await page.screenshot({ path: screenshotPath, clip });
  return { ok: true, path: screenshotPath };
};

const resolvePlaywright = () => {
  try {
    return require("playwright");
  } catch (error) {
    const fallback = path.resolve(__dirname, "../frontend");
    return require(require.resolve("playwright", { paths: [fallback] }));
  }
};

const runShots = async () => {
  const targets = applySample(parseIds());
  if (!targets.length) {
    // eslint-disable-next-line no-console
    console.log("No flagged lessons to capture.");
    return;
  }

  const { chromium } = resolvePlaywright();
  ensureDir(screenshotDir);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto(baseUrl, { waitUntil: "domcontentloaded" });

  const startTime = Date.now();
  let captured = 0;

  for (let index = 0; index < targets.length; index += 1) {
    const lessonId = targets[index];
    const auditSuffix = auditParam ? "?audit=1" : "";
    const hashRoute = `#/lesson/${lessonId}${auditSuffix}`;
    // eslint-disable-next-line no-console
    console.log(`Capturing lesson ${lessonId}...`);
    try {
      await page.evaluate((nextHash) => {
        window.location.hash = nextHash;
      }, hashRoute);
      await waitForAuditReady(page, lessonId);
      const shot = await captureLessonShot(page, lessonId);
      if (shot.ok) {
        captured += 1;
      } else {
        // eslint-disable-next-line no-console
        console.warn(`Screenshot skipped for ${lessonId}: ${shot.error}`);
      }
    } catch (error) {
      // eslint-disable-next-line no-console
      console.warn(`Screenshot failed for ${lessonId}:`, error && error.message ? error.message : String(error));
    }
    logProgress(index + 1, targets.length, startTime);
  }

  await browser.close();
  // eslint-disable-next-line no-console
  console.log(`Screenshots captured: ${captured}/${targets.length}`);
};

runShots().catch((error) => {
  // eslint-disable-next-line no-console
  console.error(error);
  process.exit(1);
});
