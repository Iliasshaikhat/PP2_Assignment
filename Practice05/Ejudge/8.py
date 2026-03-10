import re

s = input()
pattern = input()

result = re.split(pattern , s)
print(",".join(result))