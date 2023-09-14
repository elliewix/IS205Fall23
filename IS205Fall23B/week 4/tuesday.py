has_205 = False
has_203 = True

# if (has_205 == True) and (has_203 == True):


# example of nested
if has_205 and has_203:
    print("yes you can")
elif has_205 or has_203:
    # print("missing one")
    if (has_205 == True) and (has_203 == False):
        print("203 missing")
    else:
        print("205 missing")
else:
    print("no")

# just using elifs plus else

if has_205 and has_203:
    print("yes you can")
elif (has_205 == True) and (has_203 == False):
    print("missing 203")
elif (has_205 == False) and (has_203 == True):
    print("missing 205")
else:
    print("no")


# super overkill

if has_205 and has_203:
    print("yes you can")
elif (has_205 == True) and (has_203 == False):
    print("missing 203")
elif (has_205 == False) and (has_203 == True):
    print("missing 205")
elif (has_205 == False) and (has_203 == False):
    print("no")
else:
    print("this should never print")