#workflow of SQL querying
#1 Import packages and functions
#2 Create the database engine
#3 Connect to the engine
#4 Query the database
#5 Save query results to a DataFrame
#Close the connection

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.sqlite')
con = engine.connect()

#sends results to rs-> which we can convert to dataframe
rs = con.execute("SELECT * FROM Orders")
df = pd.DataFrame(rs.fetchall())

#set columns to their proper names
df.columns = rs.keys()

#close connection
con.close()

print(df.head())


#can also use context manager so you don't have to close columns
with engine.connect() as con:
	rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
	df = pd.DataFrame(rs.fetchmany(size=5))
	df.columns = rs.keys()

	
