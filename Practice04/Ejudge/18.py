import sys

x1, y1 = map(float, sys.stdin.readline().split())
x2, y2 = map(float, sys.stdin.readline().split())

t = y1 / (y1 + y2)

x = x1 + t * (x2 - x1)
y = 0.0

print(f"{x:.10f} {y:.10f}")