from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import load_info

path=load_info.info["path"]

ch_options=Options()
def wdpath():
    global chrome
    try:
        chrome = webdriver.Firefox(executable_path="geckodriver.exe")
    except:
        print("some error happend in chrome path driver contact 09380043744")
    return chrome