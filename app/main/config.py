import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

DATABASE_URI = os.getenv("DATABASE_URI")
FLASK_DEBUG = os.getenv("FLASK_DEBUG")
SECRET_KEY = os.getenv("SECRET_KEY")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

