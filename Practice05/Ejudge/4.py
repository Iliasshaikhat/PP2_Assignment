import re

s = input()

digits = re.findall(r"\d", s)

print(" ".join(digits))