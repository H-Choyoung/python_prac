import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from pandas_db_dataframe import query_MariaDB

# SQL query
query = """
    SELECT T1.market, T1.code, T1.name, T2.open, T2.close, T2.volume, T2.day
    FROM companylist T1
    INNER JOIN kospi_005930_d T2
    WHERE T1.name = '삼성전자'AND T2.day BETWEEN '2022-01-02' AND '2022-01-28' 
    ORDER BY T2.day;
"""
print(query_MariaDB(query))  # 250, int64

# print(query_MariaDB(query)['open']) #250, int64
# print(query_MariaDB(query)['day']) #250, obj

plt.plot(query_MariaDB(query)['day'], query_MariaDB(query)['open'])

plt.show()
