#coding=utf-8
from selenium import webdriver
import configparser
import os
class Browser(object):
    # Open the browser
    def open_browser(self):
        config = configparser.ConfigParser()
        config.read("../config/config.ini", encoding='UTF-8')
        browser = config.get("browserType", "browserName")
        dir = os.path.abspath('..')
        url = dir + "\\downloadfile\\"
        if browser == "Firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.download.dir', url)
            profile.set_preference('browser.download.folderList', 2)
            profile.set_preference('browser.download.manager.showWhenStarting', False)
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/json')
            # Create a browser driver
            self.driver = webdriver.Firefox(firefox_profile=profile)

        elif browser == "Chrome":
            options = webdriver.ChromeOptions()
            prefs = {'profile.default_content_settings.popups': 0,  # 设置为禁止弹出下载窗口
                     'download.default_directory': url  # 设置为文件下载路径
                     }
            options.add_experimental_option('prefs', prefs)

            self.driver = webdriver.Chrome(chrome_options=options)
        elif browser == "IE":
            self.driver = webdriver.Ie()
        #self.driver.set_window_size(1920, 1080)  # 分辨率
        #self.driver.maximize_window()
        #self.driver.get(url)
        return self.driver

        # Open url site

    def open_url(self, url):
        self.driver.get(url)

        # Close the browser

    def quit_browser(self):
        self.driver.quit()

    # Browser forward operation
    def forward(self):
        self.driver.forward()

    # Browser back action
    def back(self):
        self.driver.back()

    # An implicit wait
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
