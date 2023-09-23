country = 'Brazil'
#if country == 'Angola':
print(country == 'Angola')
print("\nYour county is not in the same country as mine! I predict that is false")
print(country != 'Angola')
print("\nYour county is not in the same country as mine! I predict that is TRue")

pais = "India"

print(pais =='india', 'I predict false, because Case sensitivity')
print(pais.lower()=='india','I predict true cause case sentivity')

num = 5
print(num==8,'a, predit false')
print(num>8,'b, predit false')
print(num<8,'c, predit true')
print(num>=8,'d, predit false')
print(num<=8,'e, predit true')
print(num>=8 or num<=4,'f,predit false' )
print(num>=5 and num<=6,'g,predit true' )

countries=['ireland','mexico','laos']
country="Iran"
if country not in countries:
    print(country.title()+", is not in the list")
print('iran'in countries, 'I predict false')
