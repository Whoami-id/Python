n = 42

if n < 42:
    print("Die Zahl ist kleiner als 42")
elif n == 42:
    print("Die Zahl ist gleich 42")
else:
    print("Die zahl ist kleiner als 42")




age = 45

if age >= 30 and age <= 39:
    print("Diese Person ist in ihren 30-ern")

if age < 30 or age >= 39:
    print("Diese Person ist nicht in ihren 30-ern")



nums = [12,34,44,67]

for num in nums:
    if num % 5 == 0:
        print(num)
else:
    print("not found")
