from bs4 import BeautifulSoup
import requests

# Requests web page and parses into soup
target_page = requests.get("https://quotes.toscrape.com/")   
soup = BeautifulSoup(target_page.text, "html.parser")

# Find all quotes and authors in the html
quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

# Store all quotes in a list
quote_arr = []
for quote in quotes:
    quote_arr.append(quote.string)

# Store all authors in a list
author_arr = []
for author in authors:
    author_arr.append(author.string)
