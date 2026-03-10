import re

s = input()

if re.fullmatch(r'\d+', s):
    print("Match")
else:
    print("No match")