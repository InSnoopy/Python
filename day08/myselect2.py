import psycopg2, pprint
import psycopg2.extras

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor(cusrsor_factory=psycopg2.extras.DictCursor)
cursor.execute("SELECT col01,col02,col03 from sample") 
data=cursor.fetchall() 

print(data)

cursor.close()
connection.close()
