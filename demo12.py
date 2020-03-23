from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://dynamic2.scrape.cuiqingcai.com/')
input = browser.find_element_by_class_name('logo-image')
print(input)