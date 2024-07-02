import os

file_name = "sm-nat.txt"

with open(file_name, "w") as file:
    file.write("Natita\n")
    file.write("31\n")
    file.write("python\n")  

with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

