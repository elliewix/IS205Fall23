# print(1,2,3,4)
# print(print)

formatted = "hello".upper()
# print(formatted)


# we can reuse it inside another function
def repeat_hello():
    print_hello()
    print_hello()
    print("I am a human")
    print_hello()
def print_hello():
    print("Hello there,")
    print("friends")
    # print(11/0)
# we can reuse it multiple times
# print_hello()
# print_hello()
# print("I am a human")
# print_hello()

# repeat_hello()

def print_twice(phrase):
    print(phrase)
    print(phrase)
    print(phrase.upper())

print_twice("hello")
# print_twice(10) # will fail on .upper()

def yell(greeting, name):
    print(greeting + " " + name)
    print("Did you hear me????")
    print(greeting.upper() + " " + name.upper())

# yell("hello there", "declan")

def yell_but_return_it(greeting, name):
    text = greeting + " " + name
    text = text + "\nDid you hear me???"
    text = text + "\n" + greeting.upper() + " " + name.upper()

    return text

yell("hello there", "Leo")
print(yell_but_return_it("hello there", "Leo"))