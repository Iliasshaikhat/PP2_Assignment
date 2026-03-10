n = int(input())

def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

for i, num in enumerate(fibonacci(n)):
    if i != 0:
        print(",", end="")
    print(num, end="")