bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(2, 'ducati')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)

first_owned = motorcycles.pop(0)
print(first_owned)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
print(len(cars))
print(cars[len(cars) - 1])
print(sorted(cars))
