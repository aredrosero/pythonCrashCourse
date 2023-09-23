motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
#Appending Elements to the End of a List
motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)
#Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2,'ducati')
print(motorcycles)
#Removing an Item Using the del Statement

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
##Removing an Item Using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle =motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned= motorcycles.pop(0)
print(f"The first motocycle I have owned was a {first_owned.title()}.")

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive= 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")