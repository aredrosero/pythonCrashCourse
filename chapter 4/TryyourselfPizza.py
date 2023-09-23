pizzas=["Margarita","Peruana","Angolena"]
#for pizza in pizzas:
  #  print(f"I like this pizza:{pizza.title()}.\n")
#print(f"but my favourite is:"pizzas[1].title()))
#print(f"but my favourite is: {pizzas[1].title()}")

friend_pizza = pizzas[:]
pizzas.append("hawaina")
friend_pizza.append("pepperoni")
#print(pizzas)
for pizza in pizzas:
    print(f"I like this pizza:{pizza.title()}.\n")
for pizza in friend_pizza:
    print(f"My friend like this pizza:{pizza.title()}.\n")




