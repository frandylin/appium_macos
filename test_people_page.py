import pytest
import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import pyautogui
from test_room_page import Test_Room_Page




class Test_Room_Page:
    def setup_method(self):
        options = AppiumOptions()
        options.load_capabilities({
            "appium:automationName": "Mac2",
            "appium:platformName": "mac",
            "appium:bundleId": "im.shaberi.desktop",
            "appium:noReset": "true",
            "appium:systemPort": "10100",
            "appium:systemHost": "0.0.0.0",
            "appium:webDriverAgentMacUrl": "http://localhost:10100",
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        })

        self.driver = webdriver.Remote("http://0.0.0.0:4723", options=options)
        self.actions = ActionChains(self.driver)
        self.actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_MOUSE, 'mouse'))
        self.wait = WebDriverWait(self.driver, 10)
        self.add_bt = "label == \"Start group chat, add friends, search for groups\""
        self.add_friend_option = (380, 120)
        self.add_group_option = (380, 160)


    def teardown_method(self):
        self.driver.quit()

    def ckick_coordinate(self, x, y):
        self.actions.w3c_actions.pointer_action.move_to_location(x, y)
        self.actions.w3c_actions.pointer_action.click()
        self.actions.perform()

    def add_friend(self):
        add_button = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=self.add_bt)
        add_button.click()
        time.sleep(1)
        self.ckick_coordinate(*self.add_friend_option)
        time.sleep(1)
        textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeTextField")
        textbox.send_keys("tester") #search userid
        search_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[8]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[3]/XCUIElementTypeButton")
        search_bt.click()
        time.sleep(1)
        user_name = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"tester\"]")
        assert user_name.is_displayed() , "cant search for user"
        add_friend_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[8]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[5]/XCUIElementTypeGroup/XCUIElementTypeButton")
        add_friend_bt.click()
        time.sleep(1)
        friend = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[@label=\"People\"]/XCUIElementTypeGroup/XCUIElementTypeGroup/XCUIElementTypeOutlineRow[@label=\"testfrandy\"]")
        assert friend.is_displayed(), "add friend iss not success"

    def join_group(self):
        recently_group = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeButton[@label=\"Autogroup\"])[1]/XCUIElementTypeGroup")
        recently_group.click()
        time.sleep(1)
        join_group_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeButton")
        join_group_bt.click()
        time.sleep(1)
        group = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[@label=\"Rooms\"]/XCUIElementTypeGroup/XCUIElementTypeGroup/XCUIElementTypeOutlineRow[@label=\"Autogroup\"]")
        assert group.is_displayed, "join group is not success"

    def create_group(self):
        add_button = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=self.add_bt)
        add_button.click()
        time.sleep(1)
        self.ckick_coordinate(*self.add_group_option)
        time.sleep(1)
        name_textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[9]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[1]/XCUIElementTypeTextField")
        topic_textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[9]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeTextField")
        name_textbox.send_keys("Appium Fucking Lets gooo")
        topic_textbox.send_keys("Appium testing")
        create_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[9]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeButton[2]")
        create_bt.click()
        time.sleep(2)
        name_text = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypePopUpButton[@label=\"Room options\"]/XCUIElementTypeStaticText/XCUIElementTypeStaticText[@value=\"Appium Fucking Lets gooo\"])")
        topic_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"Appium testing\"")
        assert  name_text.is_displayed(), "create room failed"
        assert  topic_text.is_displayed(), "create room failed"

    # def test_add_friend(self):
    #     self.add_friend()

    # def test_join_group(self):
    #     self.join_group()
    
    def test_create_group(self):
        self.create_group()
    
   