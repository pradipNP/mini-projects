import requests

url = "https://zenquotes.io/api/random"
data = requests.get(url).json()

print("Quote:", data[0]['q'])
print("Author:", data[0]['a'])