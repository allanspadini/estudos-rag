import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY"),
)