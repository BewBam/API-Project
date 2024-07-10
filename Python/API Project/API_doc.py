import requests

# Replace 'API_KEY' with your actual API key from NewsAPI
API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"
response = requests.get(url)
print(response.status_code)