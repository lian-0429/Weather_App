import streamlit as st
import requests

st.title('天氣查詢APP')
city = st.text_input('請輸入一個城市')

if city:
    url = f'https://wttr.in/{city}?format=j1'
    read = requests.get(url)

    if read.status_code == 200:
        data = read.json()
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        st.success(f'目前{city}的溫度為{temp}，天氣狀況為{desc}')
        st.info('謝謝您的查詢')
    else:
        st.error('查無此城市')
