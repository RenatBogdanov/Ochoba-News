import requests
from bs4 import BeautifulSoup
import time
import os

clear = lambda: os.system('cls')

#print(soup)
#print(quotes, "\n")
#print(requests.get(url).status_code)

def _request(url):
 
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	quotes = soup.find_all('div', class_='content-title content-title--short l-island-a')

	n = 1
	for quote in quotes:

		print(str(n)+".", quote.text.replace("Статьи редакции", '').strip(' \n\t'))
		#time.sleep(3)
		n += 1
	n = 1


def help():
	print('help')
	print('dtf')
	print('vc')
	print('exit')

def greetings():
	print('Добро пожаловать в Ochoba News. Пожалуйста, введите команду (для полного списка команд введите "help").')

def main():
	greetings()

	while True:
		
		_input = str(input())
		
		if _input == "dtf":
			clear()
			print("Информация с сайта dtf.ru:\n")
			_request('https://dtf.ru/')

		elif _input == "vc":
			clear()
			print("Информация с сайта vc.ru:\n")
			_request('https://vc.ru/')

		elif _input == "exit":
			break

		elif _input == "help":
			clear()
			help()

		else: 
			clear()
			print('Неизвестная команда, введите "help", чтобы увидеть список команд')

main()


#print("-----------\nE N D")
