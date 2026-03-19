# Libraries
import shutil
import os

# Exersice 1

with open("file.txt", "w") as file:
    file.write("Doner Kebab")

# Exersice 2

with open("file.txt", "r") as file:
    text = file.read()
print(text)

# Exersice 3

with open("file.txt", "a") as file:
    file.write("Chubar Lagman")

# Exersice 4

shutil.copy("file.txt", "newfile.txt")

# Exersice 5

os.remove("file.txt")

