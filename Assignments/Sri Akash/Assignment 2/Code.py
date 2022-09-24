'''dht11 sensor ranges are used for temperature and humidity'''

import random
from time import sleep 

while True:
    #Temperature range is 0.00 C to 50.00 C
    temp = random.randint(0,5000)/100
    
    #Relative Humidity range is 20% to 90%
    humidity = random.randint(20,91)
    
    #Warnings for temperature is set for ranges below 10.00 C and above 40.00 C
    #Warnings for humidity is set for ranges below 30% and above 80%

    if temp > 40:
        print("High Temperature detected!!")
    elif temp < 10:
        print("Low Temperature detected!!")
    else:
        print("Stable temperature")

    print()
    
    if humidity > 80:
        print("Wet condition is detected")
    elif humidity < 30:
        print("Dry condition is detected")
    else:
        print("Stable Relative Humidity")

    print("--------------------------------")
    sleep(2)
