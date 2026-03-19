# Libraries

from  functools import reduce

# Exercise 1

nums = int(input())

squares = list(map(lambda x : x**2, nums))
print(squares)
sorted = list(filter(lambda x : x % 2 == 0, squares))
print(sorted)

# Exercise 2

nums = int(input())

total = reduce(lambda x, y : x + y, nums)
print(total)
# Exercise 3

names = ["Doner", "Pizza", "Chubar Lagman"]

for i, name in enumerate(names):
    print(i, name)


names = ["Doner", "Pizza", "Chubar Lagman"]
scores = [990, 1490, 2590]

for name, score in zip(names, scores):
    print(name, score)
    
    
# Exercise 4

x = 5

print(type(x))  
print(isinstance(x, int))

a = "10"

num = int(a)   
print(num + 5) 

b = 5
text = str(b)
print(text + " apples")
