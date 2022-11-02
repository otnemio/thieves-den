import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class GST():
    
    def __init__(self,headless:bool) -> None:
        self.driver = self.get_driver(headless)

    def get_driver(self,headless):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--disable-gpu')  
            if headless:
                chrome_options.add_argument('--headless')  
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument("--disable-dev-shm-usage")
            if os.path.exists('/snap/bin/chromium.chromedriver'):
                svc = Service(executable_path='/snap/bin/chromium.chromedriver') 
            else:    
                quit()
            driver = webdriver.Chrome(
                service=svc,
                options=chrome_options
                )
            driver.get("https://services.gst.gov.in/")
            if(driver.title!="Goods & Services Tax (GST) | Login"):        
                quit()
            return driver
        except:
            print("Unknown error occurred while Opening")
    
    def login_a(self,ID,PASS):
        try:
            wait = WebDriverWait(self.driver, timeout=5)
            wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='username']"))).send_keys(ID)
            wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='user_pass']"))).send_keys(PASS)
            return True
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.error(f'{exc_type}, {fname}, {exc_tb.tb_lineno}')
            return False
    
    def login_b(self,CAPTCHA):
        try:
            wait = WebDriverWait(self.driver, timeout=5)
            wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='captcha']"))).send_keys(CAPTCHA)
            wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Login')]"))).click()
            return True
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.error(f'{exc_type}, {fname}, {exc_tb.tb_lineno}')
            return False