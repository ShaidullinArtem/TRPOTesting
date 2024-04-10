from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


class Browser:
    def __init__(self):
        self.useragent = UserAgent()

        self.service = Service(executable_path="./chromedriver./chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-agent={self.useragent.random}')

    def __call__(self, *args, **kwargs) -> WebDriver:
        return webdriver.Chrome(service=self.service, options=self.options)
