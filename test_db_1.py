import pymysql
from testfunc import testFunc

# *mariaDB connect
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='fullstack305', port=3306, db='aitrading_db', charset='utf8')

try:
    # *connection으로부터 cursor클래스 생성
    # cursor는 fetch동작을 관리하는데 사용된다.
    # cursor메소드를 사용해서 객체를 받는다.
    # curs = conn.cursor()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs2 = conn.cursor(pymysql.cursors.DictCursor)
    # cursor 생성시 DictCursor옵션을 주면 row 결과를 dictionary 형태로 리턴한다.

    # * NAME으로 종목코드 찾기
    # sql = """
    # SELECT T1.code FROM companylist T1 WHERE T1.name LIKE '삼성%'
    # """

    # * 종목명으로 테이블 join
    # sql = """
    # SELECT T1.code, T1.name, T1.market, T2.open, T2.close, T2.volume, T2.day
    # FROM companylist T1
    # INNER JOIN kospi_005930_d T2
    # WHERE T1.name = '삼성전자'
    # ORDER BY T2.volume;
    # """
    # sql = testFunc('kospi', '005930', 'd', '삼성전자')

    sql2 = testFunc('kospi', '005930', 'd', '삼성전자')
    sql = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = SCHEMA() AND TABLE_NAME LIKE '%005930%'"

    curs.execute(sql)
    curs2.execute(sql2)

    # *객체에서 데이터 가져오기 : fetch
    rows = curs.fetchall()
    rows2 = curs2.fetchall()

    # *전체 row 출력
    for j in rows2:
        tbCode = j['code']
        print(tbCode)

    for i in rows:
        tbName = i['TABLE_NAME']
        if tbCode in tbName:
            print('포함')

finally:
    # *연결 닫기
    conn.close()
