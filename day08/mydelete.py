import psycopg2, pprint

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor()

col01 = '3'

sql =f"""
    DELETE FROM sample 
    where 
        col01 ='{col01}';
"""

cursor.execute(sql)
connection.commit()
print("cnt",cursor.rowcount)

cursor.close()
connection.close()