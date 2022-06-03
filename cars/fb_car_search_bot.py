from operator import mod
import os
import time
import cars.constants as const
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate library to open the chrome browser.
class FB_Car_Search_Bot:
    def __init__(self, driver_path=ChromeDriverManager().install(), teardown=False):
        self.driver_path = webdriver.Chrome(service=Service(driver_path))
        self.teardown = teardown
        #os.environ['PATH'] += driver_path

        # If browser notifications are getting in the way, run the following:
        # self.driver_path.chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.default_content_setting_values.notifications" : 2}
        # self.driver_path.chrome_options.add_experimental_option("prefs", prefs)
        super(FB_Car_Search_Bot, self).__init__()

    def __enter__(self):
        return self

    def __exit__(self):
        if self.teardown:
            self.driver_path.quit()

    # Open first page of the program defined in constants, in this case, "Facebook".
    def land_first_page(self):
        self.driver_path.get(const.BASE_URL)
        #time.sleep(2)

    # Login to the website
    def login_account(self):
        username = WebDriverWait(self.driver_path, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password = WebDriverWait(self.driver_path, timeout=10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

        # Enter username and password
        username.clear()
        username.send_keys(const.MY_USERNAME)
        password.clear()
        password.send_keys(const.MY_PASSWORD)

        # Login
        login_button = WebDriverWait(self.driver_path, timeout=2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()

        # We are logged in!
        #time.sleep(2)

    def land_facebook_marketplace_vehicles(self):
        self.driver_path.get(const.FB_MARKETPLACE_URL)
        #time.sleep(2)

    def set_seller(self):
        # Default is all types
        if (const.SELLER == '2' or const.SELLER == '3'):
            # Open sub-menu
            change_seller = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[3]/div[1]/div[1]/span/span')))
            change_seller.click()

            if (const.SELLER == '2'):
                change_seller = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[4]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/span')))
                change_seller.click()
            if (const.SELLER == '3'):
                change_seller = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[4]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/span')))
                change_seller.click()

            # Close sub-menu
            change_seller = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[3]/div[1]/div[1]/span/span')))
            change_seller.click()
        #time.sleep(2)

    def set_price_range(self):
        # Set minimum price range
        if (const.MIN_PRICE != ''):
            min_price = WebDriverWait(self.driver_path, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[5]/div[2]/span[1]/label/input')))
            min_price.clear()
            min_price.send_keys(const.MIN_PRICE)
        # Set maximum price range
        if (const.MAX_PRICE != ''):
            max_price = WebDriverWait(self.driver_path, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[5]/div[2]/span[2]/label/input')))
            max_price.clear()
            max_price.send_keys(const.MAX_PRICE)

    def set_year_range(self):
        # Minimum year range
        if (const.MIN_YEAR != ''):
            min_year = WebDriverWait(self.driver_path, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[8]/div[2]/span[1]/label/input')))
            min_year.clear()
            min_year.send_keys(const.MIN_YEAR)
        # Maximum year range
        if (const.MAX_YEAR != ''):
            max_year = WebDriverWait(self.driver_path, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[8]/div[2]/span[2]/label/input')))
            max_year.clear()
            max_year.send_keys(const.MAX_YEAR)
        #time.sleep(2)

    def set_car_make(self):
        if (const.CAR_MAKE != ''):
            # Open sub-menu
            car_make = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[9]/div[1]/div[1]/span/span')))
            car_make.click()

            # Toggle car make
            path_num = int(const.CAR_MAKE) + 1
            path_num = str(path_num)
            car_make = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[10]/div/div[1]/div['+path_num+']')))
            car_make.click()

            # Close sub-menu
            car_make = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[9]/div[1]/div[1]/span/span')))
            car_make.click()
        #time.sleep(2)

    def set_car_model(self):
        if (const.CAR_MODEL != ''):
            # Open sub-menu
            car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[11]/div[1]/div[1]/span/span')))
            car_model.click()

            # Infiniti
            if (const.CAR_MAKE == '27'):
                if (const.CAR_MODEL == '27a'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[2]')))
                if (const.CAR_MODEL == '27b'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[3]')))
                if (const.CAR_MODEL == '27c'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[4]')))
                if (const.CAR_MODEL == '27d'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[5]')))
                if (const.CAR_MODEL == '27e'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[6]')))
                if (const.CAR_MODEL == '27f'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[7]')))
                if (const.CAR_MODEL == '27g'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[8]')))
                if (const.CAR_MODEL == '27h'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[9]')))
                if (const.CAR_MODEL == '27i'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[10]')))
                if (const.CAR_MODEL == '27j'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[11]')))
                if (const.CAR_MODEL == '27k'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[12]')))
                if (const.CAR_MODEL == '27l'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[13]')))
                if (const.CAR_MODEL == '27m'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[14]')))
                if (const.CAR_MODEL == '27n'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[15]')))
                if (const.CAR_MODEL == '27o'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[16]')))
                if (const.CAR_MODEL == '27p'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[17]')))
                car_model.click()
            # Tesla
            if (const.CAR_MAKE == '61'):
                if (const.CAR_MODEL =='61a'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/span')))
                if (const.CAR_MODEL =='61b'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/span')))
                if (const.CAR_MODEL =='61c'):
                    car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]/div[4]/div/div[1]/div/div[1]/div/div/div/span')))

                car_model.click()

                    
            # Close sub-menu
            #car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[11]/div[1]/div[1]/span/span')))
            #car_model.click()

            
        time.sleep(2)

    def input_search_params(self):
        # Set seller type
        self.set_seller()
        # Set price range
        self.set_price_range()
        # Set year range
        self.set_year_range()
        # Set car make
        self.set_car_make()
        # Set car model
        self.set_car_model()
        
        time.sleep(5)
        

        # '//*[@id="seo_filters"]/div[2]/div[12]/div/div[1]'
        # WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '')))
