import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image



css_file = "style.css"
cv_file = "Images/cv Estevão portugues 2025 - 1°Semestre (1).pdf"
cv_portuguese = "Images/cv Estevão portugues 2025 - 1°Semestre.pdf"

profile_photo = "Images/foto cv atual.png"
PAGE_TITLE = "Data Engineer"
PAGE_ICON = ":wave:"
NAME = "Estevão Lins Maia"
PROFILE = "Data Scientist"
AGE = 20
DESCRIPTION = "*Passionate Data Engineer with expertise in building and optimizing data solutions. Currently working as a Data Engineer at Stefanini Latam, one of Brazil’s leading company's, where I develop automation, data pipelines, and analytics to drive strategic decision-making. Pursuing a degree in Software Engineering, I am constantly refining my skills in data engineering, software development, and machine learning. Committed to leveraging technology to solve complex problems and enhance data as a service"
EMAIL = "estevaolins94@gmail.com"
SOCIAL_MEDIA = { "🐈‍⬛ github": "https://github.com/ttstive",
"🌎 linkedin":"https://www.linkedin.com/in/estevaolins/",
"✉️ contact me": "estevaolins94@gmail.com"}


projects = {
    "project5": "Pipeline automation for E-commerce", "link5": " ", "image5": "Images/airflow_project.jpeg",
    "project1": "Big Companies Tech analysis", "link": "https://github.com/ttstive/linguagens-utilizadas-repositorios-algumas-empresas", "image": "Images/languages companies .png",
    "project2": "Car crashes Analysis Worldwide", "link2": "https://github.com/ttstive/Vehicules-Crash-Analysis", "image2": "Images/data_crash.png",
    "project3": "Flappy Bird with AI", "link3": "https://github.com/ttstive/jogo_flappybird", "image3": "Images/flappy-bird.jpg",
    "project4": "Playlist Recommendation with Spotify API", "link4": "https://github.com/ttstive/Sistema_recomendador_de_musicas", "image4": "Images/spotify theme.png",
    "project6": "Little Cat Groceries", "link6": "https://app.powerbi.com/groups/me/reports/3e3a8d44-bd85-4571-899f-f3a95af3796f/ReportSection?experience=power-bi", "image6": "Images/Captura de tela de 2024-08-05 21-21-11.png"}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
with open(cv_file, "rb") as pdf_file:
    pdf_Byte = pdf_file.read()
    profile_photo = Image.open(profile_photo)
with open(cv_portuguese, "rb") as pdf_file:
    pdf_Byte2 = pdf_file.read()






st.markdown('<a id="hero"></a>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_photo, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=pdf_Byte,
        file_name=cv_file,
        mime="application/octet-stream",
    )
    st.download_button(
        label="📄 Download Resume Portuguese",
        data= pdf_Byte2,
        file_name=cv_portuguese,
        mime="application/octet-stream",
    )
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

# Experience & Qualifications section
st.markdown('<a id="experience"></a>', unsafe_allow_html=True)
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 3 Years experience extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python, SQL, Spark and Databricks
- ✔️ Good understanding of statistical principles and their applications, such as hypothesis testing, regression analysis, etc.
- ✔️ Excellent team-player and displaying a strong sense of initiative on tasks, always looking for new challenges and opportunities to test my capabilities
"""
)# Hard Skills and Soft Skills Lists
hard_skills = ["Python", "SQL", "React", "Java", "PowerBI", "Grafana"]
soft_skills = ["Teamwork", "Problem Solving", "Communication", "Analytical Thinking", "Adaptability"]

# Define values for hard skills (emphasize Python and SQL)
hard_values = [40, 30, 20, 20, 14, 8]  # Python and SQL have larger values

# Define values for soft skills (equal distribution for simplicity)
soft_values = [20, 20, 20, 20, 20]  # Equal distribution


@st.cache_data

def create_pie_chart(skills, values, title):
    """Creates a Pie Chart for skill distribution without percentages."""
    fig, ax = plt.subplots(figsize=(8, 5))  # Medium size (5x5 inches)
    ax.pie(values, labels=skills, startangle=140, colors=plt.cm.Paired.colors, wedgeprops={'edgecolor': 'black'})
    ax.set_title(title, fontsize=18, fontweight="bold")
    return fig

# Streamlit App
st.title("🚀 My Skills Overview")
st.write("### Hard Skills & Soft Skills")

# Create two columns for side-by-side layout
col1, col2 = st.columns(2)

# Plot Hard Skills Pie Chart in the first column
with col1:
    fig1 = create_pie_chart(hard_skills, hard_values, "Hard Skills")
    st.pyplot(fig1)

# Plot Soft Skills Pie Chart in the second column
with col2:
    fig2 = create_pie_chart(soft_skills, soft_values, "Soft Skills")
    st.pyplot(fig2)

# Work History section
st.markdown('<a id="work-history"></a>', unsafe_allow_html=True)
st.subheader("Work History")
st.write("---")

# Job 1
col0, col01 = st.columns(2)
with col0:
    st.image("Images/stefanini logo.png", width=269)

with col01:
    st.write("🧙‍♂️", "**Mid Level Data Engineer| Up Estágios**")
    st.write("03/2023 - 10/2023")
    st.write(
        """
   ► Specialized in developing data-driven automation using observability platforms like Grafana and building efficient data pipelines with Apache Airflow. Experienced in designing and optimizing ETL/ELT processes for seamless data flow orchestration, incorporating artificial intelligence.

