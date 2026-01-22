import streamlit as st
import pandas as pd

st.set_page_config(page_title="建築環境計画Ⅲ", layout="centered")

st.markdown("""
<style>
button {
    width: 100%;
    height: 60px;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_excel("建築環境計画Ⅲまとめ.ods", engine="odf", header=None)
terms = df[[1, 2]].dropna()
terms.columns = ["用語", "説明"]

st.title("📘 建築環境計画Ⅲ 学習アプリ")

item = terms.sample(1).iloc[0]
st.subheader(item["用語"])

if st.button("👀 答えを見る"):
    st.success(item["説明"])
