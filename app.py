from dotenv import load_dotenv
load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gemini_response(input,pdf_content,prompt):
    model=genai.GenerationModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def pdf_input(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())
        first_page=images[0]

#       converting to bytes..
        image_byte_arr=io.BytesIO()
        first_page.save(image_byte_arr,format="JPEG")
        image_byte_arr=image_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(image_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
st.set_page_config(page_title="Resume Tracker")
st.header("Resume Tracker")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader(" Please Upload your resume(PDF)...",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1=st.button("Tell me about the resume")
submit2=st.button("How to improve my skills")
submit3 = st.button("Percentage match")
submit4 = st.button("Make this resume a perfect resume for intern")

input_prompt1="""
    As a seasoned Technical Recruiter, your objective is to assess the resume
    provided in relation to the job description. Please provide a detailed 
    analysis of the candidate's qualifications and experience, highlighting
    areas of alignment with the role's requirements. Identify both the
    strengths and potential gaps in the candidate's profile.

    """
input_prompt2="""
   Create a list of real-world projects or tasks where I can practice and 
   refine my [specific skill]. Suggest ways to integrate these into my daily
    routine.Design a weekly schedule that balances my current 
    responsibilities with dedicated time for improving [specific skill]. 
    Ensure it's realistic and sustainable.

    """
input_prompt3="""
    You are an skilled ATS (Applicant Tracking System) scanner with a deep 
    understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description.
 give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then 
keywords missing and last final thoughts.

    """
input_prompt4="""
    Revise the objective or summary statement to clearly reflect my 
    enthusiasm for the internship role and highlight the key skills and 
    experiences that make me a strong candidate.
    Rewrite the project descriptions to clearly articulate the outcomes, 
    technologies used, and your specific contributions. Ensure each project 
    is relevant to the internship role
    """

if submit1:
    if uploaded_file is not None:
        pdf_content=pdf_input(uploaded_file)
        response=gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please uplaod the resume first")

elif submit2:
    if uploaded_file is not None:
        pdf_content=pdf_input(uploaded_file)
        response=gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please uplaod the resume first")

elif submit3:
    if uploaded_file is not None:
        pdf_content=pdf_input(uploaded_file)
        response=gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please uplaod the resume first")

elif submit4:
    if uploaded_file is not None:
        pdf_content=pdf_input(uploaded_file)
        response=gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please uplaod the resume first")