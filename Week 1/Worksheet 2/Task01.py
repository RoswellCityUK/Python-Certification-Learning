furlongsInMile = 8
numberOfFurlongs = float(input("Provide number of furlongs: "))
print(f"{numberOfFurlongs:g}", 'furlong' if numberOfFurlongs <= 1 else 'furlongs', '=', end=" ")
print(f"{numberOfFurlongs * furlongsInMile:g}", 'mile' if numberOfFurlongs * furlongsInMile <= 1 else 'miles')
