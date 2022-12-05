import psycopg2, pprint

col01 = '3'
col02 = '8'
col03 = '8'

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor()

# f를 앞에 붙이면 {}안에 넣을 수 있다.
#.format(col02, col03, col01)는 {}안에 빈 공간에 있어야한다.
sql =f"""
    UPDATE sample 
    set 
        col02 = '{col02}', 
        col03 = '{col03}' 
    where 
        col01 = '{col01}'
"""


cursor.execute(sql)
connection.commit()
print("cnt",cursor.rowcount)
cursor.close()
connection.close()