

ticket = True

while ticket:
    prompt = input("please tell me your age: ")
    age = int(prompt)
    if age <=3:
        print("your kid doesnt pay anything")
        break
    elif age <=12:
        print("You must pay £10")
        break
    elif age >=12:
        print( "you must pay £15")
        break

    else:
        ticket = False