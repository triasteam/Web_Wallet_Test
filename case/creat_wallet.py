#coding=utf-8
from common.browser_engine import Browser
import time
import os
class CreatWallet():
    '''
    the class is for creat wallet
    '''
    @staticmethod
    def creat_wallet():
        driver=Browser().open_browser()
        #Enter the homepage
        driver.get('https://wallet.trias.one/')
        time.sleep(3)
        #Click create wallet
        driver.find_element_by_xpath('/html/body/div/div/main/div/a[1]/div[1]').click()
        driver.implicitly_wait(2)
        #Enter password and click ok to create
        driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/article[1]/section/div[2]/input').send_keys('123456789')
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/article[1]/section/a').click()
        driver.implicitly_wait(5)
        #Click to download the file and confirm that it has been downloaded
        driver.find_element_by_xpath('/html/body/div/div/main/div/div/article[2]/section/a/span').click()
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div/div/main/div/div/article[2]/section/p/a').click()
        time.sleep(3)
        driver.quit()