n =int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = sum(x * y for x, y in zip(a, b))
print(result)