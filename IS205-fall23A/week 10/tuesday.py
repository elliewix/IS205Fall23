import csv

infile = open('horse csv example.csv', 'r', encoding='utf-8')

csvin = csv.reader(infile) # done with infile

# csvin is our special object that parses the csv for you

headers = next(csvin) # parse just one item, just the first row
# print(headers)
data = [] # outer list
for row in csvin:
    data.append(row)

print(len(data))
print(data[:10])

# for row_list in data[:10]:
#     print(row_list)
#     for cell in row_list:
#         print(cell)

# writing out

# make the data first

new_data = []

for row_list in data:
    wikidata = row_list[0]
    name = row_list[1]
    wdid = wikidata.split("/")[-1]
    # print(wdid[-1])
    # print(wdid, name)
    new_row = [wdid, name]
    # print(new_row)
    new_data.append(new_row)

new_headers = ['wikidata id', 'name']

# the two things you need before you can write it out

# print(len(data), len(new_data))

## once you have the new headers
## and the new data, then write it out

outfile = open("horse ids.csv", 'w', encoding='utf-8')

csvout = csv.writer(outfile)

# write out the headers, a 1D list
csvout.writerow(new_headers) # give writerow a 1d list
# write all the data out, a 2D list
csvout.writerows(new_data) # give writerowS a 2d list
