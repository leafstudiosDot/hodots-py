import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_url = 'http://localhost:5001'
HODOTS_SESSION_KEY = os.environ.get('HODOTS_SESSION_KEY', None)

class SessionKeyError(Exception):
    pass

if HODOTS_SESSION_KEY is None:
    raise SessionKeyError("HODOTS_SESSION_KEY is not set")

req = requests.Session()
req.params = {}
req.headers.update({'Authorization': f'Bearer {HODOTS_SESSION_KEY}'})

from .post import Post