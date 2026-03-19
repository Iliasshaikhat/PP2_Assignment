# Libraries
import os
import shutil

# Exersice 1

os.mkdirs("Folder1/Folder2/Folder3")

# Exersice 2

path = "Folder1"
for item in os.listdir(path):
    print(item)

# Exersice 3

files = os.listdir(".")

for file in files:
    if file.endswith(".txt"):
        print(file)

# Exersice 4
shutil.copy("file.txt", "Folder1/file.txt")
shutil.move("file.txt", "Folder1/file.txt")
