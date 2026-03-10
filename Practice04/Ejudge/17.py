import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx * dx + dy * dy
b = 2 * (x1 * dx + y1 * dy)
c = x1 * x1 + y1 * y1 - R * R

seg_len = math.hypot(dx, dy)

if a == 0:
    if x1 * x1 + y1 * y1 <= R * R:
        print(f"{seg_len:.10f}")
    else:
        print("0.0000000000")
else:
    D = b * b - 4 * a * c
    if D < 0:
        if x1 * x1 + y1 * y1 <= R * R:
            print(f"{seg_len:.10f}")
        else:
            print("0.0000000000")
    else:
        sqrtD = math.sqrt(D)
        t1 = (-b - sqrtD) / (2 * a)
        t2 = (-b + sqrtD) / (2 * a)
        l = max(0.0, min(1.0, t2) - max(0.0, t1))
        print(f"{l * seg_len:.10f}")