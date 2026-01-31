n = int(input())
arr = [input().strip() for _ in range(n)]

first_index = {}


for i, s in enumerate(arr):
    if s not in first_index:
        first_index[s] = i + 1


for s in sorted(first_index):
    print(s, first_index[s])
