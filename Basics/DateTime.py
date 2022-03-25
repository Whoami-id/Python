from datetime import datetime, timedelta

now = datetime.now()
print(now)

day = datetime(2017,8,20,0,0)
print(day)

print(day.year)
print(day.month)
print(day.day)
print(day.hour)
print(day.minute)
print(day.second)

print(now.timestamp() - day.timestamp())


print(now.strftime("%d.%m.%Y"))

d = "18.07.2027"
print(datetime.strptime(d, "%d.%m.%Y"))


print(now + timedelta(days = 20))

