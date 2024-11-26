# archivo: app.py

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
    if not input_value.isdigit() or len(input_value) != length:
        return False
    if prefix and not input_value.startswith(prefix):
        return False
    return True

# Título de la app
st.title("Aplicación de Validación de Inputs")
st.write("Ingrese los valores para validar y guardar los datos.")

# Campos de entrada
input1 = st.text_input("Ingrese el primer valor (20 dígitos):")
input2 = st.text_input("Ingrese el segundo valor (40 dígitos):")
input3 = st.text_input("Texto adicional (opcional):")

# Validar entradas
if st.button("Validar y Guardar"):
    valid1 = validate_input(input1, 20, "003")
    valid2 = validate_input(input2, 40, "90")
    
    if valid1 and valid2:
        st.success("Todos los valores son válidos. Se guardarán en el archivo.")
        
        # Guardar en Excel
        file_name = "datos.xlsx"
        new_data = {
            "Input1": [input1],
            "Input2": [input2],
            "Input3": [input3],
        }
        df_new = pd.DataFrame(new_data)
        
        if os.path.exists(file_name):
            # Si el archivo existe, agregar los datos
            df_existing = pd.read_excel(file_name)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            df_combined.to_excel(file_name, index=False)
        else:
            # Crear un nuevo archivo
            df_new.to_excel(file_name, index=False)
        
        st.write("Datos guardados exitosamente en `datos.xlsx`.")
    else:
        st.error("Uno o más valores son inválidos. Revise los requisitos de los campos.")

# Mostrar datos guardados (opcional)
if os.path.exists("datos.xlsx"):
    st.write("Datos guardados actualmente:")
    st.dataframe(pd.read_excel("datos.xlsx"))
# archivo: app.py

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
    if not input_value.isdigit() or len(input_value) != length:
        return False
    if prefix and not input_value.startswith(prefix):
        return False
    return True

# Título de la app
st.title("Aplicación de Validación de Inputs")
st.write("Ingrese los valores para validar y guardar los datos.")

# Campos de entrada
input1 = st.text_input("Ingrese el primer valor (20 dígitos):")
input2 = st.text_input("Ingrese el segundo valor (40 dígitos):")
input3 = st.text_input("Texto adicional (opcional):")

# Validar entradas
if st.button("Validar y Guardar"):
    valid1 = validate_input(input1, 20, "003")
    valid2 = validate_input(input2, 40, "90")
    
    if valid1 and valid2:
        st.success("Todos los valores son válidos. Se guardarán en el archivo.")
        
        # Guardar en Excel
        file_name = "datos.xlsx"
        new_data = {
            "Input1": [input1],
            "Input2": [input2],
            "Input3": [input3],
        }
        df_new = pd.DataFrame(new_data)
        
        if os.path.exists(file_name):
            # Si el archivo existe, agregar los datos
            df_existing = pd.read_excel(file_name)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            df_combined.to_excel(file_name, index=False)
        else:
            # Crear un nuevo archivo
            df_new.to_excel(file_name, index=False)
        
        st.write("Datos guardados exitosamente en `datos.xlsx`.")
    else:
        st.error("Uno o más valores son inválidos. Revise los requisitos de los campos.")

# Mostrar datos guardados (opcional)
if os.path.exists("datos.xlsx"):
    st.write("Datos guardados actualmente:")
    st.dataframe(pd.read_excel("datos.xlsx"))
