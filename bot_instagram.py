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
browser = webdriver.Chrome(executable_path='./chromedriver')

browser.get('https://www.instagram.com/accounts/login/')
sleep(2)

# Login
user = browser.find_element(By.NAME, 'username')
user.send_keys(USER)
password = browser.find_element(By.NAME, 'password')
password.send_keys(PASSWORD)

btn_login = browser.find_element(By.CSS_SELECTOR, 'div._abak:nth-child(3)')
btn_login.click()

sleep(3)

btn_not_now_login = browser.find_element(
    By.CSS_SELECTOR, 'button._acan:nth-child(1)')
btn_not_now_login.click()

btn_not_now_notifications = browser.find_element(
    By.CSS_SELECTOR, 'button._a9--:nth-child(2)')
btn_not_now_notifications.click()

sleep(4)

# Inside
hastag_list = ['python', 'bot', 'rock']
novos_users_seguidos = []
acc = -1
seguindo = 0
likes = 0
comentarios = 0

for hastag in hastag_list:
    acc += 1
    browser.get('https://www.instagram.com/explore/tags/' +
                hastag_list[acc] + '/')
    sleep(4)
    primeira_thumb = browser.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
    primeira_thumb.click()
    sleep(randint(3, 4))
    try:
        for _ in range(1, 3):
            usuario = browser.find_element(
                By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a').text
            if usuario not in novos_users_seguidos:
                if browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').text == 'Follow':
                    browser.find_element(
                        By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').click()
                    novos_users_seguidos.append(usuario)
                    seguindo += 1

    except:
        continue
