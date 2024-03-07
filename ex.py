import streamlit as st
import pandas as pd
import numpy as np
from datetime import time, datetime

st.title("St.write")
st.header("Display text")
st.write('Hello,World! :sunglasses:')
st.header("Display numbers")
st.write(1234)
st.header("Display DataFrame")
df=pd.DataFrame({
             'First column':[1,2,3,4],
             'Second column':[10,20,30,40]})
st.write(df)
st.header("Accept multiple arguments")
st.write('Below is a DataFrame:',df,'Above is a dataframe')

# St.slide
st.title('St.slide')
a=st.slider('How old are you?',0,130,25)
st.write("I'm",a,"years old")
b=st.slider('Select a range of values',0.0,100.0,(10.0,20.2))
st.write('Values:', b)

#time 
c=st.slider("when do you start",value=(time(11,30),time(12,45)))
st.write("You're scheduled for:", c)

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.select_slider('pick a mark',['Bad','hot','Good','Excellent'])


#st.line_chart
st.subheader('st.line_chart')

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.write(chart_data)
st.line_chart(chart_data)

#st.selectbox
d=st.selectbox('Choisis ta couleur préférée',['Jaune','Bleu','Rouge'])
st.write('Ta couleur est',d)