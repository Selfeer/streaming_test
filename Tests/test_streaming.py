from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service
from time import sleep

driver = webdriver.Chrome(service=Service('chromedriver.exe'))
driver.get("https://www.youtube.com/watch?v=MItluIsvfTo&ab_channel=AmazonWebServices")
options = webdriver.ChromeOptions()
options.add_argument("--use-file-for-fake-video-capture=C:\\Users\\selfe\\PycharmProjects\\streaming_test\\test_video"
                     ".m4v")
sleep(5)
# driver.find_element(By.ID, 'userEmail').send_keys("david_test@gmail.com")

driver.close()