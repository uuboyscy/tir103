import time
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1080,720")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor="https://standalone-chrome-30300274673.asia-east1.run.app/wd/hub",
    options=chrome_options,
)
# driver = Chrome()

url = "https://www.ptt.cc/bbs/index.html"

driver.get(url)
time.sleep(10)

driver.find_element(by=By.CLASS_NAME, value="board-name").click()
time.sleep(10)

driver.find_element(by=By.CLASS_NAME, value="btn-big").click()
time.sleep(10)

cookie = driver.get_cookies()
time.sleep(10)

driver.quit()

ss = requests.session()

# Extract cookies
for c in cookie:
    ss.cookies.set(c["name"], c["value"])

res = ss.get("https://www.ptt.cc/bbs/Gossiping/index.html")
soup = BeautifulSoup(res.text, "html.parser")
print(soup.prettify())