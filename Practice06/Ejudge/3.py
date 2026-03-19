n = int(input())
words = input().split()

for i, word in enumerate(words):
    print(f"{i}:{word}", end = " ")