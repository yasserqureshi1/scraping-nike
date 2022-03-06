# Parsing HTML

# Importing necessary libraries
import requests                 # pip install requests
from bs4 import BeautifulSoup   # pip install bs4

# Make GET request to site
url = 'https://www.nike.com/gb/w?q=jordan&vst=jordan'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# Find all product elements
products = soup.find_all('div', {'class': 'product-card__body'})

# Loop through product elements and print name
for product in products:
    print(product.find('a', {'class': 'product-card__link-overlay'}).text)