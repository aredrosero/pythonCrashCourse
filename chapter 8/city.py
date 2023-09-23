
def city_country(citi,countri):

    combine = f"{citi},{countri}"
    return combine.title()
    
    #print(f"this is your facourite city and country,{combine}")
while True:
        print("\nPlease tell me your city and country!!!")
        print("use 'none' to stop the quiz, at any moment")

        city= input("please, tell me your favourite city: ") 
        if city == 'none':
              print('Bye!')
              break
        country= input("please tell me your favourite country: ")
        if country == 'none':
              print('Bye!')
              break
        city_count= city_country(city, country)

        
        

        
        print(f"this is your facourite city and country, {city_count.title()}")

            
    

