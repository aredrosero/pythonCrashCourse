prompt = "Please introduce your toppings "
prompt += "\nEnter 'exit' to end the program "


active= True
while active:
    message  = input(prompt)
    if message == 'exit':
        active = False
    else :
        print(message)