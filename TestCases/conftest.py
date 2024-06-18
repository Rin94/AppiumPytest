import allure
import pytest
import os
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def appium_driver(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'JaredSalinasEmulator'
    desired_caps['app'] = os.getcwd()+"/../App/General-Store.apk"
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
    request.cls.driver = driver
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
