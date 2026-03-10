import re

s = input()

words = re.findall(r'\b\w{3}\b', s)
print(len(words))