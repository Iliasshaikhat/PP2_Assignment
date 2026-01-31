n = int(input())
arr = list(map(int, input().split()))
num = set()

for i in arr:
    if i in num:
        print("NO")
    else:
        print("YES")
        num.add(i)