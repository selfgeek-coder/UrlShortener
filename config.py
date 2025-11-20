from dotenv import load_dotenv
from os import getenv

load_dotenv()

db_url = getenv("DATABASE_URL")