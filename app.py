import streamlit as st
import pandas as pd

st.title('تطبيق عرض بيانات الطلاب')

uploaded_file = st.file_uploader('ارفع ملف Excel للطلاب', type=['xlsx'])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
else:
    st.write('يرجى رفع ملف البيانات لعرضه هنا.')