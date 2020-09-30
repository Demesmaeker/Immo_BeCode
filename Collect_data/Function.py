from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd
import os


def init_webdriver(is_firefox: bool = False) -> webdriver:
    """ init the web driver with chrome or firefox """
    if is_firefox:
        profile = webdriver.FirefoxProfile()
        # disable pictures
        profile.set_preference('permissions.default.image', 2)
        driver = webdriver.Firefox(firefox_profile=profile)
    else:
        options = webdriver.ChromeOptions()
        # hide pictures
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        driver = webdriver.Chrome(options=options)
    return driver


def init_connection(driver: webdriver, url, title: str = None, check_button: bool = False):
    """
        init the connection to the url
        check if a banner (like cookie-banner) block us and click on it if needed
    """
    driver.get(url)
    if title is not None:
        assert title in driver.title
    if check_button:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'uc-btn-accept-banner'))
            )
            if element is not None:
                element.click()
                print("button clicked")
        except Exception as e:
            print(e)
