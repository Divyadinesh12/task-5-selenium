"""
login the page and fetch title ,current url of the webpage and extract the entire contents of the webpage and save it in a text file whose name is  webpage_task_11.txt
"""

from selenium import webdriver
from selenium .webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
class LoginAutomation :
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def boot(self) :
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)
    def sleep(self, seconds):
        sleep(seconds)
        """
        this method hold on the screen
        :param seconds
        :return None
        """
    def userName_check(self, key):
        self.driver.find_element(by=By.ID, value="user-name").send_keys(key)
        self.sleep(5)
        """
        this method send keys to username inputField
        :param key
        :return None
        """
    def passWord_check(self,key):
        """
                this method send keys to password inputfield
                :param key
                :return None
        """
        self.driver.find_element(by=By.ID, value="password").send_keys(key)
        self.sleep(5)
    def submit_button(self):
        """
                this method will check whether submit button is clickable or not
        """
        self.driver.find_element(by=By.ID, value="login-button").click()
        self.sleep(5)

    def title(self):
        """
        this method show the title of the webpage
        :return:title
        """
        print("title of the webpage:",self.driver.title)
    def current_url(self):
        """
        this method show the current url of the webpage
        :return:current url
        """
        print("current url:", self.driver.current_url)
    def extract_entirecontents(self):
        page_contents = self .driver.page_source
        with open(r"C:\Users\dines\PycharmProjects\selenium introduction\webpage_task_11.txt", "w",
                  encoding="utf-8") as file:
            file.write(page_contents)
    def quit(self):
        self.driver.quit()
    def login_fetch_title_currenturl(self):
        self.boot()
        self.userName_check(self.username)
        self.passWord_check(self.password)
        self.submit_button()
        self.title()
        self.current_url()
        self.extract_entirecontents()


url = "https://www.saucedemo.com/"
obj = LoginAutomation(url,"standard_user","secret_sauce" )
obj.login_fetch_title_currenturl()