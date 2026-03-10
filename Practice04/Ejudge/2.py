n = int(input())
def even(n):
    for i in range(0, n + 1, 2):
        yield i

for ev in even(n):
    if ev != 0:
        print(",", end = "")
    print(ev, end="")