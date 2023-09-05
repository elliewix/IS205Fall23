# chapter 2 review

word = "cat"
num_string = "4"
othernum = '5'

print(num_string + othernum)
print(type(num_string + othernum))

# print("the num_string var is", num_string,
#       "data typet is", type(num_string))



# chapter 3

#3.1 booleans

True
False

print(6 > 5)
print(6 < 5)
print(6 == 5)

print("4" == num_string) # true

print(num_string == othernum)

print("6" > "5")
print(ord("6"))
print("A" > "a")
print(ord("A"), ord("a"))
# print(ord("cat")) #error
print("6" + "cat")

print(chr(97))
print(chr(666))

## conditional execution 3.3

# has_205 = True
has_205 = False

# if has_205 == True:
#     print("You can take 305")

# 3.4 alternative execution: if/else

# has_205 = True
has_205 = False

if has_205:
    print("Yes you can take 305")
    print(stuff) #doest't exist
    print(10/0) #div by 0 error
else:
    print("No, you can't")


if True:
    print("yup true")

if False:
    print("you'll never see this")
else:
    print("but this will")