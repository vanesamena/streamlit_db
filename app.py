import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv')
frase = f"{data['nombre'][0]} su solicitud {data['solicitud'][0]} sera analizada"
# Define la interfaz de usuario con Streamlit
def main():

    st.title("Prueba de uso de Streamlit")

    st.write('Seleccione uno o varios generos')
    options = ['Terror', 'Drama', 'Aventura', 'Romantica']
    selected_options = st.multiselect('Selecciona las opciones:', options, max_selections=3)

    options = ['Opción 1', 'Opción 2', 'Opción 3']
    selected_option = st.selectbox('Selecciona una opción:', options)

    texto_usuario = st.text_input("Texto agregado por el ususario")

    if st.button("Enviar"):
        st.write(f'Opciones Seleccionadas: {selected_options}')
        st.write(f'Opcion: {selected_option}')
        st.write(f'Ingreso del ususario: {texto_usuario}')
        st.write('Se decto el siguiente dataframe en la base de datos:')
        st.dataframe(data)
        st.write(f'Frase generada: {frase}')

if __name__ == "__main__":
    main()

