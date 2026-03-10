import re

s = input()

uppercase = re.findall(r'[A-Z]', s)
print(len(uppercase))