from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://casenik.com.ua/"

class TestPage1():

    @classmethod
    def setup_class(self): #буде вплавати на весь клас
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self): #буде вплавати на весь клас
        print("\nquit browser for test suite..")
        self.browser.quit()

    def test_is_button_search(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300']")

    def test_is_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//a[@href = 'cart/show']")

class TestPage2():

    def setup_class(self): #буде вплавати на весь клас
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    def teardown_class(self): #буде вплавати на весь клас
        print("\nquit browser for test suite..")
        self.browser.quit()

    def test_is_button_search(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//div[@class = 'top_bar_user']/a[@href='user/login']")

    def test_is_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, "//a[@href = 'cart/show']")

#pytest -s -v test_fixtures_12102023.py



