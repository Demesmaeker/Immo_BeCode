from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd
import os


######################################
#     Get the urls of each page      #
######################################

base_url = "https://www.immoweb.be/"