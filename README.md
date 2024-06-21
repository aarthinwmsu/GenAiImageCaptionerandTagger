# GenAI Image Captioner and Tagger

## Implementation
**Clone**
`git clone <repo URL>`

**Installation:**
`pip install requirements.txt`

**Run the app**
`python -m streamlit run app.py`


## Tools and Technologies Planned for the Project

1. **Streamlit**: For building the web application interface.
2. **Python**: Programming language for backend logic and integration.
3. **PIL (Python Imaging Library)**: To handle image processing tasks.
4. **Google Generative AI (Gemini)**: Specifically for image captioning and tag extraction.
5. **GitHub**: Version control and repository hosting for collaborative development.
6. **HTML/CSS**: For customizing the frontend interface if needed.
7. **Deployment Platform (e.g., Heroku)**: For hosting the Streamlit app online.

## High-Level Architecture (Block Diagram)

<img width="254" alt="image" src="https://github.com/aarthinwmsu/GenAiImageCaptionerandTagger/assets/137325641/2316679d-bf7b-4171-86f7-d58b6015add9">


### Explanation of the Diagram

- **User Interface (Streamlit)**:
  - **Upload Image**: Users upload an image file through the Streamlit interface.
  - **Enter API Key**: Users input their Google Generative AI API key through a text input field.

- **Backend Logic (Python)**:
  - **File Handling**: Streamlit handles the uploaded file and stores it temporarily.
  - **Image Processing (PIL)**: The uploaded image is processed using PIL to prepare it for analysis.

- **Google Generative AI (Gemini)**:
  - **Configuration**: The application configures the Google Generative AI model using the provided API key.
  - **Caption and Tag Generation**: Requests are made to the Gemini model to generate captions and tags for the processed image.

- **Output Display (Streamlit)**:
  - **Generated Caption**: The application displays the generated caption alongside the uploaded image.
  - **Generated Tags**: The application shows the generated tags (hashtags) related to the image.

- **Error Handling**:
  - **Invalid API Key**: If the API key provided is invalid, appropriate error messages are displayed to the user.
  - **Other Errors**: General exceptions and errors during image processing or API interaction are handled and displayed.

## Comprehensive Explanation of Implementation Steps

1. **Setup Environment and Dependencies**:
   - Install Python (3.10 or above), Streamlit, PIL, and other necessary libraries specified in `requirements.txt`.

2. **Build the Streamlit Interface**:
   - Create a Streamlit app (`app.py`) with components for file upload (`file_uploader`), API key input (`text_input`), and buttons for triggering image analysis.

3. **Handling Image Uploads**:
   - Use Streamlit's `file_uploader` to allow users to upload images in supported formats (JPG, PNG, JPEG).
   - Store the uploaded image temporarily and prepare it for processing.

4. **Integration with Google Generative AI (Gemini)**:
   - Obtain an API key from Google's Makersuite.
   - Configure the Google Generative AI library (`google.generativeai`) with the API key.
   - Initialize the GenerativeModel (e.g., 'gemini-pro-vision') for image analysis.

5. **Image Processing and Analysis**:
   - Open the uploaded image using PIL for further processing.
   - Send requests to the GenerativeModel to generate captions and tags for the image.

6. **Display Results**:
   - Show the processed image alongside the generated caption and tags using Streamlit's `image` and `write` components.

7. **Error Handling**:
   - Validate the API key input to ensure it is not empty and is correctly formatted.
   - Handle exceptions such as invalid API keys or errors during image processing gracefully by displaying user-friendly error messages through `st.error`.

8. **Deployment**:
   - Optionally, deploy the Streamlit app to a platform like Heroku for online access.

9. **Testing and Refinement**:
   - Test the application thoroughly with various types of images and API key scenarios.
   - Refine the interface and error handling based on user feedback and testing results.

By following these steps and utilizing the outlined tools and technologies, developers can successfully implement the project for image captioning and tag extraction using Google's Generative AI service via a user-friendly Streamlit interface. This approach ensures that both technical functionalities and user experience considerations are addressed effectively.


**References:**

- Streamlit Documentation. Retrieved from [https://docs.streamlit.io/](https://docs.streamlit.io/)
- Python Imaging Library (PIL). Retrieved from [https://python-pillow.org/](https://python-pillow.org/)
- Google Generative AI Documentation. Retrieved from [https://cloud.google.com/gemini](https://cloud.google.com/gemini)
- Heroku Documentation. Retrieved from [https://devcenter.heroku.com/](https://devcenter.heroku.com/)
- GitHub Documentation. Retrieved from [https://docs.github.com/](https://docs.github.com/)

