import streamlit as st


st.session_state
st.title("Proyecto Aplicado en Streamlit – Fundamentos de Programación")
st.sidebar.title("Menú")

modulo =st.sidebar.selectbox("Elija un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
