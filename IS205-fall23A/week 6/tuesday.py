count = 0 # base
# print(count)
# count = count + 1
# count = count + 1
# count = count + 1
# count = count + 1
runs = 7
for turn in range(runs):
    count = count + 1
# print(count)
#
# data = ["Yes", "no", "yes", "yes", "no", "yes", "cat", "No"]
#
# yes_count = 0
# for answer in data:
#     # print(answer)
#     if answer == "yes":
#         # print(answer)
#         yes_count = yes_count + 1
#         # yes_count += 1 # optional shorthand
#
# print(yes_count)



data = ["Yes", "no", "yes", "yes", "no", "yes", "cat", "No", "stuff"]

yes_count = 0
others = 0
for answer in data:
    # print(answer)
    if answer.lower() == "yes":
        # print(answer)
        yes_count = yes_count + 1
        # yes_count += 1 # optional shorthand
    else:
        others = others + 1
        print(answer)

print(yes_count, others)