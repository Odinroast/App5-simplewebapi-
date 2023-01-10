import requests
import smtplib

# Define API key and url of info from NewsAPI
api_key = "48f8f6d6299f4890a1a651935f6ae891"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2022-12-10&sortBy=publishedAt&" \
      "apiKey=48f8f6d6299f4890a1a651935f6ae891"

# Make request
request = requests.get(url)

# Convert Request data into readable python dictionary
content = request.json()

# Get a dictionary with data
for article in content['articles']:
      print(article['title'])