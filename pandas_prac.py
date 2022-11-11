from pandas import Series, DataFrame

kakao = Series([92600, 92400, 94300, 92300])
# print(kakao)

# 인덱싱 값을 지정할 수 있음
kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=[
                '2016-02-19', '2016-02-18', '2016-02-17', '2016-02-16', '2016-02-15'])
# print(kakao2)

# 인덱싱 순서가 달라도 같은 값끼리 덧셈 연산 가능
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merge = mine + friend
# print(merge)

# DataFrame
raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}
data = DataFrame(raw_data)
print(data)

