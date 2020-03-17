import json
import glob
from datetime import datetime
import  shutil

# # copy and create new file
# json_file = 'tok_' + datetime.now().strftime("%s") + '.json'
# shutil.copy('tok.json', new_file)

def get_js(item):
    with open(item['name'] + '.js', 'r') as f:
        js = f.read()
        item['event'][0]['script']['exec'] = js
    return item


json_file = 'tok.json'

# parse json
with open(json_file, 'r') as f:
    tok_json = json.load(f)

script_names = []

# get test in js files
files = glob.glob('*.js')

# create parsed json file
items = tok_json.get('item')
# print(items)


# items = [item for item in items if item['name'] in list(map(lambda x: x.split('.js')[0], files))]


items = [get_js(item) for item in items if item['name'] in list(map(lambda x: x.split('.js')[0], files))]

tok_json['item'] = items

json_out_file = 'tok_' + datetime.now().strftime("%s") + '.json'

with open(json_out_file, 'w') as outfile:
    json.dump(tok_json, outfile)
