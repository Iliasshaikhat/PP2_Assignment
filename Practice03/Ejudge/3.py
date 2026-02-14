s = input()

d = {
    "ZER":"0","ONE":"1","TWO":"2","THR":"3","FOU":"4",
    "FIV":"5","SIX":"6","SEV":"7","EIG":"8","NIN":"9"
}
r = {v:k for k,v in d.items()}


for i in range(len(s)):
    if s[i] in "+-*":
        op = s[i]
        a = s[:i]
        b = s[i+1:]
        break


x = ""
for i in range(0, len(a), 3):
    x += d[a[i:i+3]]

y = ""
for i in range(0, len(b), 3):
    y += d[b[i:i+3]]

x = int(x)
y = int(y)


if op == "+":
    res = x + y
elif op == "-":
    res = x - y
else:
    res = x * y

ans = ""
for c in str(res):
    ans += r[c]

print(ans)
