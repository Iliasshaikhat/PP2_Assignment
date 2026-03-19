n = int(input())
keys = input().split()
values = input().split()
query = input()

d = dict(zip(keys, values))
print(d.get(query, "Not found"))