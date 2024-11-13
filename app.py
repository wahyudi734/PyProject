import streamlit as st
import pandas as pd
import numpy as np

st.title("My New Apps")
st.subheader("Belajar menulis python app menggunaka streamlit")

st.text_input("Nama")
ttl = st.date_input("Tanggal lahir","today")

v_alignment = st.selectbox(
     "Vertical alignment", ["top", "center", "bottom"], index=2
)


left, middle, right = st.columns(3,vertical_alignment=v_alignment,gap="medium")
with left:
    st.header("A cat")
middle.text("Tengah")
right.text("Kanan")
