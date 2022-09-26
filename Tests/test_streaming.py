from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-file-for-fake-video-capture=C:\\Users\\Selfeer\\PycharmProjects\\streaming_test"
                            "\\test_video.m4v")

driver = webdriver.Chrome(service=Service('chromedriver.exe'), chrome_options=chrome_options)

driver.get("https://webcamtests.com/")
wait = WebDriverWait(driver, 20)

start_streaming = wait.until(
        EC.presence_of_element_located((By.ID, "webcam-launcher"))
    ).click()

sleep(5)
# driver.find_element(By.ID, 'userEmail').send_keys("david_test@gmail.com")

driver.close()