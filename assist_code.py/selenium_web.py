from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_elements_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_elements_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()

assist=infow()
assist.get_info("neutron stars")
