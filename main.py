import requests
import send_email
topic = 'tesla'

# Define API key and url of info from NewsAPI along with different parameters of API
api_key = "48f8f6d6299f4890a1a651935f6ae891"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2022-12-10&" \
      "sortBy=publishedAt&" \
      "apiKey=48f8f6d6299f4890a1a651935f6ae891&" \
      "language=en"

# Make request
request = requests.get(url)

# Convert Request data into readable python dictionary
content = request.json()

# Assign variables to store the Topic number and the full text of the email
n = 0
full_email = ''

# Get a dictionary with data
for article in content['articles'][:20]:
    n = n + 1
    text = str(n) + '.' + str(article['title']) + '\n' \
           + str(article['description']) + '\n' \
           + str(article['url'])+ 2 * '\n'
    full_email = full_email + text + '\n'

# Send the email using ssl and smptlib
send_email.send_mail(("Subject: Today's news" + '\n' + full_email).encode("utf-8"))
