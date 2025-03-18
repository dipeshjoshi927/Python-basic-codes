# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if condition}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
#-------------------------------------------------------------------------------

#cities_in_F = {'New york': 32,'Boston': 75,'Los Angeles': 100,'Chicago': 50}
#cities_in_C = {key: round((value-32)*(100/180)) for (key,value) in cities_in_F.items()}
#print(cities_in_C)
#-------------------------------------------------------------------------------------------

weather = {'New york': "snowing",'Boston': "sunny",'Los Angeles': "sunny",'Chicago': "cloudy"}
sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)
#-------------------------------------------------------------------------------------------
cities = {'New york': 32,'Boston': 75,'Los Angeles': 100,'Chicago': 50}
desc_cities ={key: ("warm" if value >= 40 else "cold") for (key,value) in cities.items()}
print(desc_cities)
#-------------------------------------------------------------------------------------------
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69>= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {'New york': 32,'Boston': 75,'Los Angeles': 100,'Chicago': 50}
desc_cities ={key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)