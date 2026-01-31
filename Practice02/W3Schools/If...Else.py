#Python If...Else

a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

is_logged_in = True
if is_logged_in:
  print("Welcome back!")
  
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
  
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd") 
  
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")
  
a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
