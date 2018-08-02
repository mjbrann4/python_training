import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine('sqlite://Music.sqlite')

#can query directly from pandas
df = pd.read_sql_query("SELECT * FROM album", engine)

# Open engine in context manager
# Perform query and save results to DataFrame: df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result: does df = df1 ?
print(df.equals(df1))
