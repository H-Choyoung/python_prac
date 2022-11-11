# MariaDB query connect
def query_MariaDB(query):
    import pandas as pd
    import pymysql
    from datetime import datetime

    # DB connect
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           password='fullstack305', port=3306, db='aitrading_db', charset='utf8')

    # start time
    start_tm = datetime.now()

    # Get DataFrame
    global query_result

    query_result = pd.read_sql(query, conn)

    # Close connect
    end_tm = datetime.now()

    print('start time:', str(start_tm))
    print('end time:', str(end_tm))
    conn.close()

    return query_result

# SQL query
query = """
    SELECT T1.market, T1.code, T1.name, T2.open, T2.close, T2.volume, T2.day
    FROM companylist T1
    INNER JOIN kospi_005930_d T2
    WHERE T1.name = '삼성전자'AND T2.day BETWEEN '2021-01-28' AND '2022-01-28' 
    ORDER BY T2.volume;
"""

# Excute SQl in python
query_MariaDB(query)

# print(query_MariaDB(query))
