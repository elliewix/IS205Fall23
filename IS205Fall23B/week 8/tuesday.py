infile = open("Three-years-in-europe-1.txt", "r",
              encoding = "utf-8")
text_str = infile.read()
infile.close()

lines_list = text_str.splitlines()

# loop over the text

for c_str in text_str:
    print(c_str)

# for line_str in lines_list:
#     print('hello from 14', line_str)*