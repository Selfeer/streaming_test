from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pyzbar.pyzbar import decode
from PIL import Image


def test_streaming():
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-device-for-media-stream")
    chrome_options.add_argument(f"--use-file-for-fake-video-capture=C:\\Users\\selfe\\PycharmProjects\\streaming_test"
                                f"\\Videos\\newfile.mjpeg")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_camera": 1})
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=chrome_options)

    driver.get("https://www.onlinemictest.com/webcam-test/")
    wait = WebDriverWait(driver, 20)

    # Turn on the Webcam
    wait.until(
        EC.element_to_be_clickable((By.ID, "webcam-start"))
    ).click()

    sleep(3)

    # Save QR code from the Webcam
    driver.find_element(By.ID, "webcam-test").screenshot("qr.png")

    driver.close()

    decocde_qr = decode(Image.open('qr.png'))
    decoded = decocde_qr[0].data.decode('ascii')

    assert decoded == "DevOps Conference"
