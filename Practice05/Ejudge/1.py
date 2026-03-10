import re

s = input()

if re.match(r"Hello", s) :
    print("Yes")
else:
    print("No")