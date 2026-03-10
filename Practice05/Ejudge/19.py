import re

s = input()

pattern = re.compile(r'\b\w+\b')

words = pattern.findall(s)

print(len(words))