import re

s = input()
if re.search(r'cat|dog', s):
    print("Yes")
else :
    print("No")