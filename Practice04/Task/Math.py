import math

#Exercise 1
deg = int(input("Input degree: "))
rad = deg * (math.pi / 180)
print(rad)

#Exercise 2
H = int(input("Height: "))
A = int(input("Base, first value: "))
B = int(input("Base, second value: "))  
Area = ((A + B) * H ) / 2
print(Area)

#Exercise 3
n =  int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area =  (n * l * l) / 4 * math.tan(math.pi / n )
print(area)

#Exercise 4
l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
print("Expected Output", l * h)