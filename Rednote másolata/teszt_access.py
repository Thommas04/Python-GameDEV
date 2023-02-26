import pandas as pd
import pyodbc

# adatbázis elérési útvonalának megadása
db_file = r'saves/Tomikavilaga/database.accdb'

# csatlakozás az adatbázishoz
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ db_file)

# adatok betöltése pandas dataframe-be
df = pd.read_sql("SELECT * FROM tablename", conn)

# megjeleníti az első 5 sor adatot
print(df.head())

# lezárja a kapcsolatot az adatbázissal
conn.close()