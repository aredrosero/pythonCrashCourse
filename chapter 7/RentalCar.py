car= input("please let me know what car are you looking for leasing? : ")
RentCar= ['subaro','ford','BMW','seat']


if car in RentCar:
    print("Yes, we have this car to rent!")
elif car not in RentCar:
    print("Sorry at this moment we have not any of this brand, sorry")


car = input("What kind of car would you like? ")

print(f"Let me see if I can find you a {car.title()}.")

party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)

if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

    number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
    