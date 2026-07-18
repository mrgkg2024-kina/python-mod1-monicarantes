# Importamos Streamlit.
import streamlit as st


st.session_state
st.title("Fundamentos de Programación utilizando Python y Streamlit")
st.sidebar.title("Menú")

modulo =st.sidebar.selectbox("Elija un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
    
    # Título principal
    st.markdown("""
    <div class="main-title">
        <h1>🏠 Presentación del Proyecto</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Datos del proyecto
    datos_proyecto = {
        "Título del proyecto": "Módulo 1 – Python Fundamentals",
        "Nombre completo del estudiante": "Mónica Rantes García",
        "Nombre del curso o módulo": "Especialización en Python for Analytics",
        "Año": "2026",
        "Breve descripción del objetivo del trabajo": "Desarrollar una aplicación interactiva en Streamlit que integre los conceptos fundamentales aprendidos durante el Módulo 1 del curso, incluyendo variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO).",
        "Lista de tecnologías utilizadas": "Python, Streamlit, NumPy"
    }
    
    # Información principal en tarjeta grande
    with st.container():
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📚 Curso", "Python for\nAnalytics")
        with col2:
            st.metric("👤 Estudiante", "Mónica Rantes\nGarcía")
        with col3:
            st.metric("📅 Año", "2026")
    
    st.divider()
    
    # Detalles del proyecto
    for idx, (clave, valor) in enumerate(datos_proyecto.items(), 1):
        with st.expander(f"📋 {clave}", expanded=(idx == 1)):
            st.write(valor)
    
   
