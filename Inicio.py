import streamlit as st
from utils import agregar_estilo_css
from rembg import remove
from PIL import Image

# Page configs (tab title, favicon) - Debe ser el primer comando de Streamlit
st.set_page_config(
    page_title="Remove Background Image",
    page_icon="🖼️",
)

# Función principal de la aplicación
def home():
    agregar_estilo_css()  # Aplica los estilos CSS

    # Título de la aplicación
    st.title("Eliminador de Fondos de Imagen")

    # Subir la imagen
    uploaded_image = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Cargar la imagen usando PIL
        image = Image.open(uploaded_image)
        st.image(image, caption="Imagen original", use_column_width=True)

        # Botón para remover el fondo
        if st.button("Eliminar Fondo"):
            # Procesar la imagen para eliminar el fondo
            output_image = remove(image)

            # Mostrar la imagen sin fondo
            st.image(output_image, caption="Imagen sin fondo", use_column_width=True)

            # Opción para descargar la imagen sin fondo
            st.download_button(
                "Descargar imagen sin fondo",
                data=output_image.tobytes(),
                file_name="imagen_sin_fondo.png",
                mime="image/png"
            )

if __name__ == "__main__":
    home()
