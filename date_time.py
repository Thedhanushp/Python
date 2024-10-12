import datetime
now = datetime.datetime.now()

print(datetime.datetime.now())
print(datetime.date.today())

print(now.strftime("%d:%m:%y"))

x = datetime.datetime(year = 2024,month = 4,day = 12)
y = datetime.datetime(year = 2023,month = 5,day = 23)
dif = x - y

end = datetime.datetime.now()
diffence = end - now
print(diffence)
print(dif)