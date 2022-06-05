import os
import time
from cars.car_data import CarData
from cars.car_filtration import SearchFiltration
import cars.constants as const
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IPython.core.display import display, HTML

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

    def input_search_params(self):
        filtration = SearchFiltration(driver=self.driver_path)
        # Set seller type
        filtration.set_seller()
        # Set price range
        filtration.set_price_range()
        # Set year range
        filtration.set_year_range()
        # Set car make
        filtration.set_car_make()
        # Set car model
        filtration.set_car_model()

    def grab_car_data(self):
        run_report = CarData(driver=self.driver_path)
        run_report.grab_car_listings()
        
    time.sleep(5)
        
        # WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '')))
