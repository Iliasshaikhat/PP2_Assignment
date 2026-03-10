def squares(x, y):
    for i in range(x, y) :
        yield i * i
 
x, y = map(int, input().split())
for num in squares(x , y + 1):
    print(num,) 