infile = open("Three-years-in-europe-1.txt", "r", encoding="utf-8")
text_str = infile.read()
lines_list = text_str.splitlines()
infile.close()

print(lines_list[:10])

outfile = open("the-results.txt","w",
               encoding="utf-8")

for one_line in lines_list:
    if one_line.startswith("The"):
        # print(one_line)
        outfile.write(one_line + "\n")

outfile.close()

