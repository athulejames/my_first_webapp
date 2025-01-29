import streamlit as st
import pandas as pd

# Set background color (light blue)
st.markdown("""
    <style>
        body {
            background-color: #ADD8E6;  # Light blue background
        }
        .reportview-container .main .block-container {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. Athule James"
field = "Environmental & Geographical Sciences"
institution = "University of Cape Town (UCT)"

# Allow user to upload a profile photo only once
if 'photo_uploaded' not in st.session_state:
    st.session_state.photo_uploaded = False  # Track if photo has been uploaded

if not st.session_state.photo_uploaded:
    uploaded_photo = st.file_uploader(" ", 
                                      type=["jpg", "jpeg", "png"])

    if uploaded_photo:
        st.session_state.photo_uploaded = True  # Mark photo as uploaded
        st.image(uploaded_photo, width=200)  # Display uploaded image
else:
    # If the photo has been uploaded, display it and hide the uploader
    uploaded_photo = st.file_uploader("/home/james/Pictures/spiderman.jpeg", type=["jpg", "jpeg", "png"])
    
    st.image(uploaded_photo, width=200)

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a more personal bio or introduction
bio = """
Dr. Athule James is a researcher specializing in climate modeling, with a particular focus on simulations 
of tropical cyclones in the Southwest Indian Ocean. His work aims to understand the dynamics of tropical 
storms in this region and their potential future impacts in the context of climate change. 
In addition to his work on tropical cyclones, Dr. James utilizes advanced hydrological and hydraulic models 
to study the broader climate impacts, including the influence of rainfall, river flow, and flooding on 
communities and ecosystems in the Southwest Indian Ocean.

His interdisciplinary approach combines meteorological modeling, climate science, and hydrology to provide 
insightful predictions that can inform disaster management and policy-making in regions vulnerable to extreme weather events.
"""
st.write(bio)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

    # Optionally add a search box with autocomplete (basic search)
    st.text_input("Search Publications by Title or Author", key="search", value="")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a citation metric (you can replace with actual data)
citations = 150  # Example number of citations
st.header("Research Impact")
st.write(f"**Citations:** {citations}")

# Add a contact section
st.header("Contact Information")
email = "jmsath001@myuct.ac.za"
linkedin_url = "https://www.linkedin.com/in/athule-james"  # Example
twitter_url = "https://twitter.com/athulejames"  # Example
st.write(f"You can reach {name} at {email}.")

# Add social media links
st.write("Follow on:")
st.markdown(f"- [LinkedIn]({linkedin_url})")
st.markdown(f"- [Twitter]({twitter_url})")

# Include a "Back to Top" button for easier navigation if the page becomes long
st.markdown("<a href='#'>Back to Top</a>", unsafe_allow_html=True)
