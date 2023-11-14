
# empty dictionary
d = {}

# add a value
d["a"] = 4
d["b"] = 6
print(d)
# look up a value, just extraction
print(d["a"]) # should print 4
# let's change that value to 10
d["a"] = 10 # see the assignment statement?
print(d)
print("line 14", d["a"]) # now I'll see 10

# operate right on it
# the literal value takes the place of the lookup
print(d["a"] + d["b"])

# looping over lists
# there are many ways, but I like this one

### first let's see some helpful methods
print(d.items())
# print(d.keys())
# print(d.values())

# presuming there's stuff in there
# for key, value in d.items()....
for c, count in d.items():
    print(c, count)

# populate a dict from within a loop
phrase = "here is a dinosaur friend his name is gus and is a cool dude"
characters = list(phrase)
print(characters)
counts = {}
# loop over the data
for c in characters:
    # print(c)
    if c in counts:
        # when true, it means we've seen it
        # and we just need to add 1
        counts[c] = counts[c] + 1
        # counts[c] += 1 # just a shorthand
        # remember count = count + 1?
    else: # when the key isn't in there yet
        counts[c] = 1 # establish the base
        # it's 1 because we're looking at one!

# prepopulate a dictionary

prepop_counts = {}
for c in characters:
    prepop_counts[c] = 0

print(prepop_counts)

for c in characters:
    prepop_counts[c] = prepop_counts[c] + 1
print(prepop_counts)

