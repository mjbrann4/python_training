from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.sql')

query = """SELECT OrderID, CompanyName FROM Orders INNER JOIN 
           Customers on Orders.CustomerId = Customers.CustomerId"""

df = pd.read_sql_query(query, engine)