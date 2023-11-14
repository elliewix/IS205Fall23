d = {} # empty dictionary

# add a key
d["a"] = 10
d["b"] = 6
print(d)
# let's see a value, and act on it
print(d["b"] * 12)

typed_in_dict = {'d': 45, 'e': 100}

print(d)
print(typed_in_dict)

# info getting methods
# useful, but not always used
print(d.keys())
print(d.values())

# looping over a dictionary
# got to have stuff in it!

# this is the way I like

# for key, value in d.items():
for letter, count in d.items():
    print(letter, count)
# items() will give you a list of tuple pairs
# with the content
print(d.items())

# programmatically populating a dictionary

word = "dinosaur friend Gus is a cool little dude"
characters = list(word) # gives a list of all the characters
print(characters)

# phase 1, just setup
# loop over the sequence of data
# for c in characters:
#     c = c.lower()
#     print(c)

# now we'll do a dictionary accumulator

char_counts = {}
for c in characters:
    c = c.lower()
    if c in char_counts: # checks if key is in dict or not
        # if true, then I've already got that character in there
        # and I just need to increment it
        char_counts[c] = char_counts[c] + 1
        # char_counts[c] += 1 # does the same thing, just shorter
    else:
        # false means that character not seen before
        char_counts[c] = 1 # establish the base counter
        # 1 because we've seen one! right now!

print(char_counts)

# prepopulate a dict

prepop_counts = {}

for c in characters:
    prepop_counts[c] = 0

# print(prepop_counts)

for c in characters:
    prepop_counts[c] = prepop_counts[c] + 1
print(prepop_counts)