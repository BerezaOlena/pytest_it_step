import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://casenik.com.ua/"

@pytest.fixture(scope="class")  #scope="class" відкриває один раз браузер
# @pytest.fixture
def browser():
    print("\nstart browser for test suite..")
    browser = webdriver.Chrome()
    yield browser
    #цей код виконається після завершення всього тесту
    print("\nquit browser..")
    browser.quit()

'''АВТОВИКОРИСТАННЯ ФІКСТУР'''
@pytest.fixture(autouse=True)
def prepare_data():
    print("print this str for every test")

class TestPage1():
    #икликаємо фікстуру в тексті, передавши її як параметр
    def test_is_button_search(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class = 'header_search_button trans_300']")

    def test_is_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href = 'cart/show']")

# #pytest -s -v test_fixtures3_12102023.py

@pytest.fixture(scope="class")
def prepare_faces():
    print(")", "\n")
    yield
    print(":3", "\n")

@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")

@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-P", "\n")

class TestPrintSmilingFaces():
    def test_first(self, prepare_faces, very_important_fixture):
        assert 1
    def test_second(self, prepare_faces):
        assert 2