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
       
    ss = st.session_state
    ss.setdefault("lista_mov", [])
    ss.setdefault("reset_inputs", False)

    # Si toca limpiar, hacerlo ANTES de crear los widgets
    if ss.reset_inputs:
        ss["concepto_key"] = ""
        ss["tipo_key"] = "Ingreso"
        ss["valor_key"] = 0.0
        ss.reset_inputs = False  # desactivar flag
    
    # Campos de entrada usando session state
    concepto_mov = st.text_input("Concepto:", key="concepto_key")
    tipo_mov = st.selectbox("Tipo:", ["Ingreso", "Gasto"], key="tipo_key")
    valor_mov = st.number_input("Valor:", value=0.0, key="valor_key")
    
    if st.button("Registrar movimiento"):
        if concepto_mov and valor_mov != 0:
            movimiento = [concepto_mov, tipo_mov, valor_mov]
            ss.lista_mov.append([concepto_mov, tipo_mov, valor_mov])
            ss.reset_inputs = True   # marcar para limpiar
            st.rerun()
            
                 
    if st.button("Mostrar movimientos"):
        if ss.lista_mov:
                st.dataframe(
                    pd.DataFrame(ss.lista_mov, columns=["Concepto", "Tipo", "Valor"]),
                    use_container_width=True
                )
        else:
            st.info("No hay movimientos")
    
elif modulo == "Ejercicio 2":
    st.subheader("Ejercicio 2")
    st.info("Por cada actividad a registrar, ingrese los siguientes datos:") 
    actividad = st.text_input("Nombre o descripción:")
    tipo = st.text_input("Tipo:")
    presupuesto = st.number_input("Presupuesto:")
    gasto = st.number_input("Gasto:")
    

    
                    
