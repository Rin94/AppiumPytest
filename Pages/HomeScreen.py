from Pages.BasePage import BasePage
from Pages.ProductsScreen import ProductsScreen
from Utilities.scroll_util import ScrollUtil
class HomeScreen(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def typeFirstName(self,name):
        self.type("nameField_XPATH",name)

    def selectCountry(self, country):
        ScrollUtil.scroll_to_text_by_AndroidUIAutomator(text=country,driver=self.driver)

    def clickingOnLetShop(self):
        self.click("letsShopButton_XPATH")
        return ProductsScreen(self.driver)

    def validateHeaderText(self, expectedText):
        actualText = self.getText("headerTxt_XPATH")
        assert actualText == expectedText, "The texts don't match"
