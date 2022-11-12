from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

config = dotenv_values(".env")
USER = config['USER']
PASSWORD = config['PASSWORD']

# Google Chrome 107.0.5304.110
chromedrive_path = './chromedriver'
browser = webdriver.Chrome(executable_path=chromedrive_path)

# Declarations
instagram_url = 'https://www.instagram.com/accounts/login/'

browser.get(instagram_url)
sleep(2)

# Login
user = browser.find_element(By.NAME, 'username')
user.send_keys(USER)

password = browser.find_element(By.NAME, 'password')
password.send_keys(PASSWORD)

btn_login = browser.find_element(By.CSS_SELECTOR, 'div._abak:nth-child(3)')
btn_login.click()

sleep(4)

btn_not_now_login = browser.find_element(
    By.CSS_SELECTOR, 'button._acan:nth-child(1)')
btn_not_now_login.click()

sleep(1)

btn_not_now_notifications = browser.find_element(
    By.CSS_SELECTOR, 'button._a9--:nth-child(2)')
btn_not_now_notifications.click()

sleep(1)

browser.get('https://www.instagram.com/rampazzoamanda/')

sleep(5)

browser.get('https://www.instagram.com/carlosferauche/')

sleep(5)

browser.get('https://www.instagram.com/ivelintk/')

sleep(100)
