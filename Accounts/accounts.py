from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#import os
#import wget

class Account:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.options = webdriver.ChromeOptions()
        self.options.binary_location = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.chrome_driver_binary = r"D:/Program Files/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver_binary, options=self.options)

    def instagram(self):
        self.driver.get('https://www.instagram.com/')
        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]')))
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
        username.clear()
        password.clear()

        username.send_keys(self.username)
        password.send_keys(self.password)

        log_in = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        not_now = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
        not_now2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

    def facebook(self):
        self.driver.get('https://www.facebook.com/')

        username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="email"]')))
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="pass"]')))
        username.clear()
        password.clear()

        username.send_keys(self.username)
        password.send_keys(self.password)

        log_in = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

