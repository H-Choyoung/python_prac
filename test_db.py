import pymysql

# *mariaDB connect
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='fullstack305', port=3306, db='aitrading_db', charset='utf8')

try:
    # *connection으로부터 cursor클래스 생성
    # cursor는 fetch동작을 관리하는데 사용된다.
    # cursor메소드를 사용해서 객체를 받는다.
    # curs = conn.cursor()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    # cursor 생성시 DictCursor옵션을 주면 row 결과를 dictionary 형태로 리턴한다.

    # *sql문으로 리턴값 담기
    # ? 특정 범위 데이터 구하기
    # sql = "select * from kosdak_000250_d WHERE day >='2020-01-02' AND day <= '2022-01-28'"

    # ? 특정 범위 내의 평균값 구하기
    # sql = "select AVG(open) from kosdak_000250_d WHERE day BETWEEN '2020-01-02' AND '2022-01-28'"
    # sql = "select AVG(open) from kosdak_000250_d WHERE day >='2020-01-02' AND day <= '2022-01-28'"
    # sql = "SELECT * FROM (SELECT avg(open) FROM kosdak_000250_d WHERE day BETWEEN '2020-01-02' AND '2022-01-28') AS subtest"
    # sql = "SELECT * FROM (SELECT * FROM kosdak_000250_d WHERE day BETWEEN '2020-01-02' AND '2022-01-28') AS new_table WHERE open='34500'"

    # ? group by
    # sql = "SELECT open, AVG(open) FROM kosdak_000250_d GROUP BY open"

    # ? 테이블에서 특정컬럼이 평균컬럼보다 높은 것을 선택하는 쿼리문
    # sql = "select * from kosdak_000250_d WHERE open > (select AVG(open) from kosdak_000250_d)"

    # ? 여러 테이블에서 검색한 결과 합치기
    sql = """
    SELECT AVG(open), 
    
    (SELECT AVG(open) 
    FROM kosdak_000440_d 
    WHERE day BETWEEN '2020-01-02' AND '2022-01-28')
    AS new_000440, 
    
    (SELECT AVG(open) 
    FROM kosdak_001000_d 
    WHERE day BETWEEN '2020-01-02' AND '2022-01-28')
    AS new_001000 
    
    FROM kosdak_000250_d 
    AS new_000250 
    WHERE day BETWEEN '2020-01-02' AND '2022-01-28'
    """

    curs.execute(sql)
    # excute : sql문장을 db서버에 보냄(실행)
    # curs객체에는 sql문의 리턴값들이 들어있다.

    # *객체에서 데이터 가져오기 : fetch
    # fetchone() : 첫째 row데이터를 가져온다.(실행할 때마다 순차적으로)
    # fetchall() : 전체 / 데이터를 하나만 가져올 때 fetchall을 사용하면 '리스트 타입'으로 가져오게 됨
    # fetchmany(size) : 조회된 결과로부터 입력받은 size만큼의 데이터를 '리스트 형태'로 반환
    rows = curs.fetchall()

    # *전체 row 출력
    for i in rows:
        # if i == 'new_000250':
        print(i)

finally:
    # *연결 닫기
    conn.close()
