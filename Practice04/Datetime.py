from datetime import datetime, timedelta

# Exercise 1
current_date = datetime.now()
new_date = current_date - timedelta(days = 5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Minus 5 days:", new_date.strftime("%Y-%m-%d"))


# Exercise 2
today = datetime.now()
tomorrow = datetime.now() + timedelta(days = 1)
yesterday = datetime.now() - timedelta(days = 1)

print("Yesterday" , yesterday.strftime("%A, %d %B %Y"))
print("Today" , today.strftime("%A, %d %B %Y"))
print("Tomorrow" , tomorrow.strftime("%A, %d %B %Y"))


# Exercise 3
now = datetime.now()

print("Without microseconds: ", now.strftime("%Y-%m-%w  %H-%M-%S"))


# Exercise 4

today = datetime.now()
tomorrow = datetime.now() + timedelta(days = 1)
difference = tomorrow - today

print("Date 1:", today.strftime("%Y-%m-%d %H:%M:%S"))
print("Date 2:", tomorrow.strftime("%Y-%m-%d %H:%M:%S"))
print("Differnce: ", difference.total_seconds())