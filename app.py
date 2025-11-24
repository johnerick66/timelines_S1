import streamlit as st
st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
st.title("Modelos de pronóstico de la volatilidad del tipo de cambio")
st.write("Autor: John Erick Argandoña Acosta| BCP")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes de modelos de cambio.")
# URLs de imágenes en GitHub
base_url = "https://raw.githubusercontent.com/johnerick66/timelines_s1/main/timeline_images/"
imagenes = {
   1: base_url + "image1.jpg",
   2: base_url + "image2.jpg",
   3: base_url + "image3.jpg",
   4: base_url + "image4.jpg",
   5: base_url + "image5.jpg"
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
 st.info("1986: Primeros modelos neuronales logran predecir el USD/GBP mejor que métodos estadísticos.")
if opcion == 2:
 st.info("2005: Bancos adoptan SVM y ML para mejorar pronósticos del USD/EUR en alta volatilidad.")
if opcion == 3:
 st.info("2014: Surgen modelos LSTM que mejoran la predicción intradía del USD/JPY.")
if opcion == 4:
 st.info("2019: Modelos híbridos IA-macroeconomía fortalecen forecasting de pares como EUR/USD.")
if opcion == 5:
 st.info("2023: Transformers generativos integran noticias y datos de mercado para anticipar shocks cambiarios.")
