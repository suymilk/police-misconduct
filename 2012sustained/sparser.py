import re

f = open("sustained012012.txt")
content = str(f.read())

content = re.split("\n(?=Log)", content)
print content

