#use SQLite database as an example

#use SQLAlchemy package - works with most SQL
from sqlalchemy import create_engine

#fire up a SQL engine that will communicate queries
engine = create_engine('sqlite:///Northwind.sqlite')

#get table names
table_names = engine.table_names()
print(table_names)

