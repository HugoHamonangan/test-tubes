import streamlit as st
from custom_module.custom import *


def luas_persegi():
    st.header("BANGUN DATAR PERSEGI")

    st.subheader("Mencari Luas")

    luas_persegi = st.number_input("Masukkan Sisi :")

    btn_luas = btnhasil(1)

    if btn_luas:
        result_luas = luas_persegi * luas_persegi

        rumusbangundatar("Luas", "Persegi", "S x S")

        resultbangundatar("Luas", "Persegi", result_luas)


def keliling_persegi():
    st.subheader("Mencari Keliling")

    keliling_persegi = st.number_input("Masukkan Sisi : ")

    btn_keliling = btnhasil(2)

    if btn_keliling:

        result_keliling = keliling_persegi * 4

        rumusbangundatar("Keliling", "Persegi", "S x 4")

        resultbangundatar("Keliling", "Persegi", result_keliling)


def persegi():
    import streamlit as st
    luas_persegi()
    keliling_persegi()