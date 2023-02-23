from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from Login.LoginPage import LoginPage
from Product.product import Product
from Product.cart import YourCart
from Product.checkout import CheckOut
from Product.checkout_description import  CheckOutDescription
from Product.complete import Complete
from Logout.logout import Logout

import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

login_page = LoginPage\
    (driver)
driver.get("https://www.saucedemo.com/")
login_page.set_username("standard_user")
login_page.set_password("secret_sauce")
login_page.click_login()


product_page = Product(driver)
product_page.add_to_cart_backpack()
product_page.add_to_cart_bike_light()
product_page.add_to_cart_bolt_tshirt()
time.sleep(1)


cart = YourCart(driver)
cart.remove_backpack()
time.sleep(1)
cart.go_to_cart()
time.sleep(1)
cart.shop()
time.sleep(1)


product_page.add_to_cart_fleece_jacket()
time.sleep(1)

cart.go_to_cart()
time.sleep(1)

cart.checkout()
time.sleep(4)

cout = CheckOut(driver)
cout.first_name()
cout.last_name()
cout.zip_code()
cout.checkout_continue()
time.sleep(3)

cod = CheckOutDescription(driver)
cod.cod_finish()
time.sleep(2)

comp = Complete(driver)
comp.backhome()
time.sleep(2)

log = Logout(driver)
log.click_menu()
log.click_menu()
time.sleep(5)