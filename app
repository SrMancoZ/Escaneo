import streamlit as st

# Función para validar si la entrada contiene solo dígitos y tiene la longitud especificada
def validate_input(input_value, length):
    return input_value.isdigit() and len(input_value) == length

# Aplicación de Streamlit
st.title("Aplicación de Validación de Inputs")

# Campos de entrada
input1 = st.text_input("Ingrese el primer valor (20 dígitos):")
input2 = st.text_input("Ingrese el segundo valor (40 dígitos):")

# Validar entradas
if st.button("Validar"):
    if validate_input(input1, 20) and validate_input(input2, 40):
        st.success("Ambos valores son válidos.")
    else:
        st.error("Uno o ambos valores no son válidos. Asegúrese de que el primer valor tenga 20 dígitos y el segundo valor tenga 40 dígitos.")
