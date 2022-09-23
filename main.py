import requests
from bs4 import BeautifulSoup
import time


url = 'https://dtf.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='content-title content-title--short l-island-a')

#print(quotes, "\n")
#print(requests.get(url).status_code)

for quote in quotes:

	print(quote.text.replace("Статьи редакции", '').strip(' \n\t'))
	#time.sleep(3)

#print("-----------\nE N D")
