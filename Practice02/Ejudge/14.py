n = int(input())
a = list(map(int, input().split()))

best = a[0]
best_count = a.count(a[0])

for x in a:
    c = a.count(x)
    if c > best_count or (c == best_count and x < best):
        best = x
        best_count = c

print(best)
