import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp
import libreria_clases_proyecto1 as lcp
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
    st.subheader("Ejercicio 3")
    st.info("Calcular disponibilidad del sistema")

    res ={}
    st.session_state.setdefault("tiempos_th", [])
    st.session_state.setdefault("tiempos_ch", [])
    st.session_state.setdefault("dispos", [])
    st.session_state.setdefault("clear_inputs", False)

    # Limpiar en el siguiente ciclo antes de dibujar widgets
    if st.session_state.clear_inputs:
        st.session_state["th_key"] = 0.0
        st.session_state["ch_key"] = 0.0
        st.session_state.clear_inputs = False
    

    th = st.number_input("Tiempo total (h)", min_value=0.0, format="%.2f", key="th_key")
    ch = st.number_input("Tiempo caída (h)", min_value=0.0, format="%.2f",key="ch_key")

    if st.button("Calcular y guardar"):
        if th <= 0:
            st.error("Tiempo total debe ser > 0.")
        elif ch > th:
            st.error("La caída no puede superar el total.")
        else:
            res = lfp.calcular_disponibilidad_sistema(th, ch)  # siempre dict
            dispo = res.values()  # ajusta la clave si es otra
            st.session_state.tiempos_th.append(th)
            st.session_state.tiempos_ch.append(ch)
            st.session_state.dispos.append(dispo)
            st.write(res)
            st.session_state.clear_inputs = True
            st.rerun()

    if st.session_state.tiempos_th:
        df = pd.DataFrame({
            "Tiempo total (h)": st.session_state.tiempos_th,
            "Tiempo caída (h)": st.session_state.tiempos_ch,
            "Disponibilidad (%)": st.session_state.dispos
        })
        st.dataframe(df, use_container_width=True, hide_index=True)


# *********************************************
# EJERCICIO 4
# *********************************************
elif modulo == "Ejercicio 4":
    st.subheader("Ejercicio 4")
    st.info("Calcular disponibilidad del servidor")

    resumen={}
    st.session_state.setdefault("servidores", [])
    st.session_state.setdefault("tiempo_total", [])
    st.session_state.setdefault("tiempo_caida", [])
    st.session_state.setdefault("almacenamiento_total", [])
    st.session_state.setdefault("almacenamiento_usado", [])
    st.session_state.setdefault("clear_inputs", False)
    
    # Limpiar en el siguiente ciclo antes de dibujar widgets
    if st.session_state.clear_inputs:
        st.session_state["nombre_serv_key"] = ""
        st.session_state["tth_key"] = 0.0
        st.session_state["tch_key"] = 0.0
        st.session_state["almacenamiento_tgb__key"] = 300
        st.session_state["almacenamiento_ugb__key"] = 250
        st.session_state.clear_inputs = False
 

    nombre_serv = st.text_input("Nombre del servidor:", key="nombre_serv_key")
    tiempo_th = st.number_input("Tiempo total (h)", min_value=0.0, format="%.2f", key="tth_key")
    tiempo_ch = st.number_input("Tiempo caída (h)", min_value=0.0, format="%.2f",key="tch_key")
    almacenamiento_tgb = st.selectbox("Almacenamiento total (GB)", [300,350,400,450,500], key="almacenamiento_tgb__key")
    almacenamiento_ugb = st.selectbox("Almacenamiento usado (GB)", [250,300,350,400,450], key="almacenamiento_ugb__key")

    if st.button("Calcular y guardar"):
        if tiempo_th <= 0.0:
           st.error("Tiempo total debe ser > 0.")
        elif tiempo_ch > tiempo_th:
            st.error("La caída no puede superar el total.")
        elif almacenamiento_ugb > almacenamiento_tgb:
            st.error("El almacenamiento usado no puede superar el almacenamiento total.")
        else:
            if nombre_serv.strip():
                servidor_nvo = lcp.Servidor(nombre_serv,tiempo_th,tiempo_ch,almacenamiento_tgb,almacenamiento_ugb)
                resumen = servidor_nvo.resumen()
                st.session_state.servidores.append(nombre_serv.strip())
                st.session_state.tiempo_total.append(tiempo_th)
                st.session_state.tiempo_caida.append(tiempo_ch)
                st.session_state.almacenamiento_total.append(almacenamiento_tgb)
                st.session_state.almacenamiento_usado.append(almacenamiento_ugb)
                st.session_state["ultimo_resumen"] = resumen
                st.session_state.clear_inputs = True
                st.rerun()
            else:
                st.error("Ingresa nombre del servidor")

    if st.session_state.servidores:
        st.write(st.session_state.get("ultimo_resumen"))
        df = pd.DataFrame({
            "Nombre_servidor": st.session_state.servidores,
            "Tiempo total (h)": st.session_state.tiempo_total,
            "Tiempo caída (h)": st.session_state.tiempo_caida,
            "Alm. total (GB)": st.session_state.almacenamiento_total,
            "Alm. usado (GB)": st.session_state.almacenamiento_usado,
        })
        st.dataframe(df, use_container_width=True, hide_index=True)         
    
    if st.button("🗑️ Limpiar"):
        st.session_state.servidores,st.session_state.tiempo_total,st.session_state.tiempo_caida,st.session_state.almacenamiento_total,
        st.session_state.almacenamiento_usado =[]
        ss.reset_inputs = True
        st.rerun()      
         



