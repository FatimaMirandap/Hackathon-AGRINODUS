import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import streamlit.components.v1 as components

# Define the logo and banner
logo = Image.open("images/logo.jpg")  # Change this to your logo URL
banner = Image.open("images/agri.jpg")  # Change this to your banner URL

# Insert the banner and logo
st.image(banner, use_column_width=True)
st.image(logo, width=500)

# Custom CSS for background and style
st.markdown("""
    <style>
        /* Custom Background */
        body {
            background-image: url("/mnt/data/image.png");  /* Replace with background image */
            background-size: cover;
        }

        /* Adjust Page Width */
        .main .block-container {
            max-width: 90%; /* Increase width */
            padding: 1rem 2rem; /* Adjust padding */
        }

        /* Customize Titles and Texts */
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

        /* Style for SMS Messages */
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

# Project Title
st.markdown("<h1 class='title'>Agrinodus: The Technology Program for Farmers</h1>", unsafe_allow_html=True)

# Program Description
st.markdown("<h2 class='header'>At Datacomets, we propose the planning of a program and three technological tools for farmers worldwide to learn how to use them for their benefit and everyone else’s, using data provided by NASA.</h2>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>-</p>
""", unsafe_allow_html=True)

# Program Phases
st.markdown("<h2 class='header'>Program Phases</h2>", unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>1. Awareness</h3>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>Establish an awareness campaign; communicate with ministries, authorities, and local offices, depending on the country and its regulations. Programs and informational resources include websites, posters, and diagrams.</p>
""", unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>2. Selection</h3>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>Analyze population data and select candidates based on their technological preferences.</p>
""", unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>3. Training</h3>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>Establish local section leaders, provide training for section leaders and groups according to the selected technology.</p>
""", unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>4. Technology Implementation</h3>", unsafe_allow_html=True)
st.markdown("""
<p class='text'>Technology 1: SMS Broadcasting.<br>
Technology 2: Text-to-speech by radio. This technology will provide daily alerts regarding weather, water, and possible pests based on NASA predictions. The alerts will be broadcasted in various languages, such as Maya in Mérida.</p>
""", unsafe_allow_html=True)

# Data Analysis Section with Charts
st.markdown("<h2 class='header'>Data Analysis</h2>", unsafe_allow_html=True)
st.markdown("<p class='text'>Here are some data obtained from NASA, presented in charts.</p>", unsafe_allow_html=True)

Dashboard = Image.open("images/DashboardP.png")  # Change this to your logo URL
st.image(Dashboard, use_column_width=True)

# Dummy data for display (you can connect real NASA data)
data = pd.DataFrame({
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Temperature (°C)': [28, 30, 27, 29, 31],
    'Humidity (%)': [65, 70, 60, 68, 72]
})

# Create Temperature Chart
fig, ax = plt.subplots(figsize=(5, 3))  # Adjust chart size
ax.plot(data['Day'], data['Temperature (°C)'], marker='o', color='b')
ax.set_title("Weekly Temperature")
ax.set_xlabel("Day")
ax.set_ylabel("Temperature (°C)")
st.pyplot(fig)

# Create Humidity Chart
fig2, ax2 = plt.subplots(figsize=(5, 3))  # Adjust chart size
ax2.plot(data['Day'], data['Humidity (%)'], marker='o', color='g')
ax2.set_title("Weekly Humidity")
ax2.set_xlabel("Day")
ax2.set_ylabel("Humidity (%)")
st.pyplot(fig2)

# Announcements Block with Examples
st.markdown("<h2 class='header'>Announcements</h2>", unsafe_allow_html=True)
st.markdown("<p class='text'>These are examples of messages to be sent according to the area.</p>", unsafe_allow_html=True)

# Example Announcement Message
st.info("Rain expected today. Temperature: 27°C. Don’t forget to protect your crops. Alert: Favorable conditions for pests. Stay alert. More information here: [Meteomatics](https://meteomatics.com)")

# Radio Section for Announcements
st.markdown("<h2 class='header'>Radio Section</h2>", unsafe_allow_html=True)
st.markdown("<p class='text'>Here you can listen to the announcements that will be broadcasted.</p>", unsafe_allow_html=True)

# HTML Embed for Radio
radio_embed_html = """
<div class="cstrEmbed" data-type="newStreamPlayer" data-publicToken="5f66bb41-7a1c-4c20-a5eb-fe023e0af99d" data-theme="light" data-color="6C2BDD" data-channelId="" data-rendered="false">
<a href="https://www.caster.fm">Shoutcast Hosting</a> <a href="https://www.caster.fm">Stream Hosting</a> <a href="https://www.caster.fm">Radio Server Hosting</a></div>
<script src="//cdn.cloud.caster.fm//widgets/embed.js"></script>
"""

# Display the embed in the Streamlit app
components.html(radio_embed_html, height=300)

# Footer
st.markdown("<p class='footer'>© 2024 - Hackathon Demo | Technology Program for Farmers</p>", unsafe_allow_html=True)
