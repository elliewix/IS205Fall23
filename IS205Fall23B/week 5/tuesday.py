
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    "stuff"
    print("hello there")
    print("friends")
    print('one more')

# print("starting program")
# print_lyrics()
# print_lyrics()

# repeat_lyrics()

# parameters

def greeting(name):
    print(name)
    print("Elizabeth")

# greeting("Elizabeth")
# greeting("Humans")

## multiple parameters

def yell(greeting, name):
    print(greeting + " " + name)
    print("did you hear me?????")
    print(greeting.upper() + " " + name.upper())

# yell("hello there", "human child")

def yell_but_return(greeting, name):
    text = greeting.upper() + " " + name.upper()

    return text

result = yell_but_return("hello again", "human child")
print(result)

def stuff():
    print("hello from line 44")

result2 = stuff()
print(result2) # doesn't work