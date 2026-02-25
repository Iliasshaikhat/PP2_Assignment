# Exercise 1
def squares(n):
    for i in range(n + 1) :
        yield i * i
 
n = int(input("Enter number: "))        
for num in squares(n):
    print(num, end = " ") 
    

# Exercise 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
            
n = int(input("Enter number: "))
for num in even_numbers(n):
    print(num, end = ", ")
    
    
# Exercise 3
def divisibles(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter number: "))
for num in divisibles(n):
    print(num, end = ", ")
    

# Exercise 4
def squares(x, y):
    for i in range(x, y) :
        yield i * i
 
x, y = map(int, input("Enter number: ").split())
for num in squares(x , y):
    print(num, end = " ") 
    

# Exercise 5

def inverse(n):
    while n >= 0:
        yield n
        n -= 1
        

n = int(input("Enter number: "))
for num in inverse(n):
    print(num , end = ", ")