Implemented real-time monitoring solutions by integrating InfluxDB for industrial automation. Managed the automation backlog, enhancing weekly deliveries and optimizing process efficiency.

Skilled in maintaining and evolving ETL systems, conducting metric analysis, and providing strategic insights for critical decision-making. Additionally, developed data projects for photovoltaic power plants, focusing on monitoring and analyzing solar energy generation.

 """
    )
# Job 2
st.write('\n')
col02, col03 = st.columns(2)
with col02:
    st.image("Images/sicooblogo.jpg", width=269)

with col03:
    st.write("🔍", "** Data Analyst | Sicoob**")
    st.write("10/2023 - Present")
    st.write(
        """
    - ► The biggest credit cooperative in Brazil, elected fourth times, with over 4 million members and 3,000 branches.
    - ► Extract and process data from the company's management system using SQL, Power BI, and Python.
    - ► Automate complex data structures.
    - ► Develop, test, and implement automations, create detailed documentation, and provide specialized training.
    - ► Perform comparative analysis of budget management frameworks, offering valuable insights for strategic decision-making.
    """
    )

    # Job 2
st.write('\n')
col03, col04 = st.columns(2)
with col03:
    st.image("Images/upestagio-logo.png", width=269)

with col04:
    st.write("🧙‍♂️", "**Intern Web Developer | Up Estágios**")
    st.write("03/2023 - 10/2023")
    st.write(
        """
   ► UP Estágios: Contributed to a startup connecting students with companies by developing and maintaining systems, spreadsheets, and websites. Specialized in data analysis and processing with Python (Numpy, Seaborn, Pandas, Matplotlib).

   ► Automation: Created user-friendly interfaces using HTML5, CSS, JavaScript, and Bootstrap on Google Apps Script. Excelled in developing automation solutions with Python and Google Apps Script.

   ► Streaming Data Visualization: Built an ETL pipeline to address data organization issues, enabling daily monitoring of students, companies, and contracts using Google Apps Script.
    """
    )
st.write('\n')

st.write('\n')

# Projects Section
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.subheader("Projects")
st.write("---")

# Projects
st.write('\n') # col33 its project that I didnt do or finished yet
col3, col4 = st.columns(2)


with col3:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.write("🔍", f"[{projects['project1']}]({projects['link']})")
    st.image(projects["image"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.write("🔍", f"[{projects['project2']}]({projects['link2']})")
    st.image(projects["image2"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)

st.write('\n')

col5, col6 = st.columns(2)

with col5:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.write("🔍", f"[{projects['project3']}]({projects['link3']})")
    st.image(projects["image3"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.write("🔍", f"[{projects['project4']}]({projects['link4']})")
    st.image(projects["image4"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)

st.write('\n')

col7, col8 = st.columns(2)


with col7:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.write("🔍", f"[{projects['project6']}]({projects['link6']})")
    st.image(projects["image6"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)

with col8:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.write("🔍", f"[{projects['project5']}]({projects['link5']})")
    st.image(projects["image5"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)

