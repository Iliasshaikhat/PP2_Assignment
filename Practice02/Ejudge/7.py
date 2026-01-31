n = int(input())
arr = list(map(int, input().split()))
max = arr[0]
index = 0
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        index = i
print(index + 1)