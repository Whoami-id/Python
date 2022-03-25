import os
from pathlib import Path

print(__file__)

print(os.path.dirname(__file__))
print(os.listdir("."))

folder = os.path.join(os.path.dirname(__file__), "..")
print(folder)


filename = os.path.join(os.path.dirname(__file__), "umlaute.txt")

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


print("-----------------------------------------------")



