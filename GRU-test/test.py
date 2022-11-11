#모듈 불러오기 
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib as pl

# 학습 데이터 : 아마존(2013~2018 일일주가)
# 테스트 데이터 : 아마존 2019년
AMZN = yf.download('AMZN',
                  start= '2013-01-01',
                  end= '2019-12-31',
                  progress= False)

# 수정종가(Adj close), 시가(Open), 최고가(High), 최저가(Low), 종가(Close). 거래량(Volume)

allData = AMZN[['Adj Close', 'Open', 'High', 'Low', 'Close', 'Volume']].round(2)
allData.head(10)

print(str(allData[:'2018'].shape[0])+'학습데이터')
print(str(allData['2019':].shape[0])+'학습데이터')
allData['Adj Close'].plot()

def ts_train_test(all_data, time_steps, for_periods):
  """
  input-------------------------------------------
  data: 날짜를 인덱스로 가지는 주식가격(Adj Close)데이터
  output--------------------------------------------
  X_train, u_train: 2013/1/1 ~ 2018/12/31 까지의 데이터
  X_test: 2019년 데이터
  time_steps: input데이터의 time steps(과거 몇 개의 데이터를 볼 것인지 나타냄)
  for_periods: output데이터의 time stpes
  """
  
  # training & test set 만들기
  ts_train = all_data[:'2018'].iloc[:,0:1].values
  ts_test = all_data['2019':].iloc[:,0:1].values
  ts_train_len = len(ts_train)
  ts_test_len = len(ts_test)
  
  # scale the data (데이터 정규화)
  from sklearn.preprocessing import MinMaxScaler #머신러닝용 스케일러(??)
  sc = MinMaxScaler(feature_rane=(0,1))
  ts_train_scaled = sc.fit_transform(ts_train)
  
  