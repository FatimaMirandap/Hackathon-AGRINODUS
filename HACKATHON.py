import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components


# Definir el logo y el banner
logo = Image.open("images/logo.jpg")  # Cambia esto a la URL de tu logo
banner = Image.open("images/agri.jpg")  # Cambia esto a la URL de tu banner

# Insertar el banner y el logo
st.image(banner, use_column_width=True)
st.image(logo, width=500)

# CSS personalizado para fondo y estilo
st.markdown("""
    <style>
        /* Fondo personalizado */
        body {
            background-image: url("/mnt/data/image.png");  /* Reemplaza con la imagen del fondo */
            background-size: cover;
        }

        /* Ajustar la amplitud de la página */
        .main .block-container {
            max-width: 90%; /* Más amplitud */
            padding: 1rem 2rem; /* Ajuste de padding */
        }

        /* Personalizar los títulos y textos */
        .title {
            color: #4CAF50;
            font-family: 'Arial', sans-serif;
            font-size: 50px;
            font-weight: bold;
            text-align: center;
        }

        .header {
            color: #795548;
            font-family: 'Arial', sans-serif;
            font-size: 30px;
            font-weight: bold;
        }

        .text {
            color: #616161;
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            text-align: justify;
        }

        /* Estilo para los mensajes SMS */
        .sms {
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            font-weight: bold;
            color: #4CAF50;
            background-color: #F1F8E9;
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
        }

    </style>
""", unsafe_allow_html=True)


# Título del proyecto
st.markdown("<h1 class='title'>Agrinodus: El programa de Tecnología para Agricultores</h1>", unsafe_allow_html=True)

# Descripción del programa
st.markdown("<h2 class='header'>En Datacomets proponemos la planeación del programa y tres herramientas tecnológicas para que los agricultores a nivel global aprendan a utilizarlas en su beneficio y el de todos, con datos proporcionados por NASA.</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>-</p>
""", unsafe_allow_html=True)

# Fases del programa
st.markdown("<h2 class='header'>Fases del Programa</h2>", unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>1. Concientización</h3>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>Establecer una campaña de concientización; comunicación con secretarías, autoridades, comisarías, dependiendo del país y sus regulaciones. Programas y recursos informativos como página web, posters y diagramas.</p>
""", unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>2. Selección</h3>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>Análisis de datos de la población y selección de candidatos según preferencias tecnológicas.</p>
""", unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>3. Capacitación</h3>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>Establecer jefes de sección locales, capacitación de jefes de sección y de grupos según la tecnología seleccionada.</p>
""", unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>4. Implementación de Tecnología</h3>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>Tecnología 1: Broadcasting por SMS.<br>
Tecnología 2: Text-to-speech por radio. Esta tecnología dará avisos diarios respecto al clima, agua y posibles plagas, basados en predicciones de NASA. Los avisos se transmitirán en diferentes lenguajes, como el Maya en Mérida.</p>
""", unsafe_allow_html=True)

# Sección de análisis de datos con gráficas
st.markdown("<h2 class='header'>Análisis de Datos</h2>", unsafe_allow_html=True)
st.markdown("<p class='text'>Aquí se muestran algunos datos obtenidos de NASA, presentados en gráficos.</p>", unsafe_allow_html=True)

st.markdown("""
<iframe src="https://public.tableau.com/views/Predicciones07octubre/Dashboard1?:language=es-ES&:display_count=y&:origin=viz_share_link" 
width="100%" height="800px"></iframe>
""", unsafe_allow_html=True)

Dashboard = Image.open("images/DashboardP.png")  # Cambia esto a la URL de tu logo
st.image(Dashboard, width=500)

# Datos ficticios para mostrar el análisis (puedes conectar datos reales de NASA)
data = pd.DataFrame({
    'Día': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    'Temperatura (°C)': [28, 30, 27, 29, 31],
    'Humedad (%)': [65, 70, 60, 68, 72]
})

# Crear gráfico de temperatura
fig, ax = plt.subplots(figsize=(5, 3))  # Ajustar tamaño de la gráfica
ax.plot(data['Día'], data['Temperatura (°C)'], marker='o', color='b')
ax.set_title("Temperatura Semanal")
ax.set_xlabel("Día")
ax.set_ylabel("Temperatura (°C)")
st.pyplot(fig)

# Crear gráfico de humedad
fig2, ax2 = plt.subplots(figsize=(5, 3))  # Ajustar tamaño de la gráfica
ax2.plot(data['Día'], data['Humedad (%)'], marker='o', color='g')
ax2.set_title("Humedad Semanal")
ax2.set_xlabel("Día")
ax2.set_ylabel("Humedad (%)")
st.pyplot(fig2)

# Bloque de anuncios con ejemplos
st.markdown("<h2 class='header'>Anuncios</h2>", unsafe_allow_html=True)
st.markdown("<p class='text'>Estos son ejemplos de los mensajes que se enviarán según la zona.</p>", unsafe_allow_html=True)

# Ejemplo de mensaje de anuncio
st.info("Hoy se esperan lluvias. Temperatura: 27°C. No olvides proteger tus cultivos. Alerta: Condiciones favorables para plagas. Mantente alerta. Más información aquí: [Meteomatics](https://meteomatics.com)")

# Sección de radio con los anuncios
st.markdown("<h2 class='header'>Sección de la Radio</h2>", unsafe_allow_html=True)
st.markdown("<p class='text'>A continuación puedes escuchar los anuncios que serán transmitidos.</p>", unsafe_allow_html=True)

# HTML del embed de la radio
radio_embed_html = """
<div class="cstrEmbed" data-type="newStreamPlayer" data-publicToken="5f66bb41-7a1c-4c20-a5eb-fe023e0af99d" data-theme="light" data-color="6C2BDD" data-channelId="" data-rendered="false">
<a href="https://www.caster.fm">Shoutcast Hosting</a> <a href="https://www.caster.fm">Stream Hosting</a> <a href="https://www.caster.fm">Radio Server Hosting</a></div>
<script src="//cdn.cloud.caster.fm//widgets/embed.js"></script>
"""

# Mostrar el embed en la aplicación Streamlit
components.html(radio_embed_html, height=300)

# Footer
st.markdown("<p class='footer'>© 2024 - Hackathon Demo | Programa de Tecnología para Agricultores</p>", unsafe_allow_html=True)
