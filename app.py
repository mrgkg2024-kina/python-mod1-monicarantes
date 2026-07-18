# Importamos Streamlit.
import streamlit as st


st.session_state
st.title("Fundamentos de Programación utilizando Python y Streamlit")
st.sidebar.title("Menú")

modulo =st.sidebar.selectbox("Elija un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
    
    # Título principal con estilo
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
    
    # Mostrar datos en contenedores individuales
    col1, col2 = st.columns([3, 1])
    
    with col1:
        for clave, valor in datos_proyecto.items():
            with st.container():
                st.markdown(f"### 📌 {clave}")
                st.write(valor)
                st.divider()
    
    with col2:
        st.markdown("### 📊 Resumen Rápido")
        st.info(f"""
        **Estudiante:** Mónica Rantes García
        
        **Curso:** Python for Analytics
        
        **Año:** 2026
        
        **Tecnologías:** 3
        """)
    
   
