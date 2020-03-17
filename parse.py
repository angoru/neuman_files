import json
from datetime import datetime
import os

with open('tok.json', 'r') as f:
    tok_json = json.load(f)

items = tok_json.get('item')

# create a directory to put all js files
parse_dir_name = 'parse_' + datetime.now().strftime("%s")
os.mkdir(parse_dir_name)


for item in items:
    event = item.get('event')
    if event:
        for data in event:
            script = data.get('script')
            f = open(os.path.join(parse_dir_name, item["name"] + ".js"),"w")
            for line in script['exec']:
                f.write(line + "\n")
            f.close()
