from Pages.BasePage import BasePage
from Utilities.scroll_util import ScrollUtil
class ProductsScreen(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def validateHeaderText(self, expectedText):
        actualText = self.getText("headerTxt_XPATH")
        assert actualText == expectedText, "The texts don't match"

    def addProducts2Cart(self, expectedProduct):
        ScrollUtil.scroll_to_text_by_AndroidUIAutomator(text=expectedProduct, driver=self.driver)
        productList = self.getElements("txtProductName_ID")
        productCount = len(productList)
        for i in range (0, productCount):
            actualProduct = productList[i].text
            if actualProduct == expectedProduct:
                self.clickIndex('btnAdd2Cart_ID',i)
