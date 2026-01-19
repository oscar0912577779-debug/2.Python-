import streamlit as st
from datetime import datetime

st.title("請選元素")
colorArray=["紅","綠","藍"]
optionIndex=st.selectbox("請選顏色",["紅","綠","藍"])
st.write(f"您選的是",optionIndex)
selectIndex = colorArray.index(optionIndex)
st.write("您選的是:",optionIndex,"SelectIndex:",selectIndex)

#多選
fruits= ['蘋果', '香蕉', '橙子', '葡萄', '西瓜']
optMult=st.multiselect("喜歡的水果",fruits)
st.write("選的水果:",optMult)


#單選單
optionRadio=st.radio("喜歡的季節",['春季','夏季','秋季','冬季'])
st.write("你選了",optionRadio)

optionSlider=st.select_slider("選範圍",
                                options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],value=('1','6')) #value=('1','6')開啟時的預設範圍
st.write("選擇範圍:",optionSlider)

valueSlider=st.slider("數字範圍:",0.0,100.0,value=(25.0,75.0)) #value=(25.0,75.0)開啟時的預設範圍
st.write("範圍:",valueSlider)
st.write("type:",type(valueSlider[0]))

chexkBox=st.checkbox("是否同意")
st.write("checkBox:",chexkBox)
if chexkBox:
    st.write("同意條款!")

dataInput=st.date_input("請選日期",datetime.today().date())
st.write("你選的日期:",dataInput)
    