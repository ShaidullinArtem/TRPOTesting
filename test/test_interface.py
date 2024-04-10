import time
from selenium.webdriver.common.by import By
from browser import Browser


class TestInterface:
    def __init__(self, url: str):
        self.url = url
        self.browser = Browser().__call__()

    def header_test(self, header_class: str) -> None | str:
        try:
            self.browser.get(self.url)
            header_element = self.browser.find_element(By.CLASS_NAME, header_class)
            return header_element.text
        except Exception as e:
            print(e)
            return None
        finally:
            self.browser.close()
            self.browser.quit()

    def is_visible_test(self, element_class: str) -> bool:
        try:
            self.browser.get(self.url)
            element = self.browser.find_element(By.CLASS_NAME, element_class)
            return element.is_displayed()
        except Exception as e:
            print(e)
            return False
        finally:
            self.browser.close()
            self.browser.quit()

    def nav_to_link_test(self, link: str) -> None:
        try:
            self.browser.get(link)
        except Exception as e:
            print(e)
        finally:
            self.browser.close()
            self.browser.quit()

    def enter_input_test(self, input_id: str, text: str) -> None:
        try:
            self.browser.get(self.url)
            time.sleep(5)
            input_element = self.browser.find_element(By.ID, input_id)
            input_element.clear()
            input_element.send_keys(text)
            self.browser.execute_script("arguments[0].scrollIntoView();", input_element)
            time.sleep(5)
        except Exception as e:
            print(e)
        finally:
            self.browser.close()
            self.browser.quit()

    def click_test(self, element_class: str) -> None:
        try:
            self.browser.get(self.url)
            element = self.browser.find_element(By.CLASS_NAME, element_class)
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(5)
            element.click()
            time.sleep(5)
        except Exception as e:
            print(e)
        finally:
            self.browser.close()
            self.browser.quit()
