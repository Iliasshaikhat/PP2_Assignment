n = int(input())
numbers = list(map(int, input().split()))

unique_numbers = set(numbers)
sorted_numbers = sorted(unique_numbers)

print(*sorted_numbers)