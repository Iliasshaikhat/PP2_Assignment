n = int(input())
words = input().split()

longest = max(words, key = len)
print(longest)