people = []

pers = { 
    'f_name' : 'Sergio' ,
    'l_name':'Bernal',
    'age': 23,
    'city':'Sagunto' 
    }
people.append(pers)
pers1 = { 
    'f_name' : 'Dora' ,
    'l_name':'Rosero',
    'age': 51,
    'city':'Sagunto' 
    }
people.append(pers1)
pers2 = { 
    'f_name' : 'Sebas' ,
    'l_name':'Serrano',
    'age': 13,
    'city':'Sagunto' 
    }
people.append(pers2)
"""for person, details in personalDetails.items():
 #   print(f"person:{person}")
 #   print(f"details:{details}")

#print(people)
#for peopl in people:
    name = f"{persona['first_name']},{persona['last_name']}"
    age= f"{persona['age']}"
    city= f"{persona['city']}"
    this is wrong: print(f"Name:{name},\nAge:{age},\nCity:{city}")
        because i added more values at the list, correct otion show dowm line
      
    print(f"{name},{age},{city}")
    print(f"{name}, of {city}, is {age} years old.")"""



for peopl in people:
        print(f"\nHere's what I know about {pers['f_name'].title()}:")
        for key, value in pers.items():
            print(f"\t{key}: {value}")
            print(f"\nHere's what I know about {pers1['f_name'].title()}:")
        for key, value in pers1.items():
            print(f"\t{key}: {value}")
            print(f"\nHere's what I know about {pers2['f_name'].title()}:")
        for key, value in pers2.items():
            print(f"\t{key}: {value}")