import pytest
from selenium import webdriver
from lesson7.mainform import MainForm


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):

    form = MainForm(driver)
    form.fill_parameters("first-name", "Иван")
    form.fill_parameters("last-name", "Петров")
    form.fill_parameters("address", "Ленина,55-3")
    form.fill_parameters("e-mail", "test@skypro.com")
    form.fill_parameters("phone", "+7985899998787")
    form.fill_parameters("city", "Москва")
    form.fill_parameters("country", "Россия")
    form.fill_parameters("job-position", "QA")
    form.fill_parameters("company", "SkyPro")

    form.click_submit()
    assert "danger" in form.return_result("zip-code")


    fields_to_check = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city', 'country', 'job-position', 'company']

    for field_name in fields_to_check:
        assert "success" in form.return_result(field_name)

    driver.quit()