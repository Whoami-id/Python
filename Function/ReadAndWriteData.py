file = open("Read.txt", "r")

for line in file:
    print(line.strip())

file2 = open("Write.txt", "w")
file2.write("asdfdf")
file2.close()

with open("Read.txt", "r") as f:
    for line in f:
        print(line.strip())
