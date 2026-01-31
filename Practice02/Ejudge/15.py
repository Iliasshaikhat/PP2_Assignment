n = int(input())
name = set()
for i in range(n):
    surname = input().strip()
    name.add(surname)
    
print(len(name))
