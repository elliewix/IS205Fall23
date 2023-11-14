import json

infile = open('human.json', 'r', encoding='utf-8')
# note how I DIDNT use .read()
data = json.load(infile)
infile.close()
print(type(data))
# print(data)

# here's how we can drill in

# for something in data:
#     print(type(something), something)

print(type(data))

for key, value in data.items():
    print(key, type(value))

# let's get the home phone
# get into the key
print(data["phone_numbers"])
# which one has home?
for phones in data["phone_numbers"]:
    # print(phones)
    if "type" in phones.keys():
        type = phones["type"]
        # print(type)
        if type == "home":
            print(phones)
# print(data["phone_numbers"])

data["children"].append("Leo")

# print(data)

# now that we've updated it we can write it out

outfile = open("updatedhuman.json", "w", encoding='utf-8')
json.dump(data, outfile, indent = 4)
outfile.close()