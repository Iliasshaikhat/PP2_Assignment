items = input().split()
k = int(input())

def limited_cycle(lst, times):
    for _ in range(times):
        for item in lst:
            yield item

for element in limited_cycle(items, k):
    print(element, end=" ")