# Importamos Streamlit.
import streamlit as st


st.session_state
st.title("Fundamentos de Programación utilizando Python y Streamlit")
st.sidebar.title("Menú")

if modulo == "Home":
    
    # Datos del proyecto
    datos_proyecto = {
        "Título del proyecto": "Módulo 1 – Python Fundamentals",
        "Nombre completo del estudiante": "Mónica Rantes García",
        "Nombre del curso o módulo": "Especialización en Python for Analytics",
        "Año": "2026",
        "Breve descripción del objetivo del trabajo": "Desarrollar una aplicación interactiva en Streamlit que integre los conceptos fundamentales aprendidos durante el Módulo 1 del curso, incluyendo variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO).",
        "Lista de tecnologías utilizadas": "Python, Streamlit, NumPy"
    }
    
    # HTML mejorado
    html_content = """
    <style>
        .home-container { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3rem 2rem; border-radius: 15px; color: white; }
        .info-card { background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 5px solid #667eea; }
        .info-card h3 { color: #667eea; margin: 0 0 1rem 0; }
        .info-card p { color: #555; margin: 0; line-height: 1.6; }
    </style>
    
    <div class="home-container">
        <h1>🏠 Presentación del Proyecto</h1>
    </div>
    
    <div class="info-card">
        <h3>Título</h3>
        <p>Módulo 1 – Python Fundamentals</p>
    </div>
    
    <div class="info-card">
        <h3>Estudiante</h3>
        <p>Mónica Rantes García</p>
    </div>
    
    <div class="info-card">
        <h3>Curso</h3>
        <p>Especialización en Python for Analytics</p>
    </div>
    """
    
    st.markdown(html_content, unsafe_allow_html=True)
