import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    WRONG_LOGIN = os.getenv("WRONG_LOGIN")
    WRONG_PASSWORD = os.getenv("WRONG_PASSWORD")
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")