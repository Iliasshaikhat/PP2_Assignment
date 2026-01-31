n =int(input())
arr = list(map(int, input().split()))
max = arr[0]
min = arr[0]

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]

for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
        

for i in range(len(arr)):
    if arr[i] == max:
        arr[i] = min

print(*arr)