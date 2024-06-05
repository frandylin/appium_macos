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
        self.profile = "Profile"
        self.introduction = "Introduction"
        self.language = "Language and region"
        self.theme = "Theme"
        self.font_size = "Font size"
        self.image_size = "Image size in the timeline"
        self.global_text = "Global"
        self.mention = "Mentions & keywords"
        self.other = "Other"
        self.room_list = "Room list"
        self.displaying_time = "Displaying time"
        self.presence = "Presence"
        self.send_message = "Send message"
        self.new_line = "New line"
        self.toggle_bold = "Toggle Bold"
        self.home = "Home"
        self.favourites = "Favourites"
        self.friends = "Friends"
        self.voice = "Voice settings"
        self.video = "Video settings"
        self.processing = "Voice processing"
        self.account = "Account"
        self.device_name = "device name"
        self.online = "last time online"
        self.version = "2.0.8"

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

    def change_settings_page(self, sort, element1, element2, element3):
        self.open_settings_page()
        tab_page = self.driver.find_element(by=AppiumBy.XPATH, value=f"//XCUIElementTypeWebView/XCUIElementTypeGroup[8]/XCUIElementTypeGroup/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup[1]/XCUIElementTypeButton[{sort}]")
        tab_page.click()
        time.sleep(1)
        element1 = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=f"value == \"{element1}\"")
        element2 = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=f"value == \"{element2}\"")
        element3 = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=f"value == \"{element3}\"")
        assert element1.is_displayed() and element2.is_displayed() and element3.is_displayed(), "elements is not displayed"
        close_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Close dialog\"")
        close_bt.click()
        time.sleep(1)



    def test_open_settings_page(self):
        self.open_settings_page()
        close_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Close dialog\"")
        close_bt.click()

    def test_change_display_name(self):
        self.change_display_name("frandy_appium_test")
        self.change_display_name("frandy")

    def test_change_language_chinese(self):
        self.change_language_chinese()

    def test_change_language_English(self):
        self.change_language_English()
    
    def test_settings_page_general(self):
        self.change_settings_page(1, self.profile, self.introduction, self.language)

    def test_settings_page_appearance(self):
        self.change_settings_page(2, self.theme, self.font_size, self.image_size)

    def test_settings_page_notifications(self):
        self.change_settings_page(3, self.global_text, self.mention, self.other)

    def test_settings_page_preferences(self):
        self.change_settings_page(4, self.room_list, self.displaying_time, self.presence)

    def test_settings_page_keyboard(self):
        self.change_settings_page(5, self.send_message, self.new_line, self.toggle_bold)

    def test_settings_page_sidebar(self):
        self.change_settings_page(6, self.home, self.favourites, self.friends)

    def test_settings_page_voice(self):
        self.change_settings_page(7, self.voice, self.video, self.processing)

    def test_settings_page_security(self):
        self.change_settings_page(8, self.account, self.device_name, self.online)

    def test_settings_page_about(self):
        self.change_settings_page(9, self.version, self.version, self.version)