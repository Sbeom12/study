# pip install plotly 필요.

import streamlit as st
import pandas as pd
import plotly.express as px
def format_price(price):
    man = int(price // 10000)
    chun = int((price % 10000) // 1000)
    return f"{man}만{chun}천" if chun != 0 else f"{man}만"

df= pd.read_csv('./data.csv', encoding='euc-kr')

# 웹페이지 제목
st.title('중고폰 사업 진출')
st.markdown('---')
st.markdown('### 네이버 쇼핑부')
st.markdown('* 네이버에서 중고폰 거래시장으로 진출하기 위한 데이터를 수집')
st.markdown("""
* 현재 고물가로 소비 추세가 감소하여 신규 휴대폰 구매가 감소 [링크](https://www.thelec.kr/news/articleView.html?idxno=21702)
    * 작년해 보다 14% 성장중. / 신규 스마트폰은 전년보다 2% 역성장. [링크](https://biz.chosun.com/it-science/ict/2023/07/18/OT577N5N6VEUZKNABO5VCA6VNE/)
    * 고물가가 한동안 유지될것으로 예상됨.
    * 중고폰 시장이 커질것으로 기대됨.
""")
st.markdown("""  
* 수집의 목적
    * 이번 데이터 수집은 앞으로 서비스 개발 시 기종 및 결함관련 데이터를 수집하여 참고자료로 사용 가능.
    * 추가적으로 AI 기술을 통해 현재 기종의 출시 날짜로부터 지난일, 결함 상태에 따라 자동적으로 가격을 예상할 수 있는 모델 개발 가능.
""")

st.markdown("""
* 서비스 개발 측면
    * 네이버 쇼핑팀에서 개발한다면, 네이버라는 이름으로 신뢰성을 기반으로 이용자로 부터 실물을 전달받아, 검수 과정만 거치면 됨.
        * 사용자들이 걱정하지 않고 사용할 가능성이 높음.
    * 또한, 이용자 중 구매자의 경우 남성과 여성, 각 나이 때 별로 분류하여 해당 휴대폰을 추천하는 시스템도 개발 가능.
    * 추가적으로, 비전 학습을 통해 이용자가 제공한 이미지를 기반으로 결함 상태도 파악할 수 있어 검수 과정도 줄일 수 있음.
""")

st.markdown("""
* 데이터 수집 
    * [폰가비](https://fongabi.com/fon_2/deal_live/)
    * 기종, 등급, 가격, 개봉여부, 미세손상, 외관손상, 내부LCD손상, 화면잔상, 기능불량을 수집.
""")

st.markdown("""
* 데이터 분석
    * 거래량이 정말 많음.
        * 평균 400건 정도.
    * 아이폰이 거래가 가장 활발하게 됨.
    * 워치 시리즈도 거래가 되고 있음.
        * 하지만, 데이터에서는 제외시킴.
    * 생각보다 예전의 휴대폰(갤럭시 S7 2016년 출시)이 거래가 꽤 되고 있음.
""")

model_counts = df['기종'].value_counts().reset_index() 
model_counts.columns = ['기종', '매물 개수']
unique_models = model_counts['기종'].tolist()
count_models= len(df['기종'].unique())

selected_model = st.selectbox(f"**기종을 선택하세요. 총 {count_models}개**", unique_models)

unique_capacity = df[df['기종'] == selected_model]['용량'].unique().tolist()
unique_capacity =sorted(unique_capacity, key=lambda x:x[:1])
selected_capacity = st.selectbox("**용량을 선택하세요.**", unique_capacity)
filtered_df = df[(df['기종'] == selected_model) & (df['용량'] == selected_capacity)]

if not filtered_df.empty:
    mean_price = filtered_df['가격'].mean()
    mean_price = int(round(filtered_df['가격'].mean(), -3))
    st.markdown(f'**{selected_model} {selected_capacity}의 평균 가격은 {mean_price}({format_price(mean_price)})원입니다.**')

    # 등급별 평균 가격 계산
    mean_prices = filtered_df.groupby('등급')['가격'].mean().apply(lambda x: format_price(round(x, -3))).reset_index()
    mean_prices.columns = ['등급', '평균가격']

    # 등급별 개수 계산
    grade_counts = filtered_df['등급'].value_counts().reset_index()
    grade_counts.columns = ['등급', '개수']

    # 두 데이터프레임 병합
    grade_data = pd.merge(grade_counts, mean_prices, on='등급')
    fig = px.bar(grade_data, x='등급', y='개수', title=f'{selected_model} {selected_capacity}의 등급별 개수 및 평균 가격',
                labels={'등급':'등급', '개수':'개수'}, color='등급', 
                hover_data=['평균가격'])  # hover_data 옵션을 사용하여 평균 가격 정보를 추가
    st.plotly_chart(fig)

    # 두 번째 열에 데이터프레임 출력하기
    unique_grades = filtered_df['등급'].unique().tolist()
    st.write('**자세히 살펴보기**')
    selected_grade = st.selectbox("등급을 선택하세요.", unique_grades)
    grade_df = filtered_df[filtered_df['등급'] == selected_grade][['개봉여부', '미세손상', '외관손상', '내부LCD손상', '화면잔상', '기능불량']]
    grade_df.reset_index(drop=True, inplace=True)
    st.dataframe(grade_df)

with st.expander('사용한 데이터 보기'):
    st.write(f"아래는 이 페이지를 만드는 데 사용한 데이터입니다.(총 {len(df)}개)")
    df = df[['기종','용량','등급', '가격', '개봉여부', '미세손상', '외관손상', '내부LCD손상', '화면잔상', '기능불량']]
    st.dataframe(df)
