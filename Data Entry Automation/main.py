from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


SHEET_LINK = 'https://forms.gle/TXiDhYkg9yDEbLKCA'
URL = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(URL)
response_text = response.text

soup = BeautifulSoup(response_text, 'html.parser')

addresses = soup.findAll('address')
prices = soup.findAll('span', class_="PropertyCardWrapper__StyledPriceLine")
property_links = soup.findAll('a', class_="property-card-link")

addresses_text = []
prices_text = []
links_text = []

for i in range(len(addresses)):
    ad = addresses[i].getText().strip('\n').strip().strip('|')
    addresses_text.append(ad)

    pr = prices[i].getText().split('+')[0]
    prices_text.append(pr)

    hr = property_links[i].get('href')
    links_text.append(hr)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(SHEET_LINK)

time.sleep(3)


for i in range(len(addresses)):
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div'
                                                        '/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]'
                                            '/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]'
                                           '/div/div[1]/input')

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_input.send_keys(addresses_text[i])
    price_input.send_keys(prices_text[i])
    link_input.send_keys(links_text[i])

    submit_button.click()

    time.sleep(2)

    submit_another_response_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response_button.click()

    time.sleep(2)
