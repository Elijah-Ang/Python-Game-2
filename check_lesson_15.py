import json

with open('/Users/elijahang/Python-Game-2/frontend/public/data/lessons.json', 'r') as f:
    data = json.load(f)

l15 = data.get('15', {})
print(json.dumps(l15, indent=2))
