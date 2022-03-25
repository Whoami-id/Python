from collections import defaultdict

print("Hallo".upper())
print("Hallo".lower())

sentence = "Ist das Wetter heute gut?"
if sentence.endswith("?"):
    print("Der satz endet mit Fragezeichen")


word = " Hallo "
print(word.strip())
print(word.strip("o"))
print(word.find("o"))
print(word.replace("l", "L"))



def generate():
    print("generate wurde aufgerufen")
    return 0

d = defaultdict(generate)
d["existiertNicht"] = d["existiertNicht"] = 5
print(d)


d = defaultdict()

def better_string_format(name, age):
    print("Hallo my name is {} and i am {} years old".format(name, age))

better_string_format("Eirk", 22)


def f_string_format(name, age):
    print(f"Hallo my name is {name} and i am {age} years old")

f_string_format("Max", 23)