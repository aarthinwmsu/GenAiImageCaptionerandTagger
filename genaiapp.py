import streamlit as st
import os
from PIL import Image
import google.generativeai as genai  # Assuming 'generativeai' is the correct library

# Title and file uploader
st.title('GenAI Image Captioner and Tagger')
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

# API Key input
API_KEY = st.text_input("Enter your API Key (get it from [here](https://makersuite.google.com/app/apikey))")

# Processing the uploaded file
if uploaded_file is not None:
    if st.button('Upload'):
        if API_KEY.strip() == '':
            st.error('Enter a valid API key')
        else:
            # Saving uploaded file temporarily
            file_path = os.path.join("temp", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            
            # Opening the image
            img = Image.open(file_path)
            
            try:
                # Configuring and using generative AI model
                genai.configure(api_key=API_KEY)
                model = genai.GenerativeModel('gemini-pro-vision')
                
                # Generating caption
                caption = model.generate_content(["Write a caption for the image in english", img])
                st.image(img, caption=f"Caption: {caption.text}")
                
                # Generating tags
                tags = model.generate_content(["Generate 5 hash tags for the image in a line in english", img])
                st.write(f"Tags: {tags.text}")
                
            except Exception as e:
                error_msg = str(e)
                if "API_KEY_INVALID" in error_msg:
                    st.error("Invalid API Key. Please enter a valid API Key.")
                else:
                    st.error(f"Failed to configure API due to {error_msg}")

# Footer with attribution
footer = """
<style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        height: 10%;
        font-size: 15px;
        color: white;
        text-align: center;
        padding: 10px 0;
        background-color: #fefefe;
    }
    .footer a {
        color: white;
        text-decoration: none;
    }
    .footer a:hover {
        color: white;
    }
</style>

<div class="footer">
    <p><a href="https://www.linkedin.com/in/ai" target="_blank">GenAI Captivate</a></p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
