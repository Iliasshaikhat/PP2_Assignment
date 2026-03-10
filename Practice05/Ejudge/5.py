import re

s = input()

if re.search(r'^[A-Za-z].*[0-9]$', s):
    print("Yes")
else:
    print("No")

