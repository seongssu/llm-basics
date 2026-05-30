from dotenv import load_dotenv
import os
from openai import OpenAI
from pathlib import Path
def get_client():
    env_path = Path(__file__).parent / "api_key.env"
    load_dotenv(env_path)
    return OpenAI(api_key= os.getenv("api_key"))