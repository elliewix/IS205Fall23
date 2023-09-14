# has_205 = True
# has_203 = True
# # both must be met to meet req, should say "yes"

# has_205 = False
# has_203 = True
# should be missing one

has_205 = True
has_203 = True
# still yes
# if (has_205 == True) and (has_203 == True):
if has_205 and has_203:
    print("yes you can")
elif has_205 or has_203:
    print("missing one")
else:
    print("no")