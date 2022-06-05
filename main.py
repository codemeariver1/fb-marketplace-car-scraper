from cars.fb_car_search_bot import FB_Car_Search_Bot

inst = FB_Car_Search_Bot()

try:
    inst.land_first_page()
    inst.login_account()
    inst.land_facebook_marketplace_vehicles()
    inst.input_search_params()
    inst.grab_car_data()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            "You are trying to run the FB-Marketplace-Car-Scraper bot from the command line\n"
            "Please add your Selenium Driver to PATH \n"
            "Windows: \n"
            "   set PATH=%PATH%;C:\path-to-your-folder\ \n\n"
            "Mac or Linux: \n"
            "   PATH=$PATH:/path/toyour/folder/ \n"
        )
    else:
        raise
