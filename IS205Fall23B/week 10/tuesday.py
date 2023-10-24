import csv

infile = open('horse csv example.csv', 'r', encoding='utf-8')

csvin = csv.reader(infile)
# done with infile

headers = next(csvin) # grab just the first line

data = []

for row_list in csvin: # looping over csvin NOT infile
    data.append(row_list)
# done with csvin at this point
# all the data we want is in the data list
# let's look at the first 10 rows of data

# print(data[:2])
#
# for dontknow in data[:2]:
#     print(dontknow)
    # oh it's a list!

nums = []

nums.append([10, 20, 30])
nums.append([40, 50, 60])

# print(nums)

# print(headers)
# print(data[:5])

# writing stuff out

# need two things: the new headers and the new data
# headers needs to be 1D list
# data needs to be a 2D list
# 1d list
new_headers = ['wikidata id', 'horse name thing']
# construct the 2 d list

new_data = []

for row_list in data:
    wikidata = row_list[0]
    name = row_list[1]
    # print(wikidata.split("/")[-1])
    wd_id = wikidata.split("/")[-1]
    # print(wd_id, name)
    # create my sublist
    new_row = [wd_id, name]
    new_data.append(new_row)

print(new_data[:10])

# write it out

outfile = open("wikidata names.csv", "w", encoding = 'utf-8')

csvout = csv.writer(outfile)
#write the headers first
csvout.writerow(new_headers) # writerow takes a 1 D list
csvout.writerows(new_data) # writerowS takes a 2d list