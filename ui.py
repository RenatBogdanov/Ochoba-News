from kivy.app import App
from kivy.uix.label import Label
import requests
from bs4 import BeautifulSoup
import time
import os
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
 
green = '#06D6A0'
yellow = '#FFD166'


def _request(url):
 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='content-title content-title--short l-island-a')

    n = 1
    for quote in quotes:

        #a = Label(str(n)+".", quote.text.replace("Статьи редакции", '').strip(' \n\t'))
        #layout.add_widget(a)
        print(str(n)+".", quote.text.replace("Статьи редакции", '').strip(' \n\t'))

        n += 1
    n = 1


class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
     
        btn1 = Button(text="Button 1", background_color=green)
        layout.add_widget(btn1)

        btn2 = Button(text="Button 2", background_color=yellow)
        layout.add_widget(btn2)

        l = Label(text='Something')
        layout.add_widget(l)

        _request('https://dtf.ru/')

        return layout



if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()