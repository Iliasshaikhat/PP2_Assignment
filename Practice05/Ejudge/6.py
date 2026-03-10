import re

s = input()

match = re.search(r'\S+@\S+\.\S+', s)
if match:
    print(match.group())
else:
    print("No email")