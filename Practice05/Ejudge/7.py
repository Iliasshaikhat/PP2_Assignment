import re

s = input()
pattern = input()
replacement = input()

result = re.sub(pattern, replacement, s)
print(result)