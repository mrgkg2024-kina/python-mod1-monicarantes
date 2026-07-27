import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lfp
import libreria_clases_proyecto1 as lcp
from textwrap import dedent

st.set_page_config(page_title="Fundamentos de Programación - Python y Streamlit", layout="centered")

st.title("Proyecto1 - Aplicación en Streamlit")
st.sidebar.title("Menú")

col1, col2, col3 = st.columns([1,1,1])
with col1: st.image("python_logo2.jpg", width=80)
with col2: st.image("Numpy_logo.jpg", width=150)
with col3: st.image("Pandas_logo2.jpg", width=100)

st.sidebar.image("DMC.png",width=200)


# *********************************************
# NAVEGACIÓN ENTRE LAS OPCIONES DEL MENU
# *********************************************

# Creamos un selectbox en la barra lateral.

modulo = st.sidebar.selectbox("Elija un módulo", ["Home","Home2","Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

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
      <span style="background:#f3f4f6; border:1px solid #e5e7eb; padding:6px 10px; border-radius:999px;">Pandas</span>
    </div>
    </section>
    </div>
    """)
    st.components.v1.html(home_html, height=650, scrolling=True)

elif modulo == "Home2":
    st.markdown(dedent("""
    <div class="wrap">
      <section class="card">
        <h3>Datos del proyecto</h3>
        <ul>
          <li><strong>Nombre completo del estudiante:</strong> Mónica Rantes García</li>
          <li><strong>Nombre del curso o módulo:</strong> Especialización en Python for Analytics</li>
          <li><strong>Año:</strong> 2026</li>
        </ul>
      </section>
    
      <section class="card">
        <h3>Objetivo</h3>
        <p>
          Desarrollar una aplicación interactiva en Streamlit que integre los conceptos fundamentales
          del Módulo 1: variables, estructuras de datos, control de flujo, funciones, programación funcional y POO.
        </p>
      </section>
    
      <section class="card">
        <h3>Tecnologías utilizadas</h3>
        <div class="chips">
          <span class="chip">Python</span>
          <span class="chip">Streamlit</span>
          <span class="chip">NumPy</span>
          <span class="chip">Pandas</span>
        </div>
      </section>
    </div>
"""), unsafe_allow_html=True)

    

# *********************************************
# EJERCICIO 1
# *********************************************

elif modulo == "Ejercicio 1":
    st.subheader("Ejercicio 1 – Flujo de caja con listas ")
    st.markdown("""En este ejercicio se registrarán movimientos financieros en una lista vacía. Por cada movimiento se registrará el concepto, 
                tipo y valor. Al final del ejercicio se mostrará si el flujo de caja es a favor o en contra.""")  
    st.info("Ingresar los siguientes datos:")
    
    st.session_state.setdefault("lista_mov", [])
    st.session_state.setdefault("reset_inputs", False)
    st.session_state.setdefault("flash_msg", None)

    if st.session_state.flash_msg:
        st.success(st.session_state.flash_msg)
        st.session_state.flash_msg = None
    
    # Si toca limpiar, hacerlo ANTES de crear los widgets
    if st.session_state.reset_inputs:
        st.session_state["concepto_key"] = ""
        st.session_state["tipo_key"] = "Ingreso"
        st.session_state["valor_key"] = 0.0
        st.session_state.reset_inputs = False  # desactivar flag
       
    
    # Campos de entrada usando session state
    concepto_mov = st.text_input("Concepto:", key="concepto_key")
    tipo_mov = st.selectbox("Tipo:", ["Ingreso", "Gasto"], key="tipo_key")
    valor_mov = st.number_input("Valor:", min_value=0.0, format="%.2f", key="valor_key")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Registrar movimiento"):
            if concepto_mov and valor_mov != 0:
                #movimiento = [concepto_mov, tipo_mov, valor_mov]
                st.session_state.lista_mov.append([concepto_mov, tipo_mov, valor_mov])
                st.session_state.reset_inputs = True   # marcar para limpiar
                st.session_state.flash_msg = "Movimiento registrado"   # <- mensaje
                st.rerun()
            else:
                st.error("Completar datos para el registro")
    with col2:  
        if st.button("🗑️ Limpiar"):
            st.session_state.lista_mov = []
            st.session_state.reset_inputs = True
            st.rerun()

                   
    if st.button("Mostrar movimientos"):
        if st.session_state.lista_mov:
            df = pd.DataFrame(st.session_state.lista_mov, columns=["Concepto", "Tipo", "Valor"])
            st.dataframe(df, use_container_width=True)
                     
            suma_ingresos = df.loc[df["Tipo"] == "Ingreso", "Valor"].sum()
            suma_gastos = df.loc[df["Tipo"] == "Gasto", "Valor"].sum()
            saldo_final = suma_ingresos - suma_gastos

            st.write(f"Total de ingresos = {suma_ingresos:.2f}")
            st.write(f"Total de gastos = {suma_gastos:.2f}" )  
            st.write(f"Saldo final = {saldo_final:.2f}")
            
            if saldo_final >= 0.0:
                st.success ("Flujo de caja a favor")    
            else:
                st.success ("Flujo de caja en contra")
        else:
            st.info("No hay movimientos")



# *********************************************
# EJERCICIO 2
# *********************************************

elif modulo == "Ejercicio 2":
    st.subheader(" Ejercicio 2 – Registro con NumPy, arrays y DataFrame")
    st.markdown("""En este ejercicio se registrará información usando arreglos de NumPy. Cada vez que el usuario presione el botón Agregar, 
                la información se almacenará en arrays y se mostrará en un DataFrame.""")
     
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
    st.subheader("Ejercicio 3 – Uso de funciones desde una librería externa ")
    st.markdown("""En este ejercicio se utilizará la función calcular_disponibilidad_sistema del archivo de funciones libreria_funciones_proyecto1.py .
                Luego de ingresar los parámetros requeridos, se ejecutará la función indicada y se mostrarán los resultados.""")
               
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
    st.subheader(" Ejercicio 4 – Uso de clases desde una librería externa con CRUD")
    st.markdown("""En este ejercicio se utilizará la clase Servidor del archivo de clases libreria_clases_proyecto1.py .
                Luego de ejecutar el método resumen, de la clase, se implementarán operaciones básicas tipo CRUD.""")
    st.info("Calcular disponibilidad del servidor")

    resumen={}
    st.session_state.setdefault("servidores", [])
    st.session_state.setdefault("tiempo_total", [])
    st.session_state.setdefault("tiempo_caida", [])
    st.session_state.setdefault("almacenamiento_total", [])
    st.session_state.setdefault("almacenamiento_usado", [])
    st.session_state.setdefault("dispo_pct", [])
    st.session_state.setdefault("clear_inputs", False)
    st.session_state.setdefault("ok_actualizado", False)
    st.session_state.setdefault("ok_eliminado", False)
    
    # Limpiar en el siguiente ciclo antes de dibujar widgets
    if st.session_state.clear_inputs:
        st.session_state["nombre_serv_key"] = ""
        st.session_state["tth_key"] = 0.0
        st.session_state["tch_key"] = 0.0
        st.session_state["almacenamiento_tgb_key"] = 300
        st.session_state["almacenamiento_ugb_key"] = 250
        st.session_state.clear_inputs = False
 

    nombre_serv = st.text_input("Nombre del servidor:", key="nombre_serv_key")
    tiempo_th = st.number_input("Tiempo total (h)", min_value=0.0, format="%.2f", key="tth_key")
    tiempo_ch = st.number_input("Tiempo caída (h)", min_value=0.0, format="%.2f",key="tch_key")
    almacenamiento_tgb = st.selectbox("Almacenamiento total (GB)", [300,350,400,450,500], key="almacenamiento_tgb_key")
    almacenamiento_ugb = st.selectbox("Almacenamiento usado (GB)", [250,300,350,400,450], key="almacenamiento_ugb_key")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Calcular y guardar"):
            if tiempo_th <= 0.0:
               st.error("Tiempo total debe ser > 0.0")
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
                    st.session_state.dispo_pct.append(resumen["disponibilidad_pct"])
                    st.session_state["ultimo_resumen"] = resumen
                    st.session_state.clear_inputs = True
                    st.rerun()
                else:
                    st.error("Ingresa nombre del servidor")

    def cargar_ultimo():
        if not st.session_state.servidores:
            st.session_state["msg_error"] = "No hay registros para leer."
            return
        i = -1
        st.session_state["nombre_serv_key"] = st.session_state.servidores[i]
        st.session_state["tth_key"] = float(st.session_state.tiempo_total[i])
        st.session_state["tch_key"] = float(st.session_state.tiempo_caida[i])
        st.session_state["almacenamiento_tgb_key"] = int(st.session_state.almacenamiento_total[i])
        st.session_state["almacenamiento_ugb_key"] = int(st.session_state.almacenamiento_usado[i])

    with col2:
        st.button("Leer último registro", on_click=cargar_ultimo)
        if st.session_state.get("msg_error"):
            st.error(st.session_state.pop("msg_error"))
        
    with col3:
        if st.button("Actualizar último registro"):
            if not st.session_state.servidores:
                st.error("No hay registros para actualizar.")
            elif tiempo_th <= 0.0:
                st.error("Tiempo total debe ser > 0.0")
            elif tiempo_ch > tiempo_th:
                st.error("La caída no puede superar el total.")
            elif almacenamiento_ugb > almacenamiento_tgb:
                st.error("El almacenamiento usado no puede superar el almacenamiento total.")
            else:
                if nombre_serv.strip():
                     i = - 1
                     st.session_state.servidores[i] = nombre_serv or st.session_state.servidores[i]
                     st.session_state.tiempo_total[i] = tiempo_th or st.session_state.tiempo_total[i]
                     st.session_state.tiempo_caida[i] = tiempo_ch or st.session_state.tiempo_caida[i]
                     st.session_state.almacenamiento_total[i] = almacenamiento_tgb or st.session_state.almacenamiento_total[i]
                     st.session_state.almacenamiento_usado[i] = almacenamiento_ugb or st.session_state.almacenamiento_usado[i]
                    
                     try:
                        srv = lcp.Servidor(
                        st.session_state.servidores[i],
                        st.session_state.tiempo_total[i],
                        st.session_state.tiempo_caida[i],
                        st.session_state.almacenamiento_total[i],
                        st.session_state.almacenamiento_usado[i],
                        )
                        st.session_state["ultimo_resumen"] = srv.resumen()
                        st.session_state.dispo_pct[i]=st.session_state["ultimo_resumen"]["disponibilidad_pct"]
                        st.session_state.clear_inputs = True
                         
                     except Exception as e:
                        st.warning(f"No se pudo recalcular el resumen: {e}")
                        
                     # Activa flag y recarga
                     st.session_state.ok_actualizado = True  
                     st.rerun()
                else:
                    st.error("Ingresa nombre del servidor")

    if st.session_state.ok_actualizado:
        st.success("Último registro actualizado")
        st.session_state.ok_actualizado = False

    with col4:
        if st.button("Eliminar último registro"):
            if not st.session_state.servidores:
                st.error("No hay registros para eliminar.")
            else:
                # Eliminar último de cada lista
                st.session_state.servidores.pop()
                st.session_state.tiempo_total.pop()
                st.session_state.tiempo_caida.pop()
                st.session_state.almacenamiento_total.pop()
                st.session_state.almacenamiento_usado.pop()
                st.session_state.dispo_pct.pop()
                st.session_state.pop("ultimo_resumen", None) 
                st.session_state.ok_eliminado = True  
                st.rerun()

    if st.session_state.ok_eliminado:
        st.success("Último registro eliminado")
        st.session_state.ok_eliminado = False

    with col5:
        if st.button("🗑️ Limpiar todo"):
            st.session_state.servidores = []
            st.session_state.tiempo_total = []
            st.session_state.tiempo_caida = []
            st.session_state.almacenamiento_total = []
            st.session_state.almacenamiento_usado = []
            st.session_state.dispo_pct = []
            st.session_state.pop("ultimo_resumen", None)
            st.session_state.clear_inputs = True
            st.rerun()  
    
    if st.session_state.servidores:
        st.write(st.session_state.get("ultimo_resumen"))
        df = pd.DataFrame({
            "Nombre_servidor": st.session_state.servidores,
            "Tiempo total (h)": st.session_state.tiempo_total,
            "Tiempo caída (h)": st.session_state.tiempo_caida,
            "Alm. total (GB)": st.session_state.almacenamiento_total,
            "Alm. usado (GB)": st.session_state.almacenamiento_usado,
            "Disponibilidad": st.session_state.dispo_pct
        })
        st.dataframe(df, use_container_width=True, hide_index=True)         
    
  
         



