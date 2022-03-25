import re

sentence = "ich habe 30 Hunde, die jeweils 4 Liter wasser brauchen und 2 kg Nahrung"

print(re.findall("[0-9]+", sentence))
print(re.search("[0-9]+", sentence))
