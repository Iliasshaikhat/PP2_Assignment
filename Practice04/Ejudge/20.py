import sys

g = 0
n = 0

commands = int(input())

for _ in range(commands):
    scope, value = input().split()
    value = int(value)

    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n += value
    elif scope == "local":
        pass

print(g, n)