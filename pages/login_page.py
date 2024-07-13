from locators.login_page_locator import LoginPageLocator


class Login_Page:
    def __init__(self, browser):
        self.browser = browser

    def login_username(self, username):
        self.browser.find_element_by_xpath(LoginPageLocator.EMAIL).send_keys(username)


    def login_password(self, password):
        return self.browser.find_element_by_xpath(LoginPageLocator.PASSWORD).send_keys(password)

    @property
    def submit_login(self):
        self.browser.find_element_by_xpath(LoginPageLocator.SUBMIT).click()
