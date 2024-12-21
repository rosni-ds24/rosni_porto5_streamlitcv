
import pathlib
import streamlit as st
import pandas as pd
from PIL import Image



st.title("Curriculum Vitae")

current_dir = pathlib.Path(__file__).parent if __file__ in locals() else pathlib.Path.cwd()
css_file = current_dir /"styles" / "main.css"
resume_file = current_dir / "asset" / "cv.pdf"
profil_file = current_dir /"asset" / "fotoprofil.png"

# ---GENERAL SETTING ---
PAGE_TITLE = "Curriculum Vitae | Wa Ode Rosni Yanti"
PAGE_ICON = "random"
NAME = " Wa Ode Rosni Yanti"
DESCRIPTION = """
Senior Epidemiologyst, Heath Data Analyst

"""
EMAIL = "rosniyantiwaode@gmail.com"
PROFFERIONAL_SUMMARY = "kdjdahhdhakhakhfakf"
EDUCATION = {
    "MAGISTER OF HEALTH",
    "BACHELOR OF PUBLIC HEALH MINORING IN FIED EPIDEMILOGY",
}
WORK_HISTORY = {
    "hdakdahda",
    "nsdahdaldhalda",
}

ORGANIZATIONAL_EXPERIENCE = {
    "SENIOR PROJECT MANAGER",
    "SENIOR EPIDEMIOLOGYST"
}
CERTIFICATION = {
    "Data Analyst",
    "Fundamental Epidemiology",
    "Data Science",
}

SOCIAL_MEDIA = {
    "Youtube" : "https://www.youtube.com/",
    "LinkedIn" : "https://www.linkedin.com/in/rosni-yanti-93307290/",
    "Github" : "https://www.github.com/",
}

#--- LOAD CSS, PROFIL PICTURE & CV.PDF ----

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profil_file)


# --- HERO SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
         label= " Download Resume",
         data=PDFbyte,
         file_name=resume_file.name,
         mime="application/octet-stream",
    )
st.write("  ", EMAIL)

#-- Professional Summary
st.write("#")
st.subheader("Professional Summary")
st.write("""
Experienced Senior Health Project Manager and Senior Epidemiologist with a proven track record in managing public health programs,
          particularly in the prevention and control of non-communicable diseases, 
         disease surveillance, and pandemic response. Skilled in designing 
         and implementing data-driven health initiatives, coordinating multidisciplinary teams,
          and collaborating with stakeholders to achieve measurable outcomes. 
         Expertise includes leading COVID-19 mitigation efforts, conducting epidemiological analyses, and developing evidence-based policies to enhance healthcare systems. 
         Committed to improving population health through strategic planning, innovation, and sustainable program implementation.       
""")

# -- SOCIAL MEDIA LINKS ---

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --EDUCATION  ---

st.write("#")
st.subheader("Education")
st.write("""
- MAGISTER OF HEALTH
- BACHELOR OF PUBLIC HEALH MINORING IN FIED EPIDEMILOGY
         
""")
#--- ORGANIZATIONAL_EXPERIENCE---
st.write("#")
st.subheader("Organizational Experience")
st.write("""
- SENIOR PROJECT MANAGER
- SENIOR EPIDEMIOLOGYST        
""")

# ---WORK_HISTORY ----
st.write("#")
st.subheader("Work History")
st.write("""
- Senior Health Project Manager | Riau Island Provincial Health Office: 2020 - present

	-	Led and managed public health projects focusing on the prevention and control of non-communicable diseases.
	-	Designed and implemented strategies for health promotion and disease prevention at the regional and national levels.
	-	Monitored project outcomes, ensuring alignment with health goals and stakeholder expectations.
    -  Coordinated with governmental and non-governmental organizations for program sustainability.

- Epidemiologist | Riau Island Provincial Health Office : 2015 - Present
	-	Conducted disease surveillance and epidemiological investigations, with a focus on outbreak control and prevention.
	-	Played a key role in the COVID-19 pandemic response, including data analysis, contact tracing, and public health interventions.
	-	Developed and delivered training programs for health professionals on disease surveillance systems and emergency preparedness.
	-	Analyzed health data to inform policy decisions and resource allocation.
 
""")

#--- CERTIFICATION ----
st.write("#")
st.subheader("Certification")
st.write("""
- Fullstack Data Analyst
- Fundamental Epidemiology
- Data Science     
""")

CERTIFICATION = {
    "Data Analyst",
    "Fundamental Epidemiology",
    "Data Science",
}
       
# -- EXPERIENCE  ---

st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- √ 7 year experience in analysing health data
- √ 7 year experience in mentoring
- √ strong hand on experience and klowledge in statistic, python and excel
- √ Excellent in managing team and displaying strong sense of problem solving
"""
)

# -- SKILL  ---

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- √ programming : sql, python (scikit-learn, Pandas, Numpy), VBA, R
- √ Data Visualization : Tableau, MS excel, Plotly, Seaborn
- √ Modelling : Logistic Regression, Linear Regression
- √ Databases : MYSQL, POSTGRESQL, SQLITE
"""
)

