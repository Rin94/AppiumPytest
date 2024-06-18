import time

import pytest
from Pages.HomeScreen import HomeScreen
from Pages.ProductsScreen import ProductsScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider

class Test_ProductsCart(BaseTest):


    def test_addProduct2Cart(self):
        homeScreen = HomeScreen(self.driver)
        homeScreen.typeFirstName(name="Jared")
        homeScreen.selectCountry(country="Belgium")
        productsScreen = homeScreen.clickingOnLetShop()
        productsScreen.validateHeaderText("Products")
        productsScreen.addProducts2Cart("Air Jordan 4 Retro")
        productsScreen.addProducts2Cart("Jordan 6 Rings")
        time.sleep(15)



