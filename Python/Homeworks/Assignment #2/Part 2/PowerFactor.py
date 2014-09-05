# Luciano Mejia
# 9/4/14
# Assignment #2 Part 2
# Takes the user's response for real and reactive power, in order to calculate the actual power factor
import math

#User inputs a value for the real and reactive power
real_power = int(input("Enter the real power: ")) 
react_power = int(input("Enter the reactive power: "))

# The real power is divided by the square root of the sum of the squares of the Real Power (kW) and the Reactive power (kVAr)
power_factor = (real_power / (math.sqrt(pow(real_power,2) + (pow(react_power,2)))))*100

print ("The power factor is:  ", round(power_factor,2), "%")