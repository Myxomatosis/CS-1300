#	Author: Luciano Mejia
#	Date: 9/4/14
#	Assignment #2 Part 1
#	Calculates the population of the U.S. in  one year.

# Variables
cur_pop = 318892103
sec_in_year = 31536000 # ((60*60)*24)*365

num_of_births = 31536000/8 # 3,942,000 births/year
num_of_deaths = 31536000/13 # About 2425846 deaths/year
num_of_immigrants = 31536000/40 # 788,400 immigrants/year

# Calculating the projected population
projected_pop = (cur_pop + num_of_births + num_of_immigrants) - num_of_deaths

print ("The population will be %.f" % projected_pop)