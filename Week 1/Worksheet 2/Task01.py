furlongs_in_mile = 8
number_of_furlongs = float(input("Provide number of furlongs: "))
print(f"{number_of_furlongs:g}", 'furlong' if number_of_furlongs <= 1 else 'furlongs', '=', end=" ")
print(f"{number_of_furlongs * furlongs_in_mile:g}", 'mile' if number_of_furlongs * furlongs_in_mile <= 1 else 'miles')
