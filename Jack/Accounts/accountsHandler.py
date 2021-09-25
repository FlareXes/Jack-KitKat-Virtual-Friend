import os
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Essentials.DataFilters import takecmd
from selenium.webdriver.chrome.options import Options
from Jack.jvoice import speak
#import os
#import wget


class Account:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        # chrome_options = Options()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.binary_location = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.chrome_driver_binary = r"D:/Program Files/chromedriver_win32/chromedriver.exe"

    def instagram(self):
        driver = webdriver.Chrome(self.chrome_driver_binary, options=self.options)
        driver.get('https://www.instagram.com/')
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]')))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
        not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

    def facebook(self):
        driver = webdriver.Chrome(self.chrome_driver_binary, options=self.options)
        driver.get('https://www.facebook.com/')
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="email"]')))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="pass"]')))
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        time.sleep(5)


    def discord(self):
            speak('You must need to specify password to access the server.')
            passwd = takecmd()
            if 'don\'t use weak master password' in passwd:
                discord = 'C:\\Users\\as808\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord'
                os.startfile(discord)
                speak('Access Granted!!! Proceeding further')
                speak('Discord Server Has Been Started')
            else:
                speak('Access Denied... Security feature has been enabled. From now we have start capturing your activities.')


