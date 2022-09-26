from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from file_path import get_path
from Utils.options import set_chrome_options
from pyzbar.pyzbar import decode
from PIL import Image


def test_streaming():
    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=set_chrome_options())

    driver.get("https://www.onlinemictest.com/webcam-test/")
    wait = WebDriverWait(driver, 20)

    # Turn on the Webcam
    wait.until(
        EC.element_to_be_clickable((By.ID, "webcam-start"))
    ).click()

    sleep(3)

    # Save QR code from the Webcam as PNG
    element = driver.find_element(By.ID, "webcam-test")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.screenshot("qr.png")

    driver.close()

    # Get Text from the QR
    decocde_qr = decode(Image.open(get_path('qr.png')))
    decoded = decocde_qr[0].data.decode('ascii')

    assert decoded == "DevOps Conference"
