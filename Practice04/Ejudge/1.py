def squares(n):
    for i in range(1, n + 1):
        yield i * i
        
n = int(input())
for num in squares(n):
    print(num)