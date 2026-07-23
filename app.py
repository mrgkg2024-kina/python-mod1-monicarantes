import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp
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
    ss.setdefault("flash_msg", None)

    if ss.flash_msg:
        st.success(ss.flash_msg)
        ss.flash_msg = None
    
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

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Registrar movimiento"):
            if concepto_mov and valor_mov != 0:
                movimiento = [concepto_mov, tipo_mov, valor_mov]
                ss.lista_mov.append([concepto_mov, tipo_mov, float(valor_mov)])
                ss.reset_inputs = True   # marcar para limpiar
                ss.flash_msg = "Movimiento registrado"   # <- mensaje
                st.rerun()
                
    with col2:                 
        if st.button("Mostrar movimientos"):
            if ss.lista_mov:
                #st.dataframe(
                #    pd.DataFrame(ss.lista_mov, columns=["Concepto", "Tipo", "Valor"]),
                #    use_container_width=True)

                df = pd.DataFrame(ss.lista_mov, columns=["Concepto", "Tipo", "Valor"])
                st.dataframe(df, use_container_width=True)
                     
                suma_ingresos = df.loc[df["Tipo"] == "Ingreso", "Valor"].sum()
                suma_gastos = df.loc[df["Tipo"] == "Gasto", "Valor"].sum()
                saldo_final = suma_ingresos - suma_gastos

                st.write("Total de ingresos = ", suma_ingresos )
                st.write("Total de gastos = ", suma_gastos )  
                st.write("Saldo final = ", saldo_final)
                
            else:
                st.info("No hay movimientos")
                
    if st.button("🗑️ Limpiar todo"):
        ss.lista_mov = []
        ss.reset_inputs = True
        st.rerun()

# *********************************************
# EJERCICIO 2
# *********************************************

elif modulo == "Ejercicio 2":
    st.subheader("Ejercicio 2")
    st.info("Por cada registro de producto, ingrese los siguientes datos:") 

    # Arrays en session_state
    st.session_state.setdefault("nombres", [])
    st.session_state.setdefault("categorias", [])
    st.session_state.setdefault("precios", [])
    st.session_state.setdefault("cantidades", [])
    st.session_state.setdefault("totales", [])
    st.session_state.setdefault("clear_inputs", False)

    # Limpiar en el siguiente ciclo antes de dibujar widgets
    if st.session_state.clear_inputs:
        st.session_state["nombre_prod_key"] = ""
        st.session_state["categoria_key"] = "Electrónico"
        st.session_state["precio_key"] = 0.0
        st.session_state["cantidad_key"] = 1
        st.session_state.clear_inputs = False
    
    nombre_prod = st.text_input("Nombre del producto:", key="nombre_prod_key")
    categoria = st.selectbox("Categoria:", ["Electrónico", "Ropa", "Hogar", "Deportes"], key="categoria_key")
    precio = st.number_input("Precio:", min_value=0.0, format="%.2f", key="precio_key")
    cantidad = st.number_input("Cantidad:", value=1, key="cantidad_key")
    total = precio * cantidad

    # Mostrar total como campo de solo lectura
    st.number_input("Total", value=total, disabled=True, format="%.2f")

   # Agregar
    if st.button("Agregar"):
        if nombre_prod.strip():
            st.session_state.nombres.append(nombre_prod.strip())
            st.session_state.categorias.append(categoria)
            st.session_state.precios.append(precio)
            st.session_state.cantidades.append(cantidad)
            st.session_state.totales.append(total)

            st.session_state.clear_inputs = True
            st.rerun()
     
        else:
            st.error("Ingresa el nombre.")

    # DataFrame
    df = pd.DataFrame({
        "Nombre_producto": st.session_state.nombres,
        "Categoría": st.session_state.categorias,
        "Precio": st.session_state.precios,
        "Cantidad": st.session_state.cantidades,
        "Total": st.session_state.totales
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# *********************************************
# EJERCICIO 3
# *********************************************

elif modulo == "Ejercicio 3":
    tiempo_th = st.number_input("Tiempo total en horas:", min_value=0.0, format="%.2f", key="tiempo_th__key")
    tiempo_ch = st.number_input("Tiempo caída en horas:", min_value=0.0, format="%.2f", key="tiempo_ch__key")    

    colA, colB = st.columns(2)
    
    with colA:
        if st.button("Calcular disponibilidad"):
        dispo_pct = {}
        dispo_pct = lfp.calcular_disponibilidad_sistema(tiempo_th, tiempo_ch)
        st.write(dispo_pct)
    with colB:
        df = pd.DataFrame(dispo_pct)
         st.dataframe(df, use_container_width=True, hide_index=True)
                    
