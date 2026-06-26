import streamlit as st
import requests

url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
API_KEY = "XXX"

def get_weather_cwa(city_name):
    params = {
        "authorization": API_KEY,
        "location": city_name,
        "format" : "JSON"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def parse_weather_data(data):
    try:
        location = data['records']['location'][0]
        weather_elements = location['weatherElement']
        weather_desc = weather_elements[0]['time'][0]['parameter']['parameterName']
        temp_min = weather_elements[2]['time'][0]['parameter']['parameterName']
        temp_max = weather_elements[4]['time'][0]['parameter']['parameterName']
        return f"天氣為 {weather_desc}，氣溫約 {temp_min}°C - {temp_max}°C"
    except (KeyError, IndexError):
        return "無法解析氣象資料，請檢查城市名稱是否正確。"


st.title('天氣小管家')
city = st.text_input('What city do you want to search')
if st.button("查詢"): # 按下按鈕才開始跑

    if city:  # 如果 city 不是空的
        raw_data = get_weather_cwa(city) # 呼叫函數，就像派人去執行任務
        if raw_data:  # 如果拿到了資料
            result = parse_weather_data(raw_data)
            st.write(result)
            st.success('Your searching is success.')
            # 繼續往下走
        else:  # 如果沒拿到 (None)
            st.error("API 連線失敗")  # 對應你的「報Error 查無資料」

    else:  # 否則
        st.warning("請先輸入縣市")  # 對應你的「報Error 查無城市」
