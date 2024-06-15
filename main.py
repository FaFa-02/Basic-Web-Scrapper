#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\geckodriver.exe"

service = webdriver.FirefoxService()
driver = webdriver.Firefox(service=service)

driver.get("https://quotes.toscrape.com/")

# Open Login page
author = driver.find_element(By.LINK_TEXT, "Login").click()

"""
browser_driver = Service()

# Requests web page and parses into soup
target_page = requests.get("https://quotes.toscrape.com/")   
soup = BeautifulSoup(target_page.text, "html.parser")

# Find all quotes and authors in the html
quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})

# Store all quotes and authors in a list
quote_arr = []
author_arr = []
for quote, author in zip(quotes, authors):
    quote_arr.append(quote.string)
    author_arr.append(author.string)

print(quote_arr)
print(author_arr)
"""