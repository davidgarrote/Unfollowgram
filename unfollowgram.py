from selenium import webdriver
from time import sleep
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

        """Loading Instagram Web"""

        print("Loading Instagram...")
        self.driver.get("https://instagram.com")
        sleep(2)

        """Accepting cookies"""

        print("Accepting cookies...")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        sleep(2)

        """Login"""

        print("Logging you in...")
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
        print("You have been logged in!")
        sleep(5)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not now')]").click()
            sleep(2)
        except:
            sleep(1)
        print("Successfully declined notifications...")


    """Defining the unfollow function"""
    
    def unfollow(self):
        unfollows = 0
        max_unfollows = 150
        while True:
            try:
                self.driver.get("https://www.instagram.com/YOUR_INSTAGRAM_HANDLE/")
                sleep(5)
                while self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a") is None:
                    self.driver.get("https://www.instagram.com/YOUR_INSTAGRAM_HANDLE/")
                    print("Successfully opened your profile")
                    sleep(5)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
                print("Successfully opened your following list")
                sleep(5)
            except:
                pass
            try:
                while True:
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()
                    sleep(3)
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                    unfollows +=1
                    print(f"You unfollowed {unfollows} accounts so far. Good job!")
                    sleep(10)
                    
                    if unfollows >= max_unfollows:
                        sys.exit(f"It seems that you unfollowed a total of {unfollows} accounts, so it's time to quit or you may get banned. See you soon!")
            except:
                pass
            if unfollows >= max_unfollows:
                sys.exit(f"It seems that you unfollowed a total of {unfollows} accounts, so it's time to quit or you may get banned. See you soon!")
            sleep(120)



"""Remember to edit this section and the rest on capital letters"""

my_bot = Instabot('YOUR_USERNAME', 'YOUR_PASSWORD')
while True:
    my_bot.unfollow()
