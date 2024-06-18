import logging

from appium.webdriver.common.appiumby import AppiumBy
from Utilities import configReader
from  Utilities.LogUtil import Logger
from appium import webdriver

log = Logger(__name__, logging.INFO)

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = None
        if str(locator).endswith("_XPATH"):
            element =self.driver.find_element(AppiumBy.XPATH,
                                              configReader.readConfig("locators",locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(AppiumBy.ID,
                                               configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                               configReader.readConfig("locators", locator))
        log.logger.info("Clicking on an Element: " + str(locator))
        element.click()

    def clickIndex(self, locator,index):
        element = None
        if str(locator).endswith("_XPATH"):
            element =self.driver.find_elements(AppiumBy.XPATH,
                                              configReader.readConfig("locators",locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_elements(AppiumBy.ID,
                                               configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            element = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID,
                                               configReader.readConfig("locators", locator))
        log.logger.info("Clicking on an Element: " + str(locator) + " With index: " + str(index))
        element[index].click()

    def type(self, locator, value):
        element = None
        print("Locator: ",configReader.readConfig("locators", locator))
        if str(locator).endswith("_XPATH"):
            element =self.driver.find_element(AppiumBy.XPATH,
                                              configReader.readConfig("locators",locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(AppiumBy.ID,
                                               configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                               configReader.readConfig("locators", locator))
        log.logger.info("Typing in Element: " + str(locator) + " entered the value as: " + value)
        element.send_keys(value)

    def getText(self, locator):
        element = None
        if str(locator).endswith("_XPATH"):
            element =self.driver.find_element(AppiumBy.XPATH,
                                              configReader.readConfig("locators",locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(AppiumBy.ID,
                                               configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                               configReader.readConfig("locators", locator))
        log.logger.info("Getting the text of the Element: " + str(locator) + " as: " + element.text)
        return element.text

    def getElement(self, locator):
        element = None
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(AppiumBy.XPATH,
                                               configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(AppiumBy.ID,
                                               configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                               configReader.readConfig("locators", locator))
        log.logger.info("Getting the Element: " + str(locator) + " locator")
        return element

    def getElements(self, locator):
        elements = None
        if str(locator).endswith("_XPATH"):
            elements = self.driver.find_elements(AppiumBy.XPATH,
                                               configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            elements = self.driver.find_elements(AppiumBy.ID,
                                               configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ACCESSIBILITYID"):
            elements = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID,
                                               configReader.readConfig("locators", locator))
        log.logger.info("Getting the Elements of: " + str(locator) + " locator")
        return elements


