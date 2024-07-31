import streamlit as st
import pandas as pd 
import numpy as np
from pathlib import Path
from PIL import Image

css_file = "style.css"
cv_file = "Images/cv Estevão 2024 - 2°Semestre.pdf"

profile_photo = "Images/image_123650291.JPG"
PAGE_TITLE = "Data Science Resume"
PAGE_ICON = ":wave:"
NAME = "Estevão Lins Maia"
PROFILE = "Data Scientist"
AGE = 20
DESCRIPTION = " am a passionate data scientist with a fervor for innovation and problem-solving. Currently, I am honing my skills as a data analyst at Sicoob, one of Brazil's leading credit cooperatives. This role has been an incredible opportunity to grow and make a significant impact. As I pursue a degree in Software Engineering, I am continually seeking new challenges and opportunities to expand my expertise. My belief is that technology is a driving force in all areas of life, and I am deeply committed to advancing the fields of data science, data engineering, and software development."
EMAIL = "estevaolins94@gmail.com"
SOCIAL_MEDIA = { "🐈‍⬛ github": "https://github.com/ttstive",
"🌎 linkedin":"https://www.linkedin.com/in/estevaolins/"}


projects = {
    "project1": "Big Companies Tech analysis", "link": "https://github.com/ttstive/linguagens-utilizadas-repositorios-algumas-empresas", "image": "Images/languages companies .png",
    "project2": "Car crashes Analysis Worldwide", "link2": "https://github.com/ttstive/Vehicules-Crash-Analysis", "image2": "Images/data_crash.png",
    "project3": "Flappy Bird with AI", "link3": "https://github.com/ttstive/jogo_flappybird", "image3": "Images/flappy-bird.jpg",
    "project4": "Playlist Recommendation with Spotify API", "link4": "https://github.com/ttstive/Sistema_recomendador_de_musicas", "image4": "Images/spotify theme.png",
    "project5": "Population Pyramid", "link5": "https://estevaodata.000webhostapp.com/comparacao_piramides_etarias.html", "image5": "Images/pyramids analysis.png",
    "project6": "Statistics Fundamentals", "link6": "https://github.com/ttstive/analise_dados_temporais/tree/main", "image6": "Images/Statistics Fundamentals.png"}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
with open(cv_file, "rb") as pdf_file:
    pdf_Byte = pdf_file.read()
    profile_photo = Image.open(profile_photo)

# Hero section
st.markdown("""
<style>
.navbar {
    background-color: #000;
    padding: 10px;
    text-align: center;
}
.navbar a {
    margin: 0 15px;
    text-decoration: none;
    color: #e0e0e0;
    font-size: 16px;
}
.navbar a:hover {
    color: #b0b0b0;
}
</style>
<div class="navbar">
    <a href="#hero">Home</a>
    <a href="#experience">Experience & Qualifications</a>
    <a href="#hard-skills">Skills</a>
    <a href="#work-history">Work History</a>
    <a href="#projects">Projects</a>
</div>
""", unsafe_allow_html=True)

st.markdown('<a id="hero"></a>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_photo, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=pdf_Byte,
        file_name=cv_file,
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
- ✔️ 2 Years experience extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python, SQL, Power BI, and Excel
- ✔️ Good understanding of statistical principles and their applications, such as hypothesis testing, regression analysis, etc.
- ✔️ Excellent team-player and displaying a strong sense of initiative on tasks, always looking for new challenges and opportunities to test my capabilities
"""
)

# Hard Skills section
st.markdown('<a id="hard-skills"></a>', unsafe_allow_html=True)
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Spark, Pandas, Numpy, Flask, FastAPI, Apache), SQL, NoSQL, M and DAX
- 📊 Data Visualization: PowerBI, MS Excel, Plotly, Seaborn, Matplotlib, Power BI and Looker
- 📚 Modeling: Logistic regression, linear regression, decision trees, automation and transformation of data types
- 🗄️ Databases: SQLlite, MongoDB, MySQL
"""
)
st.write('\n')
st.subheader("Soft Skills")
st.write(
    """
- 🤝 Teamwork: I have experience working in teams, I am always looking for new challenges and opportunities to test my capabilities
- 📈 Problem Solving: I am always looking for new challenges and opportunities to test my capabilities
- 📝 Communication: I have experience in teaching and I am always looking for new challenges and opportunities to test my capabilities
- 📊 Analytical Thinking: I am always looking for new challenges and opportunities to test my capabilities
- 🚀 Adaptability in Fast-Paced Team Environments: I thrive in dynamic, high-tempo team settings where quick adaptation and decision-making are crucial
"""
)

# Work History section
st.markdown('<a id="work-history"></a>', unsafe_allow_html=True)
st.subheader("Work History")
st.write("---")

# Job 1
st.write('\n')
col0, col01 = st.columns(2)
with col0:
    st.image("Images/sicooblogo.jpg", width=269)

with col01:
    st.write("🔍", "**Junior Data Analyst | Sicoob**")
    st.write("10/2023 - Present")
    st.write(
        """
    - ► The biggest credit cooperative in Brazil, elected fourth times, with over 4 million members and 3,000 branches.
    - ► Extract and process data from the company's management system using SQL, Power BI, and Python.
    - ► Utilize libraries such as Pandas, Numpy, Matplotlib, and Spark to ensure data accuracy and expedite analysis.
    - ► Automate complex data structures with Python, Power Query, DAX, and M, while maintaining data organization.
    - ► Develop, test, and implement automations, create detailed documentation, and provide specialized training.
    - ► Perform comparative analysis of budget management frameworks, offering valuable insights for strategic decision-making.
    """
    )
st.write('\n')

# Job 2
st.write('\n')
col02, col03 = st.columns(2)
with col02:
    st.image("Images/upestagio-logo.png", width=269)

with col03:
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

# Job 3
st.write('\n')
col04, col05 = st.columns(2)
with col04:
    st.image("Images/alianca-americalogo.png", width=269)

with col05:
    st.write("🌍", "**English Language Teacher (Freelancer) | Aliança América**")
    st.write("2021 - 2023")
    st.write(
        """
    - ► Taught online English classes using the Scaffold Instruction methodology, enhancing students' listening, speaking, writing, and conversational skills.
    - ► Prepared detailed reports on students' progress, contributing to their language skill development.
    - ► Assisted students in preparing for job market success and international professional opportunities.
    """
    )

# Projects Section
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.subheader("Projects")
st.write("---")

# Projects
st.write('\n')
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
    st.write("🔍", f"[{projects['project5']}]({projects['link5']})")
    st.image(projects["image5"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)

with col8:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.write("🔍", f"[{projects['project6']}]({projects['link6']})")
    st.image(projects["image6"], width=300)
    st.markdown('</div>', unsafe_allow_html=True)
