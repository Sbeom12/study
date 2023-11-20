import pandas as pd
df= pd.read_csv('./raw.csv', encoding='euc-kr', sep= ',')

# 데이터 정제
df = df.dropna() # 빈 데이터 제거.
df[['기종', '용량']] = df['이름'].str.rsplit(' ', n=1, expand=True)
df = df[~df['기종'].str.contains('워치')]
df['가격'] = pd.to_numeric(df['가격'].str.replace(',', ''), errors='coerce')

df = df.drop(columns=['이름', '시간'])

# [저장불량] 칼럼에서 잘못 들어간 E급과 F급 데이터 '검수중'으로 바꾸기
df.loc[df['기능불량'].str.contains('E급'), '기능불량'] = '검수중'
df.loc[df['기능불량'].str.contains('F급'), '기능불량'] = '검수중'
df = df.drop_duplicates()
df.to_csv('data.csv',encoding='euc-kr',index=False)
