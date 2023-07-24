number = range(0, 10)

for num in number:
    print(num, end="")

meals = ['pasta']
print("")
for item in ['meals', 'hi']:
    print(item.upper())

days = ["mon", "tue", "wed"]

for i in days:
    i.capitalize()
    print("nice day: ", i)

members = ["john smith", "sen plakay", "dora ngacely"]


for names in members:
    first_name, last_name = names.split(" ")
    print(first_name.capitalize(), last_name.capitalize())
