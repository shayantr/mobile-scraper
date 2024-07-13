from locators.mobiles_page_locator import MobilesPageLocator
class MobilesPage:
    def __init__(self,browser):
        self.browser=browser
    @property
    def check_all(self):
        return self.browser.find_element_by_name(MobilesPageLocator.SELECTALL).click()
    @property
    def submit(self):
        return self.browser.find_element_by_name(MobilesPageLocator.RENEW).click()