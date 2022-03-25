counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1

for i in range(0, 10):
    print(i * i)


for i in range(0, 10):
    if i == 3:
        continue
    print(i)


for i in range(0, 10):
    if i == 3:
        break
    print(i)