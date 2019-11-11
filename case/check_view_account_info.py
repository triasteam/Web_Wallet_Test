 #coding=utf-8
from common.browser_engine import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from common.getfilename import GetFileName
from common.getconf import GetConf
import os
import time
class CheckViewAccountInfo():
     def check_view_account_info(self):
        # getconfig coin and hidden coin
        coin=GetConf().get_coins('theCoins','coin')
        hidden_coin=GetConf().get_coins('theCoins','hidden_coin')
        account_all_coins=int(coin)+int(hidden_coin)

        # The login process for send TRY
        driver = Browser().open_browser()
        # Enter the page
        driver.get('https://wallet.trias.one/')
        time.sleep(2)
        for i in range(100):
            #enter the homepage
            driver.find_element_by_xpath(
                '/html/body/div/div/div[2]/div[2]/div/ul/li[1]/a/span').click()
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/div/ul/li[4]/a/span').click()
            # Gets the file name under the downloadfile folder
            dir = os.path.abspath('..')
            url = dir + "\\downloadfile\\"
            files = GetFileName().getfilename(url)
            # Calculate folder length
            len1 = len(os.listdir(url))
            v1 = url + files[len1 - 2]
            wait = WebDriverWait(driver, 60)
            wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="fselector"]')))
            # Upload a file
            driver.find_element_by_xpath('//*[@id="fselector"]').send_keys(v1)
            driver.implicitly_wait(5)
            # Enter the password
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(123456789)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(),"UNLOCK")]')))
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(Keys.TAB)
            # to login
            time.sleep(8)
            try:
                driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/article[1]/div[2]/article/div/div[3]/a').click()
            except:
                driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/article[1]/div[2]/article/div/div[3]/a').click()
            for i in range(40):
                # get account total balance
                time.sleep(1)
                account_total_balance = driver.find_element_by_xpath(
                    '//*[@id="app"]/div/main/div/div/div[2]/div[1]/div[2]/ul/li/span').text
                if int(account_total_balance) !=0:
                    break
            if int(account_total_balance) == int(account_all_coins):
                break
        time.sleep(3)
        driver.quit()