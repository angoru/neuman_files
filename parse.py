import json

with open('tok.json', 'r') as f:
    tok_json = json.load(f)

items = tok_json.get('item')

for item in items:
    event = item.get('event')
    if event:
        for data in event:
            script = data.get('script')
            f = open(item["name"] + ".js","w")
            for line in script['exec']:
                f.write(line + "\n")
            f.close()
