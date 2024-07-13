import time
import datetime
import random
from selenium.common.exceptions import NoSuchElementException
import load_info
from pages.login_page import Login_Page
from pages.mobiles_page import MobilesPage
from locators.login_page_locator import LoginPageLocator
from locators.mobiles_page_locator import MobilesPageLocator
from wdpath import wdpath



def login():
    """this is login form"""
    chrome.get(LoginPageLocator.URL)


    a = Login_Page(chrome)
    if chrome.current_url == LoginPageLocator.URL or f"{LoginPageLocator.URL}/":
        try:
            a.login_username(load_info.info["username"])
            a.login_password(load_info.info["password"])
            a.submit_login
            time.sleep(5)
        except NoSuchElementException:
            print("you already in! or user/pass is wrong!")

def update():

    b = MobilesPage(chrome)
    for i in range(900):
        for j in range(1, 7):
            try:
                chrome.get(f"{MobilesPageLocator.URL}{j}")
                b.check_all
                b.submit
                time.sleep(10)
            except NoSuchElementException:
                a = Login_Page(chrome)
                a.login_username(load_info.info["username"])
                a.login_password(load_info.info["password"])
                a.submit_login
                time.sleep(5)
                chrome.get(
                    f"{MobilesPageLocator.URL}{j}")
                chrome.find_element_by_name("selected_items").click()
                chrome.find_element_by_name("renew").click()
                time.sleep(5)
            except:
                update()
        print(f"last update: {datetime.datetime.now()}")
        time.sleep(random.randint(600, 1200))

"""this is the path of chrome driver"""
chrome=wdpath()

def menu():
    user_input = input(
        "1.login to mobile.ir\n2.update all pages\n3.auto login and update\nenter one of the options above: ")

    while user_input!="exit":
        if user_input=="1":
            login()

        elif user_input=="2":
            update()
        elif user_input=="3":
            login()
            update()
        user_input = input(
            "1.Login to mobile.ir\n2.Update all pages\n3.Auto login and update\nEnter one of the options above: ")

menu()