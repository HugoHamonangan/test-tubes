import streamlit as st


def btnhasil(count):
    return st.button("Hasil", key=count)


def resultbangundatar(types, category, param):
    return st.success(f"{types} {category} adalah : {param} Cm")


def rumusbangundatar(types, category, param):
    return st.info(f"Rumus {types} {category} : {param}")


def resultsuhu(types, category, param):
    return st.success(f"{types} {category} adalah : {param}")


def rumussuhu(types, category, param):
    return st.info(f"Rumus {types} {category} : {param}")


def resultoperator(types, category, param):
    return st.info(f"{types} {category} adalah : {param}")


def rumusoperator(types, category, param):
    return st.info(f"Rumus {types} {category} : {param}")
