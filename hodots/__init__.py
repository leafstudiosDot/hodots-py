import os
import requests
from dotenv import load_dotenv

__version__ = "0.0.1"

load_dotenv()

api_url = 'https://api.hodots.com'
HODOTS_SESSION_KEY = os.environ.get('HODOTS_SESSION_KEY', None)

class SessionKeyError(Exception):
    pass

if HODOTS_SESSION_KEY is None:
    raise SessionKeyError("HODOTS_SESSION_KEY is not set")

req = requests.Session()
req.params = {}
req.headers.update({'Authorization': f'Bearer {HODOTS_SESSION_KEY}'})

from .post import Post