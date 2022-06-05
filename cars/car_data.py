import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CarData:
    def __init__(self, driver: WebDriver):
        self.driver_path = driver

    def grab_car_listings(self):
        car_page_links = []

        # Scroll to the end of the page
        n_scrolls = 10
        for i in range(1, n_scrolls):
            self.driver_path.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            
        car_listings = self.driver_path.find_elements(by=By.XPATH, value="//a[contains(@href, '/marketplace/item/')]")
        for car in car_listings:
            # Print brief car summary
            #print(car.text)

            # Get all of the car page URLs
            #print(car.get_attribute('Href'))
            car_page_links += (car.get_attribute('Href'),)
            
            # Display car image
            #display(HTML(car.get_attribute('outerHTML')))
            #print('------------------------------------')

        #print(car_page_links)

        for link in car_page_links:
            self.driver_path.get(link)
            time.sleep(5)
            
            # Get the details presented in the page listing header
            car_name = self.driver_path.find_element(
                by=By.CSS_SELECTOR, 
                value='div.dati1w0a.qt6c0cv9.hv4rvrfc.discj3wi'
                ).find_element(
                    by=By.CSS_SELECTOR, 
                    value='span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.oi732d6d.ik7dh3pa.ht8s03o8.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.ns63r2gh.hrzyx87i.o0t2es00.f530mmz5.hnhda86s.oo9gr5id'
                    ).get_attribute('innerHTML')
            
            car_price = self.driver_path.find_element(
                by=By.CSS_SELECTOR, 
                value='div.dati1w0a.qt6c0cv9.hv4rvrfc.discj3wi'
                ).find_element(
                    by=By.CSS_SELECTOR, 
                    value='span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.oi732d6d.ik7dh3pa.ht8s03o8.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d9wwppkn.iv3no6db.a5q79mjw.g1cxx5fr.lrazzd5p.oo9gr5id'
                    ).get_attribute('innerHTML')
            
            # The following declaration, time_since_posted, is made up of the following two 
            # declarations: time_since_posted and seller_location
            time_since_posted_summary = self.driver_path.find_element(
                by=By.CSS_SELECTOR, 
                value='div.dati1w0a.qt6c0cv9.hv4rvrfc.discj3wi'
                ).find_element(
                    by=By.CSS_SELECTOR,
                    value='div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg'
                ).find_element(
                    by=By.CSS_SELECTOR,
                    value='span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.oi732d6d.ik7dh3pa.ht8s03o8.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d9wwppkn.mdeji52x.e9vueds3.j5wam9gi.b1v8xokw.m9osqain'
                ).text
            
            time_since_posted = self.driver_path.find_element(
                by=By.CSS_SELECTOR, 
                value='div.dati1w0a.qt6c0cv9.hv4rvrfc.discj3wi'
                ).find_element(
                    by=By.CSS_SELECTOR,
                    value='div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg'
                ).find_element(
                    by=By.CSS_SELECTOR,
                    value='span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.oi732d6d.ik7dh3pa.ht8s03o8.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d9wwppkn.mdeji52x.e9vueds3.j5wam9gi.b1v8xokw.m9osqain'
                ).get_attribute('innerHTML')
            time_since_posted = time_since_posted[time_since_posted.find("->") + 2: time_since_posted.find("ago")]
            
            seller_location = self.driver_path.find_element(
                by=By.CSS_SELECTOR, 
                value='div.dati1w0a.qt6c0cv9.hv4rvrfc.discj3wi'
                ).find_element(
                    by=By.CSS_SELECTOR,
                    value='div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.discj3wi.b5q2rw42.lq239pai.mysgfdmx.hddg9phg'
                ).find_element(
                    by=By.CSS_SELECTOR,
                    value='span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.oi732d6d.ik7dh3pa.ht8s03o8.e9vueds3.j5wam9gi.b1v8xokw.m9osqain'
                ).find_element(
                    by=By.CSS_SELECTOR,
                    value='span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.oi732d6d.ik7dh3pa.ht8s03o8.e9vueds3.j5wam9gi.b1v8xokw.m9osqain'
                ).get_attribute('innerHTML')

            # Expand and get the seller's car description
            try: # Check for 'See translation' button on description
                translate_desc = self.driver_path.find_element(
                    by=By.CSS_SELECTOR, 
                    value='div.ii04i59q.a8nywdso.f10w8fjw.rz4wbd8a.pybr56ya'
                    ).find_element(By.CSS_SELECTOR, 
                    value='span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.oi732d6d.ik7dh3pa.ht8s03o8.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d9wwppkn.mdeji52x.e9vueds3.j5wam9gi.lrazzd5p.oo9gr5id')
                     # alt translate id: 'div.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8'
                translate_desc.click()
            except:
                pass
            time.sleep(5)

            try: # Check for 'See more' button on description
                expand_desc = self.driver_path.find_element(
                    by=By.CSS_SELECTOR, 
                    value='div.ii04i59q.a8nywdso.f10w8fjw.rz4wbd8a.pybr56ya'
                    ).find_element(By.CSS_SELECTOR, 
                    value='div.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.l9j0dhe7.abiwlrkh.p8dawk7l.lzcic4wl')
                expand_desc.click()
            except:
                pass
            time.sleep(5)

            try: # Check for seller description
                car_desc = self.driver_path.find_element(
                    by=By.CSS_SELECTOR, 
                    value='div.ii04i59q.a8nywdso.f10w8fjw.rz4wbd8a.pybr56ya'
                    ).get_attribute('innerHTML')
                car_desc = car_desc[car_desc.find('">') + 2: car_desc.find("<!") + 1]
                try:
                    car_desc = car_desc[car_desc.find('"</') + 1: car_desc.find('/div')]
                except:
                    pass
            except:
                car_desc = ('No information was found by the bot')

            #print(car_page_heading)
            #print('---')
            print(car_name)
            print(car_price)
            print('Listed', time_since_posted, 'ago in', seller_location)
            print(car_desc)
            print(link)
            print('---')
        time.sleep(2)