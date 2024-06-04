from bs4 import BeautifulSoup
import requests

# Requests web page and parses into soup
target_page = requests.get("https://quotes.toscrape.com/")   
soup = BeautifulSoup(target_page.text, "html.parser")
