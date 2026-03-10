import re

s = input()
sub = input()

matches = re.findall(sub, s)
print(len(matches)) 