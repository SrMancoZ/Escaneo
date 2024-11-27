import streamlit as st
import pandas as pd
import os

# Configurar colores de la interfaz
st.set_page_config(page_title="Validación de Inputs", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9; /* Fondo blanco claro */
        color: #333333; /* Texto gris oscuro */
    }
    .stTextInput {
        border: 1px solid #cccccc;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #0073e6;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #005bb5;
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
st.title("Escaneo de pallets 📋")

st.subheader("📥 Ingrese los valores")
st.write("Ingrese los datos en los campos a continuación y asegúrese de que cumplen con los formatos requeridos.")

# Campos de entrada
input1 = st.text_input("Ingrese el primer valor (20 dígitos):")
input2 = st.text_input("Ingrese el segundo valor (40 dígitos):")
input3 = st.text_input("Texto adicional (opcional):")

# Validar y guardar
if st.button("✅ Validar y Guardar"):
    with st.spinner("Procesando..."):
        valid1, error1 = validate_input(input1, 20, "003")
        valid2, error2 = validate_input(input2, 40, "90")

        if not valid1:
            st.error(f"Error en Input 1: {error1}")
        elif not valid2:
            st.error(f"Error en Input 2: {error2}")
        else:
            sscc, material, cantidad, lote = process_inputs(input1, input2)
            
            # Verificar si ya existe el archivo
            file_name = "datos.xlsx"
            if os.path.exists(file_name):
                # Leer el archivo existente
                df_existing = pd.read_excel(file_name, dtype=str)
                # Verificar si el SSCC ya está registrado
                if sscc in df_existing["SSCC"].values:
                    st.error(f"El SSCC '{sscc}' ya está registrado. No se guardará nuevamente.")
                else:
                    # Guardar nuevo registro
                    new_data = {
                        "SSCC": [sscc],
                        "Material": [material],
                        "Cantidad por pallet": [cantidad],
                        "Lote": [lote],
                        "Texto Adicional": [input3],
                    }
                    df_new = pd.DataFrame(new_data, dtype=str)
                    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
                    df_combined.to_excel(file_name, index=False, engine='openpyxl')
                    st.success("Datos guardados exitosamente.")
                    st.write(df_new)
            else:
                # Crear un nuevo archivo si no existe
                new_data = {
                    "SSCC": [sscc],
                    "Material": [material],
                    "Cantidad por pallet": [cantidad],
                    "Lote": [lote],
                    "Texto Adicional": [input3],
                }
                df_new = pd.DataFrame(new_data, dtype=str)
                df_new.to_excel(file_name, index=False, engine='openpyxl')
                st.success("Datos guardados exitosamente.")
                st.write(df_new)

# Mostrar datos guardados con opción de descarga
if os.path.exists("datos.xlsx"):
    st.subheader("📊 Datos Guardados Actualmente")
    df_saved = pd.read_excel("datos.xlsx", dtype=str)
    st.dataframe(df_saved)
    with open("datos.xlsx", "rb") as file:
        st.download_button(
            label="📥 Descargar datos",
            data=file,
            file_name="datos_guardados.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Botón para borrar datos existentes
if st.button("🗑️ Borrar Datos Previos"):
    if os.path.exists("datos.xlsx"):
        os.remove("datos.xlsx")
        st.success("Datos anteriores eliminados.")
    else:
        st.warning("No hay datos previos para borrar.")



