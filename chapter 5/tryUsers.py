#userNames = []

#if userNames :
   #  for username in userNames:
    #    if username == 'admin':
     #       print("Hello admin, would you like to see a status report?")
     #   else:
      #      print(f"Hello {username}, thank you for loggin in again!")
#else:
  #  print("we need some users!")


current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']
current_users_lower = [user.lower() for user in current_users]

if new_users:
    for user in new_users:
        if user.lower() == current_users_lower:
            print(f"This user {user.title()}, already exist")
        else:
            print(f"User {user.title()}, has being added")
else:
    print("There are not new users!")    

if new_users:
    for user in new_users:
        if user.lower() in current_users_lower:
            print(f"This user {user.title()}, already exist")
        else:
            print(f"User {user.title()}, has being added")
else:
    print("There are not new users!")   