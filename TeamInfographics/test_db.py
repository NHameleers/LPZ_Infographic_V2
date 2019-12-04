import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
 
 
create_connection('db.sqlite3')


df = pd.read_csv('I:/LPZ/Infographic/data/Data zorgaccent variabelen infographic_final.csv')
df.index.name = 'id'

conn = sqlite3.connect('db.sqlite3')  # pass your db url

df.to_sql(name='LPZ2019V1', con=conn)


# after this, set this database in the settings.py file
# run python manage.py inspectdb > examplemodels.py
# this makes a model script
