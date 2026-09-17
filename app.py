import streamlit as st
import pandas as pd

st.title("☕ App Tính Tiền Quán Nước")

if "menu" not in st.session_state:
    st.session_state.menu = []

ten = st.text_input("Tên thức uống")
gia = st.number_input("Giá", min_value=0)

if st.button("Thêm món"):
    st.session_state.menu.append([ten, gia])

if st.session_state.menu:
    df = pd.DataFrame(
        st.session_state.menu,
        columns=["Tên món", "Giá"]
    )

    st.dataframe(df)

    tong = df["Giá"].sum()

    st.subheader(
        f"Tổng tiền: {tong:,.0f} VNĐ"
    )
