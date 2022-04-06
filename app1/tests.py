from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from bs4 import BeautifulSoup
import requests



source = requests.get('https://www.amazon.in/router/s?k={}').text()

soup = BeautifulSoup(source, 'lxml')
result = soup.find_all('div')
print(result)