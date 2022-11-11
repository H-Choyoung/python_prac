import pymysql

# *mariaDB connect
conn = pymysql.connect(host='127.0.0.1', user='root', password='fullstack305', port=3306, db='aitrading_db', charset='utf8')

# *connection으로부터 cursor생성
# db cursor는 fetch동작을 관리하는데 사용된다. 
# cursor메소드를 사용해서 객체를 받는다. 
curs = conn.cursor() 

# *sql 실행
sql = 'select * from companylist'
# sql = 'select name from companylist'
curs.execute(sql) #sql문장을 db서버에 보냄

# *데이터 fetch
# rows = curs.fetchall()
rows = curs.fetchone()
rows2 = curs.fetchone()

# *전체 row 출력
for i in rows:
    print(i)
for i in rows2:
    print(i)

# *연결 닫기
conn.close()