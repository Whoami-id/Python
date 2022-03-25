try:
    print(5/0)
    print(4)
except ZeroDivisionError:
    print("Durch null teilen ist nicht erlaubt")
print(5)


try:
    file =  open("eixist", "r")
    print(file)
    print(5/0)
except FileNotFoundError:
    print("Datei wurde nicht gefunden")
finally:
    file.close()



try:
    with open("eixist.txt", "r") as f:
        print(f)
except FileNotFoundError:
    print("Datei wurde nicht gefunden")


