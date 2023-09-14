
# has_203 = True
# has_205 = True
# should give Yes!
has_203 = False
has_205 = True
# # should give missing one

# if (has_203 == True) and (has_205 == True):
# nested option

if has_203 and has_205:
    print("You can do the thing")
elif has_203 or has_205:
    # print("missing one")
    if has_205:
        print("missing 203")
    else:
        print("missing 205")
else:
    print("no")



# just more compound booleans
#
# if has_203 and has_205:
#     print("You can do the thing")
# elif (has_203 == True) and (has_205 == False):
#     print("missing 205")
# elif (has_205 == True) and (has_203 == False):
#     print("missing 203")
# else:
#     print("no")

# we can reduce this a bit


# if has_203 and has_205:
#     print("You can do the thing")
# elif has_203 == True:
#     print("missing 205")
# elif has_205 == True:
#     print("missing 203")
# else:
#     print("no")

# and a little more

if has_203 and has_205:
    print("You can do the thing")
elif has_203:
    print("missing 205")
elif has_205:
    print("missing 203")
else:
    print("no")


# extremely defensive


if has_203 and has_205:
    print("You can do the thing")
elif has_203:
    print("missing 205")
elif has_205:
    print("missing 203")
elif has_205 == False and has_203 == False:
    print("no")
else:
    print("this should never print")