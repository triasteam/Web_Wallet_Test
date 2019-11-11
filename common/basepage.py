#coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os.path
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from random import choice
from common.logger import Logger

logger = Logger().getlog()
class BasePage(object):
    "Define a page base class that all pages inherit and encapsulate common page manipulation methods into this class."
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, selector):
        element = ''
        if '<=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('<=>')[0]
        selector_value = selector.split('<=>')[1]
        if selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == 'classname':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    # input
    def input(self, selector, text):
        el = self.find_element(selector)
        try:
            el.clear()
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    # click
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            # logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

            # switch to iframe

    def switch_frame(self):
        iframe = self.find_element('classname=>embed-responsive-item')
        try:
            self.driver.switch_to_frame(iframe)
            # logger.info("The element \' %s \' was clicked." % iframe.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

            # Handle standard drop-down selection box, select at random

    def select(self, id):
        select1 = self.find_element(id)
        try:
            options_list = select1.find_elements_by_tag_name('option')
            del options_list[0]
            s1 = choice(options_list)
            Select(select1).select_by_visible_text(s1.text)
            logger.info("随机选的是：%s" % s1.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

            # execute js

    def execute_js(self, js):
        self.driver.execute_script(js)

    # Simulate enter key
    def enter(self, selector):
        e1 = self.find_element(selector)
        e1.send_keys(Keys.ENTER)
        # Simulate left mouse click

    def leftclick(self, element):
        # e1 = self.find_element(selector)
        ActionChains(self.driver).click(element).perform()

    # Screenshot, saved in the root directory screenshots
    def take_screenshot(self):
        screen_dir = os.path.dirname(os.path.abspath('../..')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = screen_dir + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and saved!")
        except Exception as e:
            logger.error("Failed to take screenshot!", format(e))

    def isElementExist(self, xpath):
        flag = True
        driver = self.driver
        try:
            driver.find_element_by_xpath(xpath)
            return flag
        except:
            flag = False
            return flag