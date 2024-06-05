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



class Test_People_Page:
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

    def text_friend_name(self):
        friend_name = "testfrandy"
         #無法定位到 element 故使用 for 模鍵盤輸入
        for i in friend_name:
             pyautogui.press(f"{i}")

    def add_friend(self):
        add_button = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=self.add_bt)
        add_button.click()
        time.sleep(1)
        self.ckick_coordinate(*self.add_friend_option)
        time.sleep(1)
        textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeTextField")
        textbox.send_keys("tester") #search userid
        search_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[3]/XCUIElementTypeButton")
        search_bt.click()
        time.sleep(1)
        user_name = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"tester\"]")
        assert user_name.is_displayed() , "cant search for user"
        add_friend_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[5]/XCUIElementTypeGroup/XCUIElementTypeButton")
        add_friend_bt.click()
        time.sleep(2)
        friend = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[@label=\"Friends\"]//XCUIElementTypeOutlineRow[@label=\"testfrandy\"]")
        assert friend.is_displayed(), "add friend is not success"

    def join_group(self):
        recently_group = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeButton[@label=\"Autogroup\"])[1]/XCUIElementTypeGroup")
        recently_group.click()
        time.sleep(1)
        join_group_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeButton")
        join_group_bt.click()
        time.sleep(3)
        group = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[@label=\"Rooms\"]/XCUIElementTypeGroup/XCUIElementTypeGroup/XCUIElementTypeOutlineRow[@label=\"Autogroup\"]")
        assert group.is_displayed, "join group is not success"

    def create_group(self):
        add_button = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value=self.add_bt)
        add_button.click()
        time.sleep(1)
        self.ckick_coordinate(*self.add_group_option)
        time.sleep(2)
        name_textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[1]/XCUIElementTypeTextField")
        topic_textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[2]/XCUIElementTypeTextField")
        name_textbox.send_keys("Appium Fucking Lets gooo")
        topic_textbox.send_keys("Appium testing")
        create_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[2]/XCUIElementTypeButton[2]")
        create_bt.click()
        time.sleep(3)
        name_text = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypePopUpButton[@label=\"Room options\"]/XCUIElementTypeStaticText/XCUIElementTypeStaticText[@value=\"Appium Fucking Lets gooo\"])")
        topic_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"Appium testing\"")
        assert  name_text.is_displayed(), "create room failed"
        assert  topic_text.is_displayed(), "create room failed"

    def room_setting_general(self):
        room_info = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Room info\"")
        room_info.click()
        self.ckick_coordinate(1660, 380) # Share room option
        time.sleep(1)
        general_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"General\"")
        assert general_text.is_displayed(), "setting popup is not displayed"
        room_name = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeTextField")
        room_topic = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeTextView")
        room_name.send_keys("appium_name")
        room_topic.send_keys("appium_topic")
        save_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[4]/XCUIElementTypeButton[2]")
        save_bt.click()
        time.sleep(3)
        close_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Close dialog\"")
        close_bt.click()
        room_name_text = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]/XCUIElementTypeStaticText/XCUIElementTypeStaticText[@value=\"appium_name\"]")
        room_topic_text = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[@label=\"appium_topic\"]")
        assert room_name_text.is_displayed(), "room name devise is not success"
        assert room_topic_text.is_displayed(), "room topic devise is not success"

    def invite_group(self):
        room_options = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]")
        room_options.click()
        self.ckick_coordinate(550,75)
        time.sleep(1)
        self.text_friend_name()
        time.sleep(1)
        friend = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"testfrandy\"]")
        friend.click()
        time.sleep(1)
        invite_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[3]/XCUIElementTypeButton")
        invite_bt.click()
        time.sleep(2)
        invite_message = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"frandy invited testfrandy\"")
        assert invite_message.is_displayed(), "invite member to room is not success"
        room_options = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]")
        room_options.click()
        time.sleep(1)
        self.ckick_coordinate(481 , 334)
        time.sleep(1)
        leave_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[2]/XCUIElementTypeButton[2]")
        leave_bt.click()
        time.sleep(1)
        
        

    def search_friend(self):
         search_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"Search\"")
         search_bt.click()
         self.text_friend_name()
         time.sleep(1)
         friend = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"testfrandy\"]")
         assert friend.is_displayed(), "search friend is not success"
         
    def enter_room_from_search(self):
        friend = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"testfrandy\"]")
        friend.click()
        time.sleep(1)
        friend_room = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypePopUpButton[@label=\"Room options\"]/XCUIElementTypeStaticText/XCUIElementTypeStaticText[@value=\"testfrandy\"])")
        assert friend_room.is_displayed(), "enter room from search is not success"
        

    def test_add_friend(self):
        self.add_friend()

    def test_join_group(self):
        self.join_group()
    
    def test_create_group(self):
        self.create_group()

    def test_room_setting_general(self):
        self.room_setting_general()
    
    def test_invite_group(self):
        self.invite_group()

    def test_search_friend(self):
        self.search_friend()

    def test_enter_room_from_search(self):
        self.enter_room_from_search()
    
   