import time
import datetime
import random
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


ch_options=Options()
ch_options.add_argument("--user-data-dir=chrome-data")
chrome=webdriver.Chrome(options=ch_options,executable_path="/Users/LENOVO/Desktop/chromedriver.exe")
ch_options.add_argument("user-data-dir=chrome-data")
chrome.get("https://www.mobile.ir/users/account/login.aspx")
chrome.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/div[3]/input").send_keys("aradsystem_store@yahoo.com")
chrome.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/div[4]/input").send_keys("mykhanevade1991")
chrome.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/div[5]/input").click()
time.sleep(30)

for i in range(900):
    for j in range(1,5):
        try:
            chrome.get(f"https://www.mobile.ir/users/directoryrecords/productmanager.aspx?shopid=9233&sterms=&sbrandid=0&swarrantyid=0&page={j}")
            chrome.find_element_by_name("selected_items").click()
            chrome.find_element_by_name("renew").click()
            time.sleep(10)
        except:
            chrome.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/div[3]/input").send_keys(
                "aradsystem_store@yahoo.com")
            chrome.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/div[4]/input").send_keys(
                "mykhanevade1991")
            chrome.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/div[5]/input").click()
            time.sleep(10)
            chrome.get(f"https://www.mobile.ir/users/directoryrecords/productmanager.aspx?shopid=9233&sterms=&sbrandid=0&swarrantyid=0&page={j}")
            chrome.find_element_by_name("selected_items").click()
            chrome.find_element_by_name("renew").click()
            time.sleep(10)
    print(datetime.datetime.now())
    time.sleep(random.randint(900,1500))

