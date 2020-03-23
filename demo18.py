from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=option)
browser.execute_script('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
browser.get('https://antispider1.scrape.cuiqingcai.com/')
