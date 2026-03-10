import re 
s = input()
sub = input() 

if re.search(sub , s):
    print("Yes")
else: 
    print("No")