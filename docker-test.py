from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

chrome.get('https://gizmodo.com/')
print(chrome.title)  # Get suite title


def tear_down(self):  # Method close all active browser window and end script work
    self.driver.quit()
