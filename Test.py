import re

text = input()
pattern = r"\b[a-zA-Z]{4}\b"

words = re.findall(pattern,text)

print(words)