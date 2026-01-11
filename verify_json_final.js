const fs = require('fs');
const files = [
    'frontend/public/data/lessons.json',
    'frontend/public/data/courses.json'
];

files.forEach(f => {
    try {
        const data = fs.readFileSync(f, 'utf8');
        JSON.parse(data);
        console.log(`PASS: ${f}`);
    } catch (e) {
        console.error(`FAIL: ${f}`);
        console.error(e.message);
        process.exit(1);
    }
});
