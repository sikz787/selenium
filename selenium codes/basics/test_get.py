import time
from lib2to3.pgen2 import driver

from selenium import webdriver
import logging

from selenium.webdriver.common.by import By


def test_get_url():
    driver = webdriver.Chrome()
    #LOGGER = logging.getLogger(__name__)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    print(driver.title)
    time.sleep(3)
    appointment = driver.find_element(By.ID, "btn-make-appointment")
    appointment.click()
    time.sleep(3)
    #LOGGER.info(driver.title)

