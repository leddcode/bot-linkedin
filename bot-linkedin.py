from time import sleep

from selenium import webdriver

username = ''
password = ''

class LinkedinBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://www.linkedin.com/')

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//input[@name="session_key"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//input[@name="session_password"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[2]/button')
        login_btn.click()
        
        sleep(3)
        

    def connect(self):
        keep_connecting = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div/ul/li[1]/section/footer/button')
        keep_connecting.click()

        # choose a number of new connections to make
        for i in range(1, 150):
            sleep(0.5)
            xpath = f'/html/body/div[4]/div/div/div[2]/div/ul/li[{i}]/div/div[2]/button'
            try:
                    popup_1 = self.driver.find_element_by_xpath(xpath)
                    popup_1.click()
            except Exception as e:
                    print(e)
            sleep(1)


bot = LinkedinBot()
bot.login()
bot.connect()
