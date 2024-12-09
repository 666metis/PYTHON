from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson7.contact_information import ContactInformation
from lesson7.result import Result
from lesson7.shop_products import ShopProducts
from lesson7.shopmain import ShopMain


def test_fill_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    shopmain = ShopMain(driver)
    shopmain.fill_parameter("user-name", "standard_user")
    shopmain.fill_parameter("password","secret_sauce")
    shopmain.click_button()
    shopproducts = ShopProducts(driver)
    shopproducts.add_product("add-to-cart-sauce-labs-backpack")
    shopproducts.add_product("add-to-cart-sauce-labs-bolt-t-shirt")
    shopproducts.add_product("add-to-cart-sauce-labs-onesie")
    shopproducts.add_product("shopping_cart_container")
    shopproducts.add_product("checkout")
    contactinformation = ContactInformation(driver)
    contactinformation.contact_information("first-name", "Иван")
    contactinformation.contact_information("last-name", "Иванов")
    contactinformation.contact_information("postal-code", "821635")
    contactinformation.continue_button("continue")

    result = Result(driver)
    assert result.return_result() == "58.29"

    driver.quit()