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
from selenium.webdriver.common.keys import Keys
import pyautogui




class Test_Settings_Page:
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

    def teardown_method(self):
        self.driver.quit()
        
    def ckick_coordinate(self, x, y):
        self.actions.w3c_actions.pointer_action.move_to_location(x, y)
        self.actions.w3c_actions.pointer_action.click()
        self.actions.perform()
    
    def open_settings_page(self):
        settings_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@label=\"Quick settings\"]")
        settings_bt.click()
        settings_popup = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"Quick settings\"]")
        assert settings_popup.is_displayed(), "settings popup is not displayed"
        allsettings_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[2]/XCUIElementTypeButton[1]")
        allsettings_bt.click()
        time.sleep(1)
        settings_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"Settings\"")
        assert settings_text.is_displayed(), "all settings page is not displayed"

    def change_display_name(self, name):
        self.open_settings_page()
        displayname_textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[8]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[1]")
        displayname_textbox.click()
        time.sleep(1) 
        for _ in range(20):
            pyautogui.press('backspace')
        displayname_textbox.send_keys(name)
        save_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[8]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[4]/XCUIElementTypeButton[2]")
        save_bt.click()
        time.sleep(1)
        close_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Close dialog\"")
        close_bt.click()
        time.sleep(25)
        displayname_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=f"value == \"{name}\"")
        assert displayname_text.is_displayed(), "displayname_text should be display"

    def change_language_chinese(self):
        self.open_settings_page()
        language_dropdown = self.driver.find_element(by=AppiumBy.XPATH, value = "//XCUIElementTypeWebView/XCUIElementTypeGroup[8]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[5]")
        language_dropdown.send_keys("體中文")
        pyautogui.press("enter")
        time.sleep(3)
        chinese_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"好友\"")
        chinese_text.is_displayed(), "chinese text is not displayed."

    def change_language_English(self):
        settings_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@label=\"快速設定\"]")
        settings_bt.click()
        time.sleep(1)
        allsettings_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[2]/XCUIElementTypeButton[1]")
        allsettings_bt.click()
        time.sleep(1)
        language_dropdown = self.driver.find_element(by=AppiumBy.XPATH, value = "//XCUIElementTypeWebView/XCUIElementTypeGroup[8]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[5]")
        language_dropdown.send_keys("English")
        pyautogui.press("enter")
        time.sleep(3)
        english_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"Friends\"")
        english_text.is_displayed(), "english text is not displayed."





    def test_open_settings_page(self):
        self.open_settings_page()

    def test_change_display_name(self):
        self.change_display_name("frandy_appium_test")
        self.change_display_name("frandy")

    def test_change_language_chinese(self):
        self.change_language_chinese()

    def test_change_language_English(self):
        self.change_language_English()
    