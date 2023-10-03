word = "snake"
other_word = "horse"
# indexing

print(word[4]) # gives "e"
print(word[-1]) # also "e"

# java kids do this
# good if you need the index
for i in range(len(word)):
    print(word[i], other_word[i])

# the more general way,
# the normal python way

for c in word:
    print(c)

##

word = "snake"
print(word[1:4]) # nak
print(word[:3]) # omit start, starts at beginning
print(word[3:]) # omit stop goes to the end

print("nothing", word[3:0]) # gives ""
