cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car)
    else:
        print(car.title())

cars = ['audi', 'bmw', 'subaru', 'toyota']

print('audi' in cars)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
