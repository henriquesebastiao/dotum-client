from os import getenv
from load_dotenv import load_dotenv

load_dotenv()

BASE_URL = getenv('BASE_URL', default='http://localhost:8000')
