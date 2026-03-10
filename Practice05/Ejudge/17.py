import re

s = input()

dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', s)

print(len(dates))