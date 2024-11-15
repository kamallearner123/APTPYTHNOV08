import re

contents = "../README.md"

# 1. Read the file and print
fd = open(contents)
data = fd.readlines()
fd.close()
print(data)

#2. Parse only the tiles
titles = []
for line in data:
    parsed = re.findall(r"###\s(\d{1,2}\.)\s\*\*(.*)\*\*", line)
    if len(parsed) is not 0:
        titles.append("".join(parsed[0]))
print(titles)


