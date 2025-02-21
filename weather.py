city_temperature = [("rosebank", 26), ("randburg", 30), ("sandton", 18), ("pretoria", 26)]

def display_cities():
   print("--Cities and their temperature")
   for city, weather in city_temperature:
      print(f"{city}: {weather}°C")
#display_cities()
print()

def search_city(city):
   #searching for a city and it's temperature
   for city_name, temp in city_temperature:
      if city.capitalize() == city_name.capitalize():
         print(f"{city}'s temperature is {temp}°C")
   
#search_city("Rosebank")

while True:
   print("""What would you like to do?
         1. Print all the cities
         2. Search for a city
         3. any character to quit""")
   user_choice = input("Select choice from 1 - 3: ")

   if user_choice == "1":
      display_cities()

   elif user_choice == "2":
      user_search = input("Type a city: ")
      search_city(user_search)
      

   else:
      print("Exiting, Bye!")
      break