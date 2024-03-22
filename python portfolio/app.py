from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir=Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file=current_dir/"styles"/"main.css"
resume_file=current_dir/"assets"/"Augastine Ndeti A.pdf"
profile_pic=current_dir/"assets"/"yellow bg profile-pic (3).png"


# ---GENERAL SETTINGS ---
PAGE_TITLE="Digital CV|Augastine Ndeti"
PAGE_ICON=":wave:"
NAME="Augastine Ndeti"
DESCRIPTION="""
Seniour Data analyst and Python Programming Expert, assisting organizations by supporting data-driven decision-making processes.
"""
EMAIL="augastinendeti@gmail.com"
SOCIAL_MEDIA={
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
PROJECTS={
    "my portfolio":"https://augastine-s-portfolio.vercel.app/",
    "E-commerce website":"https://www.bigcommerce.com/articles/ecommerce/best-ecommerce-website-design/",
    "Resume in python":"https://www.google.com/search?q=resume+in+python+code&oq=resume+in+py&gs_lcrp=EgZjaHJvbWUqBwgCEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yCAgHEAAYFhgeMgoICBAAGA8YFhgeMggICRAAGBYYHtIBCTEzNDQzajBqNKgCALACAA&sourceid=chrome&ie=UTF-8",
    "":"",
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)
st.title("Hello there!")