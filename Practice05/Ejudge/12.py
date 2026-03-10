import re 
s = input()

numbers = re.findall(r'\d{2,}', s)
print(" ".join(numbers))