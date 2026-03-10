import re

s = input()

words = re.findall(r'\w+', s)

print(len(words))