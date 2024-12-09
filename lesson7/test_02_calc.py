import pytest
from selenium import webdriver
from lesson7.calcmain import CalcMain


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_calc(driver):
    calc = CalcMain(driver)
    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")


    assert calc.check_result(15) == "15"