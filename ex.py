from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/Users/LENOVO/Desktop/chromedriver.exe")
driver.get("https://pythonbasics.org")