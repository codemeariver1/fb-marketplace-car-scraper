import cars.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchFiltration:
    def __init__(self, driver: WebDriver):
        self.driver_path = driver

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
            car_model = WebDriverWait(self.driver_path, timeout=5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="seo_filters"]/div[2]/div[11]/div[1]/div[1]/span/span')))
            car_model.click()
        #time.sleep(2)