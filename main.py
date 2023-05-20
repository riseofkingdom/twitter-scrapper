from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import clipboard


PATH = "C:\\Users\\DevOps\\Documents\\Project Cuan\\Reza Tanjung Thesis\\Scrapper\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.set_window_size(1024, 600)
driver.maximize_window()

driver.get("https://twitter.com/login")
time.sleep(10)

username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("jigongfiraun")
next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()

time.sleep(5)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("Cl100299")
log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
time.sleep(8)
# search_box = driver.find_element(
#     By.XPATH, "//input[@data-testid='SearchBox_Search_Input']"
# )
# search_box.send_keys("bankBCA \uD83D\uDE01")
# search_box.send_keys(Keys.ENTER)


clipboard.copy("😃")
search_box = driver.find_element(
    By.XPATH, "//input[@data-testid='SearchBox_Search_Input']"
)
search_box.send_keys("bankBCA")
search_box.send_keys(Keys.CONTROL + "v")


search_box.send_keys(Keys.ENTER)

time.sleep(3)
# people = driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
# people.click()

# time.sleep(3)
# profile = driver.find_element(
#     By.XPATH,
#     "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span",
# )
# profile.click()

# time.sleep(3)


# articles = driver.find_element(By.XPATH, "//div[@data-testid='tweetText']")
# articles.click()
# UserTag = driver.find_element(By.XPATH, "//div[@data-testid='User-Name']").text
# TimeStamp = driver.find_element(By.XPATH, "//time").get_attribute("datetime")
time.sleep(3)
Tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweetText']").text
element = driver.find_element(By.XPATH, "//*[@id='id__2pd458tnk6l']/img")
title = element.get_atribute("title")
# print(UserTag)
print(Tweet)
# print(Emoji)
print(title)

# Reply = driver.find_element(By.XPATH, "//div[@data-testid='reply']").text


# print(Reply)

# Tweets = []
# Replys = []
# articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
# while True:
#     for article in articles:
#         Tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweetText']").text
#         Tweets.append(Tweet)
#         print(Tweet)
#         driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#         time.sleep(3)

#     articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
#     Tweets2 = list(set(Tweets))
#     if len(Tweets2) > 5:
#         break

# import pandas as pd
#     private String createdBy;
#     private ZonedDateTime createdAt;
#     private String updatedBy;
#     private ZonedDateTime updatedAt;
# df = pd.DataFrame(zip(Tweets), columns=["Tweets"])

# df.head()

# df.to_excel(r"D:\Learnerea\Tables\tweets_live.xlsx", index=False)

# import os

# os.system('start "excel" "D:\Learnerea\Tables\\tweets_live.xlsx"')


# print(len(Tweets))
# UserTags = []
# TimeStamps = []
