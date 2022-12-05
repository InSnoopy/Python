import psycopg2, pprint

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor()
cursor.execute("SELECT col01,col02,col03 from sample") 
data=cursor.fetchall() 

print(data)

cursor.close()
connection.close()

# cursor.execute("CREATE TABLE points (id SERIAL PRIMARY KEY, name VARCHAR(255), location GEOMETRY)")
# connection.commit()

# psycopg2.connect
# 데이터베이스명, 사용자ID, PW를 입력하여 DB에 연결
# connection.cursor
# 데이터베이스와 통신할 수 있는 cursor 생성
# cursor.execute
# 인자로 입력된 SQL문을 실행
# connection.commit
# 변경 내용을 DB에 저장
