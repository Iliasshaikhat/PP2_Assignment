n = int(input())
numbers = [input().strip() for _ in range(n)]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1


count = 0
for num in freq:
    if freq[num] == 3:
        count += 1

print(count)
