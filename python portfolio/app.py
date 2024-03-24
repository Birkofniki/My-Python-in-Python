from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir= Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file= current_dir/"styles"/"main.css"
resume_file= current_dir/"assets"/"Augastine Ndeti A.pdf"
profile_pic= current_dir/"assets"/"profile-pic.png"


# ---GENERAL SETTINGS ---
PAGE_TITLE= "Digital CV|Augastine Ndeti"
PAGE_ICON= ":wave:"
NAME= "Augastine Ndeti"
DESCRIPTION= """
Seniour Data analyst and Python Programming Expert, assisting organizations by supporting data-driven decision-making processes.
"""
EMAIL= "augastinendeti@gmail.com"
SOCIAL_MEDIA= {
    "YouTube":"https://www.youtube.com/channel/UCy9pdLZpUDSzcXrBT6rd0mg",
    "LinkedIn":"https://www.linkedin.com/in/augastine-ndeti-290230175?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BwZ6ut2hySHGJYPyJsjdf2A%3D%3D",
    "Twitter":"https://twitter.com/AugastineNdeti",
    "Facebook":"https://www.facebook.com/augastine.ndeti.3",
    "Instagram":"https://www.instagram.com/ndetiaugastino/",
    "Github":"https://github.com/Birkofniki",
    "Discord":"https://discordapp.com/users/961452033288843284",
    "Tiktok":"https://www.tiktok.com/@mr.bytes10?is_from_webapp=1&sender_device=pc",
    "F6s":"https://www.f6s.com/member/augastine-ndeti?follow=1",
    
}
PROJECTS= {
    "my portfolio":"https://augastine-s-portfolio.vercel.app/",
    "E-commerce website":"https://www.bigcommerce.com/articles/ecommerce/best-ecommerce-website-design/",
    "Resume in python":"https://www.google.com/search?q=resume+in+python+code&oq=resume+in+py&gs_lcrp=EgZjaHJvbWUqBwgCEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCAgHEAAYFhgeMgoICBAAGA8YFhgeMggICRAAGBYYHtIBCTEzNDQzajBqNKgCALACAA&sourceid=chrome&ie=UTF-8",
    "":"",
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)
# ---loading the CSS, Pdf & Profile Pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file,"rb") as pdf_file:
        PDFbyte=pdf_file.read()
        profile_pic=Image.open(profile_pic)    

# ---Hero Section Creation --- 
col1,col2= st.columns(2,gap="small") 
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)   
    # ---Social Links ---
st.write("#")
st.subheader("My Social Media Handles:")
cols= st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    # ---Experience & Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
        """
- Business Development Manager at Ngeni LABs, Kenya; 🚀May 2023 ➡ January 2024
    - ✔Optimized internal lead generation process by 20%, resulting in a 15% increase in sales conversions.
    - ✔Developed and implemented a new customer onboarding process, reducing onboarding time by 30%.
    - ✔Analyzed customer data to identify trends and opportunities for process improvement.
    - ✔Collaborated with cross-functional teams to streamline internal workflows and communication.

- Freelance Writer (CourseHero, WriterPro.com, & Writerbay) 🚀November 2021 ➡ April 2023 
    - ✔Conducted research and analysis on various topics related to Python programming and web development.
    - ✔Developed detailed process flows and documentation for complex business operations.
    - ✔Communicated effectively with clients to understand their needs and deliver high-quality work on time.
    - ✔Managed multiple projects simultaneously while meeting deadlines and ensuring accuracy.

- I.T. Support Officer-Intern (Makueni County Government, Wote, Kenya)	🚀May 2021 ➡ Oct 2021
    - ✔Provided technical support for County computers, networks, and software.
    - ✔Optimized network infrastructure by identifying and resolving network bottlenecks, leading to a 10% improvement in network performance.
    - ✔Conducted regular process audits and identified opportunities for streamlining IT operations.
    - ✔Configured IFMIS (Integrated Financial Management Information System) network ports.

        """
        )
    # ---My Skills ---
st.write("#")
st.subheader("SKILLS & AREAS OF EXPERTISE")
st.write(
        """
- Technical Skills:
    - ▶Proficient in HTML, CSS, and JavaScript
    - ▶Familiar with jQuery and WordPress
    - ▶Experience with Python Programming (scikit-learn, Pandas), SQL, VBA.
    - ▶Knowledge of tools like GitHub, CMD, Slack, and HelpNinja
    - ▶Comfortable with Databases like; Postgress, MongoDB, MySQL.
    - ▶Data Visualization: PowerBi, MS Excel, and Plotly.

- Non-technical Skills:
    - ▶Excellent written and verbal communication skills
    - ▶Strong problem-solving and troubleshooting abilities
    - ▶Empathetic and patient with customers
    - ▶Detail-oriented and well-organized
    - ▶Ability to work independently and as part of a team. 

        """
    )


# --- Work History ---
st.write("#")
st.subheader("My Work History")
st.write("---")

# --- Job 1 explained down here
st.write("🥇🥈🥉🏅","**Business Development Manager (Ngeni LABs, Kenya)**" )
st.write("May 2023-February 2024")
st.write(
    """				
- 📢Optimized internal lead generation process by 20%, resulting in a 15% increase in sales conversions.
- 📢Developed and implemented a new customer onboarding process, reducing onboarding time by 30%.
- 📢Analyzed customer data to identify trends and opportunities for process improvement.
- 📢Collaborated with cross-functional teams to streamline internal workflows and communication.

    """
    )
# --- Job 2 explained down here
st.write("🥇🥈🥉🏅","**Freelance Writer (CourseHero, WriterPro.com, & Writerbay)**" )
st.write("November 2021 - April 2023")
st.write(
    """					
- 📢Conducted research and analysis on various topics related to Python programming and web development.
- 📢Developed detailed process flows and documentation for complex business operations.
- 📢Communicated effectively with clients to understand their needs and deliver high-quality work on time.
- 📢Managed multiple projects simultaneously while meeting deadlines and ensuring accuracy.

    """
    )
# --- Job 3 explained down here
st.write("🥇🥈🥉🏅","**I.T. Support Officer-Intern (Makueni County Government, Wote, Kenya)**" )
st.write("May 2021 - Oct 2021")
st.write(
    """					
- 📢Provided technical support for County computers, networks, and software.
- 📢Optimized network infrastructure by identifying and resolving network bottlenecks, leading to a 10% improvement in network performance.
- 📢Conducted regular process audits and identified opportunities for streamlining IT operations.
- 📢Configured IFMIS (Integrated Financial Management Information System) network ports.

    """
    )

# --- Projects and Accomplishments ---
st.write("#")
st.subheader("Projetcs and Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    























    
    
        