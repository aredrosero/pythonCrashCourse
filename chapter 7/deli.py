'''
sandwich = ['tuna','ham & cheese','hawaian']
finished_sandwich =[]


 
while sandwich:
    making= sandwich.pop()

    print(f"Making your {making.title()} sandwich")
    finished_sandwich.append(making)

print(f"\nIn a moment your sandwich would be ready!!!!!")
for finish in finished_sandwich:
   print(f"\nYou  {finish.title()} sandwich has being made and served")
'''
sandwich = ['tuna','ham & cheese','hawaian','pastrami']

finished_sandwich =[]
print(sandwich)
print( 'Hi, Sorry we sold out of Pastrami')

while 'pastrami' in sandwich:
        sandwich.remove('pastrami')
print(sandwich) 


while sandwich:
    making= sandwich.pop()
    
    print(f"In your {making.title()} sandwich")
    
    finished_sandwich.append(making)

print(f"\nIn a moment your sandwich would be ready!!!!!")
for finish in finished_sandwich:
   print(f"\nYou  {finish.title()} sandwich has being made and served")