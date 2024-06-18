import pytest
@pytest.mark.flaky(2)
@pytest.mark.usefixtures("log_on_failure", "appium_driver")
class BaseTest():
    pass