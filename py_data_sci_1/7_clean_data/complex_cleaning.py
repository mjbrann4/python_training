import pandas as pd
import numpy as np
import re
from numpy import NaN

#df = pd.read_csv('data/test_usage_data.csv')
#df['kwh'] = pd.to_numeric(df['kwh'], errors='coerce')
#print(df.dtypes)

test_dict = {
    'treat_a': [18,12,24],
    'treat_b': [42, 31, 27]
}
df = pd.DataFrame(test_dict)

#means of each column 
print(df.apply(np.mean, axis=0))
#means of each row
print(df.apply(np.mean, axis=1))


#example of writing a function to clean data
def diff_money(row, pattern):
    icost = row['Initial Cost']
    tef = row['Total Est. Fee']

    if bool(pattern.match(icost)) and bool(pattern.match(tef)):
        icost = icost.replace("$", "")
        tef = tef.replace("$", "")

        icost = float(icost)
        tef = float(tef)

        return icost-tef
    else:
        return(NaN)

df_subset['diff'] = df_subset.apply(diff_money, axis=1, pattern=pattern)

# Write the lambda function using replace
tips['total_dollar_replace'] = tips['total_dollar'].apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips['total_dollar'].apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())


