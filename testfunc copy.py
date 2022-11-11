import pymysql

# *mariaDB connect
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='fullstack305', port=3306, db='aitrading_db', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

# companylist name칼럼 이름으로 코드가 일치하는 테이블을 찾는 함수

tb2 = "SELECT code FROM companylist WHERE name LIKE '" + name + "%'"
print(tb2)


def testFunc2(name):
    # tb1 = "SELECT T1.market, T1.code, T1.name FROM companylist T1"
    tb2 = "SELECT code FROM companylist WHERE name LIKE '" + name + "%'"


print(testFunc2('삼성'))

#     curs.execute(tb2)


# rows = curs.fetchall()
# for i in rows:
#     print(testFunc2('삼성'))
