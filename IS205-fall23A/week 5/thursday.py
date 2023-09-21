# write a function called cleanup_string
# input should be phrase, as the var name

# should strip white space off
# and lowercase
# return the processed string
# example: " here IS text    "
# should become "here is text"

def cleanup_string(input_string):
    # do stuff
    lower = input_string.lower()
    clean = lower.strip()
    return clean

cleaned_text = cleanup_string("  here IS Some Text    ")
print(cleaned_text)





