import json
import re
import ssl
import urllib.request
from pathlib import Path

BASE = "https://www.w3schools.com"


def fetch(url: str) -> str:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return urllib.request.urlopen(url, context=ctx, timeout=20).read().decode("utf-8", "ignore")


def extract_sidebar(html: str) -> str:
    start = html.find("<div id='leftmenuinnerinner'>")
    if start == -1:
        start = html.find('<div id="leftmenuinnerinner">')
    if start == -1:
        return html
    # capture until the next sidebar footer
    end = html.find("<!-- w3", start)
    if end == -1:
        end = html.find("</div>", start)
    return html[start:end]


def extract_topics(html: str, base_path: str, key_prefix: str):
    section = extract_sidebar(html)
    # Prefer explicit tutorial links (python_*.asp / sql_*.asp)
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', section)
    items = []
    for href, text in links:
        txt = re.sub(r"<[^>]+>", "", text).strip()
        if not txt:
            continue
        if href.startswith("https://"):
            full = href
        elif href.startswith("/"):
            full = BASE + href
        else:
            full = f"{BASE}{base_path}{href}"
        if key_prefix == "python":
            if "python_" not in full and "/python/" not in full:
                continue
        if key_prefix == "sql":
            if "sql_" not in full and "/sql/" not in full:
                continue
        items.append({"title": txt, "url": full})

    # Fallback: scan full HTML for python_ or sql_ links
    if key_prefix == "python":
        pattern = r'<a[^>]+href="([^"]*python_[^"]+)"[^>]*>(.*?)</a>'
        fallback = re.findall(pattern, html)
        for href, text in fallback:
            txt = re.sub(r"<[^>]+>", "", text).strip()
            if not txt:
                continue
            if href.startswith("https://"):
                full = href
            elif href.startswith("/"):
                full = BASE + href
            else:
                full = f"{BASE}{base_path}{href}"
            items.append({"title": txt, "url": full})
    if key_prefix == "sql":
        pattern = r'<a[^>]+href="([^"]*sql_[^"]+)"[^>]*>(.*?)</a>'
        fallback = re.findall(pattern, html)
        for href, text in fallback:
            txt = re.sub(r"<[^>]+>", "", text).strip()
            if not txt:
                continue
            if href.startswith("https://"):
                full = href
            elif href.startswith("/"):
                full = BASE + href
            else:
                full = f"{BASE}{base_path}{href}"
            items.append({"title": txt, "url": full})

    # de-dupe by url then title
    seen_url = set()
    dedup = []
    for item in items:
        if item["url"] in seen_url:
            continue
        seen_url.add(item["url"])
        dedup.append(item)
    # de-dupe by title
    seen_title = set()
    final = []
    for item in dedup:
        if item["title"] in seen_title:
            continue
        seen_title.add(item["title"])
        final.append(item)
    return final


def main():
    data = {"python": [], "sql": []}

    python_html = fetch(f"{BASE}/python/default.asp")
    sql_html = fetch(f"{BASE}/sql/default.asp")

    data["python"] = extract_topics(python_html, "/python/", "python")
    data["sql"] = extract_topics(sql_html, "/sql/", "sql")

    out_path = Path(__file__).resolve().parent / "w3schools_topics.json"
    out_path.write_text(json.dumps(data, indent=2))
    print("Wrote", out_path)
    print("Python topics:", len(data["python"]))
    print("SQL topics:", len(data["sql"]))


if __name__ == "__main__":
    main()
