cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
# .sort() sort the list in alphabetical order.
# The sort() method, shown at u, changes the order of the list permanently. The cars are now in alphabetical order, 
# and we can never revert to the original order

cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)

#You can also sort this list in reverse alphabetical order by passing the
# argument reverse=True to the sort() method. The following example sorts
# the list of cars in reverse alphabetical order
print(cars)
#the order has been permanently changed

cars=['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
# the sorted() function. The sorted() function lets you display your list 
# in a particular order but doesn’t affect the actual order of the list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
