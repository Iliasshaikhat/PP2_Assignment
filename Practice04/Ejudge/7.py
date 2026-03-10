def reverse(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]


s = input()
for char in reverse(s):
    print(char, end="")