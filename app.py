# Importamos Streamlit.
import streamlit as st


st.session_state
st.title("Fundamentos de Programación utilizando Python y Streamlit")
st.sidebar.title("Menú")

modulo =st.sidebar.selectbox("Elija un módulo",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

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
        .home-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem 2rem;
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .home-container h1 {
            font-size: 2.5rem;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        
        .info-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border-left: 5px solid #667eea;
    
   
