import re

f = open("sustained012012.txt")
content = str(f.read())

content = re.split("\n(?=Log)", content)
# print content

# mycontent = map(lambda each:each.strip("\n"), content)

allcontent = []

allcontent = [el.replace("\n", " ") for el in content]


o = open("out.txt", "w")
print >>o, allcontent


