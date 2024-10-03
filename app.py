import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Cambiamos el título a "dobuja kbro"
st.title("dobuja kbro")

with st.sidebar:
    st.subheader("Propiedades del Tablero")
    drawing_mode = st.sidebar.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = '#000000'

# Crear el componente del canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Color de relleno con algo de opacidad
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=300,
    width=500,
    drawing_mode=drawing_mode,
    key="canvas",
)
