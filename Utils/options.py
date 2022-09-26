from selenium.webdriver.chrome.options import Options
from file_path import get_path


def set_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-device-for-media-stream")
    chrome_options.add_argument("--use-file-for-fake-video-capture=" + get_path("newfile.mjpeg"))
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_camera": 1})
    chrome_options.add_argument("--start-maximized")

    return chrome_options


