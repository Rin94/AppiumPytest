from appium.webdriver.common.appiumby import AppiumBy

class ScrollUtil:

    @staticmethod
    def scroll_to_text_by_AndroidUIAutomator(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().textContains'
                   '("'+text+'").instance(0))').click()

    @staticmethod
    def swipeDown(howManySwipes, driver):
        [driver.swipe(start_x=600, start_y=1000, end_x=600, end_y=1, duration=2000) for i in range(0,howManySwipes)]

    @staticmethod
    def swipeUp(howManySwipes, driver):
        [driver.swipe(start_x=600, start_y=500, end_x=600, end_y=1000, duration=2000) for i in range(0,howManySwipes)]

    @staticmethod
    def swipeLeft(howManySwipes, driver):
        [driver.swipe(start_x=900, start_y=1000, end_x=200, end_y=1000, duration=2000) for i in range(0,howManySwipes)]

    @staticmethod
    def swipeRight(howManySwipes, driver):
        [driver.swipe(start_x=200, start_y=1000, end_x=900, end_y=1000, duration=2000) for i in range(0,howManySwipes)]

