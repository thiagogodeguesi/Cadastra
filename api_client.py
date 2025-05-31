import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='config.env')

API_KEY = os.getenv("COINCAP_API_KEY")
LIMIT = os.getenv("LIMIT")

BASE_URL = 'https://rest.coincap.io/v3'

def fetch_cryptos(limit=LIMIT):
    endpoint = f'/assets?limit={limit}&apiKey={API_KEY}'
    url = BASE_URL + endpoint

    response = requests.get(url)
    response.raise_for_status()
    
    return response.json()['data']

def fetch_exchanges(limit=LIMIT):
    url = f"{BASE_URL}/exchanges?limit={limit}&apiKey={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['data']