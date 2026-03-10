import re

s = input()
pattern = input()

matches = re.findall(re.escape(pattern), s)

print(len(matches))