import streamlit as st
st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
st.title("Modelo de Predicción LSTM para Abastecimiento Periódico | Timeline")
st.write("Autor: Marcelo Martin Herrera Yoplack| BCP")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la evolución del modelo LSTM.")
# URLs de imágenes en GitHub
base_url = "https://raw.githubusercontent.com/Marcelo-cell/timelines_s1/main/timeline_images/"
imagenes = {
   1: base_url + "timeline1.png",
   2: base_url + "timeline2.png",
   3: base_url + "timeline3.png",
   4: base_url + "timeline4.png",
   5: base_url + "timeline5.png"
}
# Slider
opcion = st.slider(
 "Selecciona un punto del timeline",
 min_value=1,
 max_value=5,
 value=1,
 step=1
)
# Mostrar imagen según slider
st.image(imagenes[opcion], use_container_width=True)
if opcion == 1:
 st.info("1997 - Invención del Modelo LSTM")
if opcion == 2:
 st.info("2010 – Deeplearning era")
if opcion == 3:
 st.info("2015 - Crecimiento de Bigdata y Hardware")
if opcion == 4:
 st.info("2017 - Consolidación de Deeplearning")
if opcion == 5:
 st.info("2018 - Optimización del Abastecimiento Periódico")
