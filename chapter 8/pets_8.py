def describe_pet(animal_type, pet_name):

    """Display information about a pet."""

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')
'''The order of keyword arguments doesn’t matter because Python
knows where each value should go. The following two function calls are
equivalent:'''

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie.
describe_pet('willies')
describe_pet(pet_name='willies')
# A hamster named Harry.
describe_pet('harrys', 'hamsters')
describe_pet(pet_name='harrys', animal_type='hamsters')
describe_pet(animal_type='hamsters', pet_name='harrys')

