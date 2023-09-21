# write a function called cleaned_text
# that should take in a phrase called input_text
# and clean it up. Lowercase all the text and
# clean the  whitepace off both sides.
# return the cleaned up text

# called like cleaned_text(input_text)...
# lowercase text via "stuff".lower()
# clean whitespace off with "stuff".strip()

def cleaned_text(input_text):
    lower = input_text.lower()
    cleaned = lower.strip()
    return cleaned

# print(cleaned_text("  here's some TeXT   "))
result = cleaned_text("  here's some TeXT   ")
print(result)