from cars.fb_car_search_bot import FB_Car_Search_Bot

inst = FB_Car_Search_Bot()
inst.land_first_page()
inst.login_account()
inst.land_facebook_marketplace_vehicles()
inst.input_search_params()
inst.grab_car_data()