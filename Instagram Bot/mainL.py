from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

SIMILAR_ACCOUNT = 'therock'
USERNAME = os.environ['username']
PASSWORD = os.environ['password']


class InstaFollower():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)


    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        time.sleep(5)

        username_login = self.driver.find_element(By.NAME, value='username')
        password_login = self.driver.find_element(By.NAME, value='password')
        login = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')

        username_login.send_keys(USERNAME)
        password_login.send_keys(PASSWORD)

        login.click()

        time.sleep(5)

        # A save info prompt pops up
        info_not_now_button = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if info_not_now_button:
            info_not_now_button.click()

        time.sleep(2)

        # A notification prompt pops up
        noti_not_now_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if noti_not_now_button:
            noti_not_now_button.click()
    def find_followers(self):
        # finding the selected account
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}')

        time.sleep(3)

        # You can find the followers button on the profile page using the find_element_by_xpath() method and an XPath
        # selector. The WebDriverWait class is used to wait until the element is present on the page. Then click on the
        # followers' button using the click() method.
        followers_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//a[@href="/{SIMILAR_ACCOUNT}/followers/"]'))
        )
        followers_button.click()

        time.sleep(3)
        modal_xpath = "/html/body/div[6]/div[2]/div/div/div[1]/div/div["
        "2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]"
        modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, modal_xpath))
        )

        # Waiting for the Followers Popup to Load: We use WebDriverWait to wait until the followers popup is present on
        # the page. Then locate the followers popup using the find_element_by_xpath() method and an XPath selector.

        # Scroll down the followers popup
        scroll_script = "arguments[0].scrollTop = arguments[0].scrollHeight;"
        last_count = 0
        while True:
            self.driver.execute_script(scroll_script, modal)
            time.sleep(1)  # Add a delay to allow time for the followers to load
            new_count = len(self.driver.find_elements(By.XPATH, value='//div[@class="isgrP"]//li'))
            if new_count == last_count:
                break  # Exit the loop if no new followers are loaded
            last_count = new_count
    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]'
                                                                    '/div/div/div/div/div[2]/div/div/div[2]/div[2]/div'
                                                                    '/div[1]/div/div/div/div[3]/div/button')
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[8]/div[1]/div/div[2]/div/div'
                                                                         '/div/div/div/div/button[2]')
                cancel_button.click()




bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
