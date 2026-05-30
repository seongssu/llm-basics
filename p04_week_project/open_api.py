from dotenv import load_dotenv
import os
from openai import OpenAI

def get_client():
    load_dotenv("api_key.env")
    return OpenAI(api_key= os.getenv("api_key"))