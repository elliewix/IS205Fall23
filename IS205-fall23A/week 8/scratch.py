from itertools import groupby

alice = [0, 1,0,0,0,1,1,0,1,1,0,1]

count = 0
for val, grouper in groupby(alice, 1):
    # if val == 1:
    #     count +=1
    # print(val, list(grouper))

# print(alice.count(1))
# print(count)