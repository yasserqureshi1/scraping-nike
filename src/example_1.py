# Using the NIKE Search API 

# Importing necessary libraries
import requests         # pip install requests
import json

# Make GET request to site
count = 60
anchor = 0
country = 'GB'
country_language = 'en-GB'
query = 'jordan'
url = f'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=241B0FAA1AC3D3CB734EA4B24C8C910D&country={country}&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace({country})%26filter%3Dlanguage({country_language})%26filter%3DemployeePrice(true)%26searchTerms%3D{query}%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D{count}&language={country_language}&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D'

html = requests.get(url=url)
output = json.loads(html.text)

# Loop through products and print name
for item in output['data']['products']['products']:
    print(item['title'], item['subtitle'])