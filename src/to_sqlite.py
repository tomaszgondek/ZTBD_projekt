import pandas as pd
import sqlite3
import os

csv_file = "../resources/Real_Estate_Sales_2001-2023_GL.csv"
db_file = "../resources/realestate_sqlite3.db"
table_name = "data"

if not os.path.exists(csv_file):
    raise FileNotFoundError(f"CSV file not found: {csv_file}")
df = pd.read_csv(csv_file)
conn = sqlite3.connect(db_file)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

print(f"done")
