n = int(input())
ans = True

while n > 0:
    if (n % 10) % 2 != 0:
        ans = False
        break
    n //= 10

if ans:
    print("Valid")
else:
    print("Not valid")
