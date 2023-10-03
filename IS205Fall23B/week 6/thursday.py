import string
# print(string.punctuation)





words = "here's some __stuff__ *thing* )()"

for punc in string.punctuation:
    print(punc)
    words = words.replace(punc, "")
# words = words.replace(")", "")
# words = words.replace("(", "")

print(words)

# the in keyword

# alone, used as a boolean operator

# when used with strings....
# looks for substrings within
print("hell" in "hello")

# when used with a list on the right....

phrase = "hello there      humans"
words = phrase.split()
print(words)
print("hell" in words)


#####

def clean_punc(source_string):
    # do stuff.....

    # presumably you've changed source_string....
    return source_string

t1 = "***START OF THE PROJECT GUTENBERG EBOOK THREE YEARS IN EUROPE***"
t2 = "E-text prepared by Suzanne Shell, Michael Punch, and the Project Gutenberg"
t3 = "MEMOIR OF WILLIAM WELLS BROWN,                           _Page_ ix-xxix"

print(clean_punc(t1))
print(clean_punc(t2))
print(clean_punc(t3))




#######

# letter grade calculator

score = 55000

if score > 100:
    print("score too high")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 0:
    print("F")
else:
    print("error")


