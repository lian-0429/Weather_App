import streamlit as st
import requests

st.title("Weather Search for Different Cities")

city = st.text_input("請輸入城市名稱 (英文，例如 Taipei):")

if city:
    st.write(f"正在搜尋 {city} 的天氣...")

    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()

    temp = data['current_condition'][0]['temp_C']
    desc = data['current_condition'][0]['weatherDesc'][0]['value']

    st.success(f"{city} 目前溫度: {temp}°C")
    st.info(f"天氣狀況: {desc}")