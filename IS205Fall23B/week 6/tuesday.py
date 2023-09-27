count = 0 # base

# count = count + 1
# count = count + 1
# count = count + 1
# count = count + 1
runs = 7
for thing in range(runs):
    count = count + 1
    # print(thing)

# print(count)

data = ["no", "yes", "yes", "no", "yes", "cat", "stuff", "Yes"]
yes_count = 0
others = 0
for answer in data:
    # print(answer)
    if answer.lower() == "yes":
        yes_count = yes_count + 1
        # print(yes_count)
    else:
        others = others + 1
    # print("hello from line 21", yes_count)
print("num yes:", yes_count, "the not yes ones", others)
