import pytest
from Pages.HomeScreen import HomeScreen
from Pages.ProductsScreen import ProductsScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider

class Test_EnterProductsScreen(BaseTest):

    @pytest.mark.parametrize("name,country,sex", dataProvider.get_data("LoginGeneralStore"))
    def test_enterData(self,name, country,sex):
        homeScreen = HomeScreen(self.driver)
        homeScreen.typeFirstName(name=name)
        homeScreen.selectCountry(country=country)
        productsScreen = homeScreen.clickingOnLetShop()
        productsScreen.validateHeaderText("Products")





