import streamlit as st
import pandas as pd
import os

# Configurar colores de la interfaz
st.set_page_config(page_title="Validación de Inputs", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #e6f2ff; /* Azul claro */
        color: #003366; /* Azul oscuro */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Función para validar entradas
def validate_input(input_value, length, prefix=None):
    if not input_value.isdigit():
        return False, "El valor contiene caracteres no numéricos."
    if len(input_value) != length:
        return False, f"Debe tener exactamente {length} dígitos."
    if prefix and not input_value.startswith(prefix):
        return False, f"Debe comenzar con '{prefix}'."
    return True, ""

# Función para procesar datos
def process_inputs(input1, input2):
    sscc = input1[-18:]  # Últimos 18 dígitos del input1
    material = input2[2:10]  # Dígitos 3 al 10
    cantidad = input2[15:18]  # Dígitos 16 al 18
    lote = input2[-9:]  # Últimos 9 dígitos
    return sscc, material, cantidad, lote

# Título de la app
st.title("Aplicación de Validación y Procesamiento de Inputs")
st.write("Ingrese los valores para validar, procesar y guardar los datos.")

# Campos de entrada
input1 = st.text_input("Ingrese el primer valor (20 dígitos):")
input2 = st.text_input("Ingrese el segundo valor (40 dígitos):")
input3 = st.text_input("Texto adicional (opcional):")

# Validar y guardar
if st.button("Validar y Guardar"):
    valid1, error1 = validate_input(input1, 20, "003")
    valid2, error2 = validate_input(input2, 40, "90")
    
    if not valid1:
        st.error(f"Error en Input 1: {error1}")
    elif not valid2:
        st.error(f"Error en Input 2: {error2}")
    else:
        sscc, material, cantidad, lote = process_inputs(input1, input2)
        st.success("Todos los valores son válidos. Se guardarán en el archivo.")
        
        # Guardar en Excel como cadenas
        file_name = "datos.xlsx"
        new_data = {
            "SSCC": [sscc],
            "Material": [material],
            "Cantidad por pallet": [cantidad],
            "Lote": [lote],
            "Texto Adicional": [input3],
        }
        df_new = pd.DataFrame(new_data, dtype=str)  # Asegurar que todo es texto
        
        if os.path.exists(file_name):
            df_existing = pd.read_excel(file_name, dtype=str)  # Leer como texto
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            df_combined.to_excel(file_name, index=False, engine='openpyxl')  # Escribir como texto
        else:
            df_new.to_excel(file_name, index=False, engine='openpyxl')  # Crear archivo nuevo
        
        st.write("Datos guardados exitosamente en `datos.xlsx`.")
        st.write(df_new)

# Botón para borrar datos existentes
if st.button("Borrar Datos Previos"):
    if os.path.exists("datos.xlsx"):
        os.remove("datos.xlsx")
        st.success("Datos anteriores eliminados.")
    else:
        st.warning("No hay datos previos para borrar.")

# Mostrar datos guardados (opcional)
if os.path.exists("datos.xlsx"):
    st.write("Datos guardados actualmente:")
    st.dataframe(pd.read_excel("datos.xlsx", dtype=str))  # Mostrar como texto

