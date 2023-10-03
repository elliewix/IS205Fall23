# indexing
# for when you want one and only one thing

text = "cat"
print(text[2]) # should be t
[] # this is a list
"cat"[2] # this is indexing
# print(text[3]) # this will give you an error
print(text[0]) # "the first"
print(text[-1]) # "the last"
print("cat"[-1], "banana"[-1], "snake"[-1])

# java kids do this
# only do this if you NEED the index position
word = "snake"
for i in range(len(word)):
    print(word[i])

# python standard pattern
for c in word:
    print(c)

# slicing, for when you want a collection of stuff

word = "snake"
# [start: stop] [inclusive:exclusive]
print(word[0:4]) # "snak"
print(word[2:])
# omit start to presume from the beginning
print(word[:4])
# omit stop to presume to the end
print(word[3:])
# both are optional
print(word[:])