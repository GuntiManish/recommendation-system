import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBQgyeiucpHP-MeGSejx3TVQ-Y2iGxXvA4")
  # or hardcode it directly here

def get_embedding(text):
    response = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    return response["embedding"]
