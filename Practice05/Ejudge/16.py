import re

s = input()

pattern = r"Name:\s*(.+),\s*Age:\s*(.+)"

match = re.search(pattern, s)

if match:
    print(match.group(1), match.group(2))