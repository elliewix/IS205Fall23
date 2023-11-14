import json

infile = open("human.json", 'r', encoding='utf-8')
# note that I didn't use .read() or anything
data = json.load(infile)
infile.close()

print(type(data))
print(data)

print(data["first_name"])
print(data["address"])
print(type(data["address"]))
print(data["address"]["postal_code"])

data["children"].append("Baby Smith")

print(data)

outfile = open("updatedhuman.json", "w", encoding='utf-8')
json.dump(data, outfile, indent = 4)
outfile.close()