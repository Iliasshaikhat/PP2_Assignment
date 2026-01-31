n = int(input())
episodes = {}

for i in range(n):
    s, k = input().split()
    k = int(k)
    if s in episodes:
        episodes[s] += k
    else:
        episodes[s] = k


for dorama in sorted(episodes):
    print(dorama, episodes[dorama])
