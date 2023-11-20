from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

grade, price,times, phone, status, tiny, frame, lcd, screen, malfuction = [],[],[],[],[],[],[],[],[],[]
url='https://fongabi.com/fon_2/deal_live/'
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
body = browser.find_element(By.CSS_SELECTOR,'body')
try:
    for i in range(1,1500):
        print('진행확인: ', i)
        de_pr = soup.select('.list > .row')[i-1].select('.f_22')[0].get_text()
        name = soup.select('h4.f_26')[i-1].get_text().strip()
        tim =soup.select('.time')[i-1].get_text().strip()
        de_pr = de_pr.replace('\xa0', ' ')
        de_pr_list = de_pr.split(' ')
        grade.append(de_pr[0])
        price.append(de_pr_list[1])
        times.append(tim)
        phone.append(name)
        # 클릭 후 내부에서 정보 얻기
        body.send_keys(Keys.END)
        wait = WebDriverWait(browser, 500) # 최대 500초까지 기다리기
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.list > div:nth-child(' +str(i)+ ')')))
        element.click()
        time.sleep(1)
        # 내부 정보 저장.
        data=browser.find_elements(By.CSS_SELECTOR,'#phone_condition > dd > table > tbody > tr > td:nth-child(2)')
        status.append(data[0].text)
        tiny.append(data[1].text)
        frame.append(data[2].text)
        lcd.append(data[3].text)
        screen.append(data[4].text)
        malfuction.append(data[5].text)
        browser.back()
        time.sleep(1+0.3*i//50)
        if i%10==0:
            # 가장 아래로 내리기
            more_btn = browser.find_element(By.ID, 'btn_review_more') 
            # 더보기 버튼 클릭.
            more_btn.click()
            time.sleep(1)
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
except Exception as e:
    print('중단되었습니다', e)
    # 저장.
    data1= pd.DataFrame(zip(times,grade,price,phone,status,tiny,frame,lcd,screen,malfuction))
    data1.columns=['시간', '등급','가격','이름','개봉여부','미세손상','외관손상','내부LCD손상','화면잔상','기능불량']
    data1.to_csv('raw.csv',encoding='euc-kr',index=False)
            