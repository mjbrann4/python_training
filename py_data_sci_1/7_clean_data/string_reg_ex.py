import pandas as pd 
import numpy as np
import re


#use str.contains() which takes a regular expression pattern and applies it to the series
#this will return true or false

# Create the series of countries: countries
countries = gapminder.country

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
#Anchor the pattern to match exactly what you want by placing 
#a ^ in the beginning and $ in the end.
#Use A-Za-z to match the set of lower and upper case letters, 
#\. to match periods, and \s to match whitespace between words.

pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)
