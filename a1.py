 # Exercise 5

def inverse(n):
    while n >= 0:
        yield n
        n -= 1
        

n = int(input("Enter number: "))
for num in inverse(n):
    print(num , end = ", ")