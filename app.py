import streamlit as st
import pandas as pd
from textwrap import dedent

st.set_page_config(page_title="Fundamentos de Programación - Python y Streamlit", layout="centered")

st.title("Fundamentos de Programación utilizando Python y Streamlit")
st.sidebar.title("Menú")


# *********************************************
# NAVEGACIÓN ENTRE LAS OPCIONES DEL MENU
# *********************************************

# Creamos un selectbox en la barra lateral.

modulo = st.sidebar.selectbox("Elija un módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

# *********************************************
# HOME
# *********************************************

if modulo == "Home":
    home_html = dedent("""
    <section style="background:#ffffff; border:1px solid #e5e7eb; border-radius:12px; padding:20px; margin-top:12px;">
    <h3 style="margin-top:0;">Datos del proyecto</h3>
    <ul style="line-height:1.6; padding-left:18px;">
      <li><strong>Nombre completo del estudiante:</strong> Mónica Rantes García</li>
      <li><strong>Nombre del curso o módulo:</strong> Especialización en Python for Analytics</li>
      <li><strong>Año:</strong> 2026</li>
    </ul>
    </section>

    <section style="background:#ffffff; border:1px solid #e5e7eb; border-radius:12px; padding:20px; margin-top:12px;">
    <h3 style="margin-top:0;">Objetivo</h3>
    <p>
      Desarrollar una aplicación interactiva en Streamlit que integre los conceptos fundamentales
      aprendidos durante el Módulo 1 del curso, incluyendo variables, estructuras de datos, control
      de flujo, funciones, programación funcional y programación orientada a objetos (POO).
    </p>
    </section>

    <section style="background:#ffffff; border:1px solid #e5e7eb; border-radius:12px; padding:20px; margin-top:12px;">
    <h3 style="margin-top:0;">Tecnologías utilizadas</h3>
    <div style="display:flex; gap:8px; flex-wrap:wrap;">
      <span style="background:#f3f4f6; border:1px solid #e5e7eb; padding:6px 10px; border-radius:999px;">Python</span>
      <span style="background:#f3f4f6; border:1px solid #e5e7eb; padding:6px 10px; border-radius:999px;">Streamlit</span>
      <span style="background:#f3f4f6; border:1px solid #e5e7eb; padding:6px 10px; border-radius:999px;">NumPy</span>
    </div>
    </section>
    </div>
    """)
    st.components.v1.html(home_html, height=650, scrolling=True)

# *********************************************
# EJERCICIO 1
# *********************************************

elif modulo == "Ejercicio 1":
    st.subheader("Ejercicio 1")
       
    # *********************************************
    # INICIALIZACIÓN VALORES
    # *********************************************
    if 'concepto_input' not in st.session_state:
        st.session_state.concepto_input = ""
    if 'tipo_input' not in st.session_state:
        st.session_state.tipo_input = "Ingreso"
    if 'valor_input' not in st.session_state:
        st.session_state.valor_input = 0.0
    if 'lista_mov' not in st.session_state:
        st.session_state.lista_mov = []
    
    # Campos de entrada usando session state
    concepto_mov = st.text_input("Concepto:", 
                                value=st.session_state.concepto_input,
                                key="concepto_key")
    
    tipo_mov = st.selectbox("Tipo:", 
                           ["Ingreso", "Gasto"],
                           index=0 if st.session_state.tipo_input == "Ingreso" else 1,
                           key="tipo_key")
    
    valor_mov = st.number_input("Valor:", 
                               value=st.session_state.valor_input,
                               key="valor_key")
    
    if st.button("Registrar movimiento"):
        if concepto_mov and valor_mov != 0:
            movimiento = [concepto_mov, tipo_mov, valor_mov]
            st.session_state.lista_mov.append(movimiento)
            st.success("Registrado!")
            
            # Limpiar los campos
            st.session_state.concepto_input = ""
            st.session_state.tipo_input = "Ingreso"
            st.session_state.valor_input = 0.0
            st.rerun() #Para que se vean los campos limpios   
        
    if st.button("Mostrar movimientos"):
        if st.session_state.lista_mov:
            tabla = pd.DataFrame(st.session_state.lista_mov, columns=["Concepto", "Tipo", "Valor"])
            st.dataframe(tabla)
        else:
            st.info("No hay movimientos")
    
elif modulo == "Ejercicio 2":
    st.subheader("Ejercicio 2")
    st.info("Por cada actividad a registrar, ingrese los siguientes datos:") 
    actividad = st.text_input("Nombre o descripción:")
    tipo = st.text_input("Tipo:")
    presupuesto = st.number_input("Presupuesto:")
    gasto = st.number_input("Gasto:")
    

    
                    
