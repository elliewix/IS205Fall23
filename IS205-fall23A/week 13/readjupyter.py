import json

with open('Untitled.ipynb', 'r',encoding='utf-8') as infile:
    nbdata = json.load(infile)

for c in nbdata["cells"]:
    print(c)