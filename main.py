#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\geckodriver.exe"

service = webdriver.FirefoxService()
driver = webdriver.Firefox(service=service)

driver.get("https://quotes.toscrape.com/")

# Open and find text fields in login page
driver.find_element(By.LINK_TEXT, "Login").click()
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Input account info and login
username_field.send_keys("1234")
password_field.send_keys("1234")
driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

# Find all quotes and authors in the html
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

# Store all quotes and authors in a list
quote_arr = []
author_arr = []
for quote, author in zip(quotes, authors):
    quote_arr.append(quote.text)
    author_arr.append(author.text)

print(quote_arr)
print(author_arr)
