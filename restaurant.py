class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  
  def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return total_price

brunch_items ={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
   }

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early_bird', early_bird_items, 1500, 1800)

dinner_items ={
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

kids_items = {
'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu('Kids', kids_items, 900, 2100)

print(brunch_menu)

brunch_order = ['pancakes', 'home fries', 'coffee']
print(brunch_menu.calculate_bill(brunch_order)) 
early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
print(early_bird_menu.calculate_bill(early_bird_order))
#Franchise
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"New Basta Fazoolin's located at: {self.address}, with all our tasty menus available! "
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus 


flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu] )

new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu] )
print(flagship_store)

# Call the available_menus() method with 12 noon (12:00 pm) as the argument
time_noon = 1200
available_menus_at_noon = flagship_store.available_menus(time_noon)

# Print out the results
for menu in available_menus_at_noon:
    print(menu)

# Businesses
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Create businesses
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Arepas Menu
arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50,
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Take a\' Arepa', arepas_items, '10am', '8pm')

# Arepas Franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Take a' Arepa Business
take_a_arepa = Business("Take a' Arepa", [arepas_place])