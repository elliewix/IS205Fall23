# if....
# else...

# has_203 = True
# has_205 = True
# should give Yes!
has_203 = False
has_205 = True
# # should give missing one

# if (has_203 == True) and (has_205 == True):
# nested
if has_203 and has_205:
    print("You can do the thing")
elif has_203 or has_205:
    print("missing one")
else:
    print("no")
