# companylist name칼럼 이름으로 코드가 일치하는 테이블을 찾는 함수
def testFunc(market, code, period, name):
    findCodeInTable = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = SCHEMA() AND TABLE_NAME LIKE '%" + \
        code + "%'"
    sql = [
        """
        SELECT T1.code, T1.name, T1.market, T2.open, T2.close, T2.volume, T2.day
        FROM companylist T1
        INNER JOIN 
        """
        + market, code, period + " T2 " +
        "WHERE T1.name = '" + name +
        "' AND T2.day BETWEEN '2022-01-28' AND '2022-01-28' ORDER BY T2.day;"
    ]
    # print(findCodeInTable)

    result = "_".join(sql)
    return result


# print(testFunc('kospi', '005930', 'd', '삼성전자'))
