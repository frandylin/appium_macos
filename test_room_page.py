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
        self.personal_room = "(//XCUIElementTypeOutlineRow[@label=\"testfrandy\"])[1]/XCUIElementTypeGroup[1]"
        self.group_room = "(//XCUIElementTypeOutlineRow[@label=\"Autogroup\"])[1]/XCUIElementTypeGroup[1]"
        self.personal_favorite = (481,94)
        self.group_favorite = (481, 134)
        self.personal_favorite_room = "//XCUIElementTypeGroup[@label=\"Favourites\"]/XCUIElementTypeGroup/XCUIElementTypeGroup/XCUIElementTypeOutlineRow[@label=\"testfrandy\"]"
        self.group_favorite_room = "//XCUIElementTypeGroup[@label=\"Favourites\"]/XCUIElementTypeGroup/XCUIElementTypeGroup/XCUIElementTypeOutlineRow[@label=\"Autogroup\"]"
        self.personal_cancell_favorite_room = "//XCUIElementTypeGroup[@label=\"Friends\"]/XCUIElementTypeGroup/XCUIElementTypeGroup/XCUIElementTypeOutlineRow[@label=\"testfrandy\"]" #被還原後的個人聊天室
        self.group_cancell_favorite_room = "//XCUIElementTypeGroup[@label=\"Rooms\"]/XCUIElementTypeGroup/XCUIElementTypeGroup/XCUIElementTypeOutlineRow[@label=\"Autogroup\"]" #被還原後得群聊
        self.personal_file = (481, 134)
        self.group_file = (481, 214)
        self.personal_leave = (481, 214)
        self.group_leave = (481 , 334)

    def teardown_method(self):
        self.driver.quit()

    def ckick_coordinate(self, x, y):
        self.actions.w3c_actions.pointer_action.move_to_location(x, y)
        self.actions.w3c_actions.pointer_action.click()
        self.actions.perform()

    def check_window_size(self):
        window_size = self.driver.get_window_size()
        print("window size:", window_size)
        if window_size["width"] != 1920 and window_size["height"] != 1080:
            self.driver.maximize_window()
        else:
            print("window size is already maximized")


    def side_menu(self):
        self.check_window_size()
        time.sleep(1)
        favorites_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@label=\"Favourites\"]")
        favorites_bt.click()
        favorites_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"Favourites\"")
        assert favorites_text.is_displayed(), "favourites page is not displayed"
        friend_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@label=\"Friends\"]")
        friend_bt.click()
        time.sleep(1)
        friend_text = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"Friends\"]")
        assert friend_text.is_displayed(), "friends page is not displayed"
        otherroom_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@label=\"Other rooms\"]")
        otherroom_bt.click()
        time.sleep(1)
        otherroom_text = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"Rooms\"]")
        assert otherroom_text.is_displayed(), "group page is not displayed"
        time.sleep(1)
        home_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@label=\"Home\"]")
        home_bt.click()
        time.sleep(1)

    def send_message(self, room_type):
        room = self.driver.find_element(by=AppiumBy.XPATH, value=room_type)
        room.click()
        time.sleep(1)
        textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeGroup[5]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup")
        textbox.send_keys("Lets goooo")
        send_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Send message\"")
        send_bt.click()
        message = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeStaticText[@value=\"Lets goooo\"])")
        assert message.is_displayed(), "message is not displayed"

    def send_emoji(self):
        # 由於 mac2 無法點擊到 emoji 故採取直接傳送 emoji 字元
        textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeGroup[5]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup")
        textbox.send_keys("👍️")
        send_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Send message\"")
        send_bt.click()
        emoji_message = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeStaticText[@value=\"👍️\"])")
        assert emoji_message.is_displayed(), "emoji message is not displayed"

    def send_attachment(self):
        attachment_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Attachment\"")
        attachment_bt.click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@value=\"桌面\"]").click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeTextField[@value=\"測試報告_0811.xlsx\"]").click()
        open_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeSheet[@label=\"打開\"]/XCUIElementTypeButton[2]")
        open_bt.click()
        time.sleep(1)
        up_load_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[2]/XCUIElementTypeButton")
        up_load_bt.click()
        time.sleep(1)
        file_message = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeStaticText[@value=\"測試報告_0811.xlsx (108.24 kB)\"])")
        attachment_bt.click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeTextField[@value=\"pepe.jpeg\"]").click()
        open_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeSheet[@label=\"打開\"]/XCUIElementTypeButton[2]")
        open_bt.click()
        time.sleep(1)
        up_load_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[2]/XCUIElementTypeButton")
        up_load_bt.click()
        time.sleep(1)
        image_message = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeImage[@label=\"pepe.jpeg\"])")
        assert file_message.is_displayed(), "file message is not displayed"
        assert image_message.is_displayed(), "image message is not displayed"

    def search_history(self):
        search_icon = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@label=\"Search\"]")
        search_icon.click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeTextField").send_keys("Lets")
        search_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeGroup[2]/XCUIElementTypeButton[1]")
        search_bt.click()
        time.sleep(1)
        history_message = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeLink[@label=\"Lets goooo\"])/XCUIElementTypeGroup")
        assert history_message.is_displayed(), "history is not displayed"
        cancel_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeGroup[2]/XCUIElementTypeButton[2]")
        cancel_bt.click()

    def favorite(self, favorite_type, room_type, cancelled_room):
        room_options = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]")
        room_options.click()
        self.ckick_coordinate(*favorite_type)
        time.sleep(1)
        room_favorite = self.driver.find_element(by=AppiumBy.XPATH, value=room_type)
        assert room_favorite.is_displayed(), "favourite room is not displayed"
        room_options = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]")
        room_options.click()
        self.ckick_coordinate(*favorite_type)
        time.sleep(1)
        room_favourite_cancelled = self.driver.find_element(by=AppiumBy.XPATH, value=cancelled_room)
        assert room_favourite_cancelled.is_displayed(), "favorite room was not cancelled"

    def file_history(self, file_type):
        room_options = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]")
        room_options.click()
        # 在执行具体动作之前，先移动到指定的位置
        self.ckick_coordinate(*file_type)
        time.sleep(1)
        file_history = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeGroup[6]")
        assert file_history.is_displayed(), "file page is not displayed"
        self.ckick_coordinate(1595, 85) #back 
        time.sleep(1)
        self.ckick_coordinate(1890, 85) #close
        assert  not file_history.is_displayed(), "file page is not collapsed"                  

    def leave_room(self, leave_type):
        room_options = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]")
        room_options.click()
        self.ckick_coordinate(*leave_type)
        time.sleep(1)
        leave_bt = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeGroup[2]/XCUIElementTypeButton[2]")
        leave_bt.click()
        time.sleep(1)
        assert self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"Welcome to Shaberi\"").is_displayed(), "leave room is not sucess"

    def member_list(self):
        room_options = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]")
        room_options.click()
        self.ckick_coordinate(481, 174)
        time.sleep(1)
        member_list = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeGroup[6]")
        assert member_list.is_displayed(), "member list is not displayed"
        self.ckick_coordinate(1595, 85) #back 
        time.sleep(1)
        self.ckick_coordinate(1890, 85)
        assert not member_list.is_displayed(), "member lis is not collapsed"
    
    def copy_room_link(self):
        room_options = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypePopUpButton[@label=\"Room options\"]")
        room_options.click()
        time.sleep(1)
        # 在执行具体动作之前，先移动到指定的位置
        self.ckick_coordinate(481, 298)
        textbox = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeWebView/XCUIElementTypeGroup[1]/XCUIElementTypeGroup[1]/XCUIElementTypeGroup/XCUIElementTypeGroup[3]/XCUIElementTypeGroup/XCUIElementTypeGroup[5]/XCUIElementTypeGroup[2]/XCUIElementTypeGroup")
        time.sleep(1)
        self.actions.w3c_actions.pointer_action.move_to(textbox)
        self.actions.w3c_actions.pointer_action.context_click()
        self.actions.perform()
        pyautogui.press("p")
        time.sleep(1)
        send_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Send message\"")
        send_bt.click()
        link_message = self.driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[starts-with(@value, \"https://shaberi.com/#/\")]\n")
        assert link_message .is_displayed(), "copy link is not success"

    def share_room(self):
        room_info = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Room info\"")
        room_info.click()
        self.ckick_coordinate(1660, 340) # Share room option
        time.sleep(1)
        share_room_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"Share Room\"")
        share_room_qrcode = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"QR Code\"")
        assert share_room_text.is_displayed(), "share room text is not displayed"
        assert share_room_qrcode.is_displayed(), "qrcode is not displayed"
        close_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Close dialog\"")
        close_bt.click()
        time.sleep(1)
        self.ckick_coordinate(1890, 85) #close
        
    def room_setting_popup(self):
        room_info = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Room info\"")
        room_info.click()
        self.ckick_coordinate(1660, 380) # Share room option
        time.sleep(1)
        general_text = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="value == \"General\"")
        assert general_text.is_displayed(), "setting popup is not displayed"

    def test_side_menu(self):
        self.side_menu()

    def test_send_message_personal(self):
        self.send_message(self.personal_room)
    
    def test_send_emoji_personal(self):
        self.send_emoji()

    def test_send_attachment_personal(self):
        self.send_attachment()

    def test_search_history_personal(self):
        self.search_history()
    
    def test_favorite_personal(self):
        self.favorite(self.personal_favorite, self.personal_favorite_room, self.personal_cancell_favorite_room)

    def test_file_history_personal(self):
        self.file_history(self.personal_file)

    def test_leave_personal(self):
        self.leave_room(self.personal_leave)

    def test_send_message_group(self):
        self.send_message(self.group_room)

    def test_send_emoji_group(self):
        self.send_emoji()

    def test_send_attachment_group(self):
        self.send_attachment()

    def test_search_history_group(self):
        self.search_history()
    
    def test_favorite_group(self):
        self.favorite(self.group_favorite, self.group_favorite_room, self.group_cancell_favorite_room)

    def test_file_history_group(self):
        self.file_history(self.group_file)

    def test_member_list(self):
        self.member_list()

    def test_copy_room_link(self):
        self.copy_room_link()

    def test_share_room(self):
        self.share_room()

    def test_room_setting_popup(self):
        self.room_setting_popup()
        close_bt = self.driver.find_element(by=AppiumBy.IOS_PREDICATE, value="label == \"Close dialog\"")
        close_bt.click()

    def test_leave_group(self):
        self.leave_room(self.group_leave)
        
