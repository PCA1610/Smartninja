from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen


url = "https://quotes.yourdictionary.com/theme/marriage/"

response = urlopen(url).read()

soup = BeautifulSoup(response)

quotes = soup.findAll('p', attrs={'class': 'quoteContent'})

for quote in quotes:
    print quote.text
