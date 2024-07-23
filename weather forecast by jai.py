def weather_forecast(temparature,location):
    location=="hyderabad" or "hyd"
    if location=="hyderabad" or "hyd":
     return location
    temparature=="monday:(28°/26°C)"
    if temparature=="monday(28°/26°C)":
     return temparature
    else:
     return "none"

location=input("Enter your location:")
temparature=input("Enter day: ")
weather=weather_forecast(temparature,location)
print(f"The temparature of your location is {weather}")

'''def weather_forecast(day, location):
    # Weather data dictionary
    weather_data = {
        "hyderabad": {
            "monday": "28°/26°C",
            "tuesday": "30°/27°C",
            "wednesday": "29°/26°C",
            "thursday": "31°/28°C",
            "friday": "32°/29°C",
            "saturday": "33°/30°C",
            "sunday": "34°/31°C"
        }
    }
    
    # Normalize inputs
    location = location.lower().strip()
    day = day.lower().strip()
    
    # Check if the location is in the weather data
    if location in weather_data:
        # Check if the day is in the location's weather data
        if day in weather_data[location]:
            return f"The temperature on {day.capitalize()} in {location.capitalize()} is {weather_data[location][day]}"
        else:
            return f"No temperature data available for {day.capitalize()} in {location.capitalize()}"
    else:
        return "Location not supported"

location = input("Enter your location: ")
day = input("Enter day: ")
weather = weather_forecast(day, location)
print(weather)
'''
