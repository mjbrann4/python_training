import pandas as pd 

#sas import needs to import sas package
from sas7bdat import SAS7BDAT

with SAS7BDAT('urbanpop.sas7bdat') as file:
	df_sas = file.to_data_frame()

#can import stata with pandas
data = pd.read_stata('urbanpop.dta')


