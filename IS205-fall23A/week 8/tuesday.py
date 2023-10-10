# creating our infile
infile = open("Three-years-in-europe.txt", "r",
              encoding = 'utf-8')
# in the middle, read the contents
# .read() gives back a str of all the file contents
# text = infile.read()
text_str = infile.read()
# the content is now in text
# close the connection to the infile
infile.close()
print(text_str)

# lines from a string

lines_list = text_str.splitlines()

print(lines_list)

# looping over lines

# for line_str in lines_list:
#     print("hello from line 22:",  line_str)
#
# for c in text_str:
#     print("hello form 27:", c)

for word_str in text_str.split():
    print(word_str)
