import requests

url = "https://zenquotes.io/api/random"

# requesting url for randon quote
response = requests.request("GET", url)
# Store response as a json
result = response.json()[0]

quote = result['q']  # Quote of the day
author = result['a']  # Auther of the quote

# Print quote and auther name
print(f"Quote: {quote} \nAuther: {author}")


