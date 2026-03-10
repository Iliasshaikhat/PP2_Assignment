import math
def power(n):
    for i in range(n + 1):
        yield pow(2, i)
        
n = int(input())
for num in power(n):
    print(num, end =" ")