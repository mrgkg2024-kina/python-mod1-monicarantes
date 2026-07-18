# Importamos Streamlit.
import streamlit as st


st.session_state
st.title("Fundamentos de Programación utilizando Python y Streamlit")
st.sidebar.title("Menú")

modulo =st.sidebar.selectbox("Elija un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":

    st.header("Presentación del Proyecto")

    st.write("Título del proyecto            : Módulo 1 – Python Fundamentals")
    st.write("Nombre completo del estudiante : Mónica Rantes García")
    st.write("Nombre del curso o módulo: Especialización en Python for Analytics")
    st.write("Año :2026")
    st.write("Breve descripción del objetivo del trabajo : Desarrollar una aplicación interactiva en Streamlit que integre los conceptos fundamentales aprendidos durante el Módulo 1 del curso, incluyendo variables,estructuras de datos, control de flujo, funciones,programación funcional y programación orientada a objetos (POO). ")
    st.write("Lista de tecnologías utilizadas: Python, Streamlit, NumPy")        
    
   
