import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DBNAME")
URI = os.getenv("URI")