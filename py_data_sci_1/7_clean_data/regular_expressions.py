import pandas as pd 
import numpy as np
import re

#REGEX PATTERNS
# 17      - \d*
# $17     - \$\d*
# $17.00  - \$\d*\.\d*
# $17.89  - \$\d*\.\d{2}
# $17.895 - ^\$\d*\.\d{2}$


test_dict = {'values': ['17', '$17', '$17.00', '$17.89', '$17.895']}
df = pd.DataFrame(test_dict)

#best way to use regex is compile the pattern and then use it over and over again
pattern = re.compile('\$\d*\.\d{2}')
result = pattern.match('$17.89')
print(bool(result))

#match on dataframe
df['test'] = df['values'].apply(lambda x: bool(pattern.match(x)))
print(df)


# Compile the pattern
prog = re.compile('\d{3}-\d{3}-\d{4}')
result = prog.match('123-456-7890')
print(bool(result))
result = prog.match('1123-456-7890')
print(bool(result))

# Extracting values with re.findall
pattern = re.compile('\d+')
matches = re.findall(pattern, 'the recipe calls for 10 strawberries and 1 banana')
print(matches)


#more regular expressions
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern1,pattern2,pattern3)
