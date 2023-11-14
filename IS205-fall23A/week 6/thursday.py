import string

print(string.punctuation)

phrase = "___hello. (There don't"
for punc in string.punctuation:
    phrase = phrase.replace(punc, "")

print(word)

phrase = "hello here     is some text"

words = phrase.split()
print(words)





### hw2 starting point...

def clean_punc(source_string):
    # do stuff to it
    new_string = "I'll fix this: " + source_string  #clearly this needs to change
    return new_string

t1 = "***START OF THE PROJECT GUTENBERG EBOOK THREE YEARS IN EUROPE***"
t2 = "E-text prepared by Suzanne Shell, Michael Punch, and the Project Gutenberg"
t3 = "MEMOIR OF WILLIAM WELLS BROWN,                           _Page_ ix-xxix"

print(clean_punc(t1))
print(clean_punc(t2))
print(clean_punc(t3))



### in keyword

phrase = "hello here     is some text"

words = phrase.split()
print(words)

# in with a string, it'll look for substring

print("hell" in "hello")

# in with a list looks for EXACT match in the members
phrase = "hello here     is some text"

words = phrase.split()
print("hell" in words)