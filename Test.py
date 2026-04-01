with open ("names.txt", "r") as file1:
    text1 = file1.read()
    
with open ("grades.txt", "r") as file2:
    text2 = file2.read()
list2 = text2.split()
list1 = text1.split()

for n , g in zip(list1,list2 ) :
    print (f'{n}-{g}')