import requests
from bs4 import BeautifulSoup
import time
import os

clear = lambda: os.system('cls')

url = 'https://dtf.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='content-title content-title--short l-island-a')

#print(soup)
#print(quotes, "\n")
#print(requests.get(url).status_code)

def _quotes():
	n = 1
	for quote in quotes:

		print(str(n)+".", quote.text.replace("Статьи редакции", '').strip(' \n\t'))
		#time.sleep(3)
		n += 1
	n = 1

def help():
	print("help")
	print("update")
	print("exit")

def main():
	while True:
		
		_input = str(input())
		
		if _input == "update":
			clear()
			_quotes()
		elif _input == "exit":
			break
		elif _input == "help":
			clear()
			help()
		else: print('unknown command, print "help" for read list of commands')

main()


#print("-----------\nE N D")
