#coding=utf-8
from common.browser_engine import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from common.getfilename import GetFileName
import os
import time
'''
This class is the public-address-hidden-amount transfer balance when have no ennough amount
'''
class NoEnoughPublicAddressHiddenAmount():
    def no_enough_public_address_hidden_amount(self):
        '---------------------Log in and check the amount--------------------------------------------'

        #send  TRY login process
        driver=Browser().open_browser()
        #Enter the page
        driver.get('https://wallet.trias.one/')
        driver.find_element_by_xpath('/html/body/div/div/main/div/a[2]/div[1]/h2').click()
        #Gets the file name under the downloadfile folder
        dir = os.path.abspath('..')
        url = dir + "\\downloadfile\\"
        files=GetFileName().getfilename(url)
        # Calculate folder length
        len1 = len(os.listdir(url))
        v1 = url + files[len1 - 2]

        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="fselector"]')))
        #Upload a file
        driver.find_element_by_xpath('//*[@id="fselector"]').send_keys(v1)
        driver.implicitly_wait(5)
        #Enter the password
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(123456789)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[contains(text(),"UNLOCK")]')))
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(Keys.TAB)
        #login
        time.sleep(9)
        for i in range(2):
            try:
                driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/article[1]/div[2]/article/div/div[3]/a').click()
            except:
                pass

        #get public address  balance
        time.sleep(2)
        for i in range(100):
            public_account_balance = driver.find_element_by_xpath(
                '//*[@id="app"]/div/main/div/div[1]/div[2]/div[2]/div[1]/ul/li/span').text
            total_account_balance = driver.find_element_by_xpath(
                '/html/body/div/div/main/div/div/div[2]/div[1]/div[2]/ul/li/span').text
            time.sleep(2)
            if int(total_account_balance) != 0:
                break

        '---------------------------------------------Transaction process-----------------------------------'

        time.sleep(2)
        #Get the name and address of the transfer target account
        splits=files[len1-1].split('--')
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/div[1]/div[1]/input').send_keys(splits[2])

        #send how much amount
        amount=int(public_account_balance)-50
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/section/div[2]/div/input').send_keys(amount)
        time.sleep(2)
        # Click the hide amount button
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/a[2]').click()
        #Click the trade button
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/div[2]/div/a').click()
        time.sleep(3)
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[2]/section/section/div[2]/button[2]').click()
        #Wait for the trade page to change
        try:
            wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                            '/html/body/div/div/main/div/div[1]/article[2]/section/a[2]/span')))
        except:
            print('Transaction timeout')
        time.sleep(3)
        '-------------------------------------------check account----------------------------------------------'
        for i in range(100):
            time.sleep(2)
            #enter the homepage
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/ul/li[1]/a/span').click()
            # click the view account info
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/ul/li[4]/a/span').click()
            # Upload a file
            driver.find_element_by_xpath('//*[@id="fselector"]').send_keys(v1)
            driver.implicitly_wait(5)
            # enter the password
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(123456789)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(),"UNLOCK")]')))
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(Keys.TAB)
            # 登陆
            time.sleep(8)
            try:
                driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/article[1]/div[2]/article/div/div[3]/a').click()
            except:
                print('This element was not found')
            # get account_total_amount again
            time.sleep(2)
            for i in range(100):
                account_total_amount_second = driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/div[2]/div[1]/div[2]/ul/li/span').text
                time.sleep(2)
                if int(account_total_amount_second) != 0:
                    break

            if int(account_total_amount_second) != int(total_account_balance):
                print('The account has been updated. Please check')
                break
        time.sleep(5)
        #login process
        # enter the homepage
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/ul/li[1]/a/span').click()
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/ul/li[3]/a/span').click()
        # Upload a file
        driver.find_element_by_xpath('//*[@id="fselector"]').send_keys(v1)
        driver.implicitly_wait(5)
        # Enter the password
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(123456789)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(),"UNLOCK")]')))
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(Keys.TAB)
        # login
        time.sleep(9)
        for i in range(2):
            try:
                driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/article[1]/div[2]/article/div/div[3]/a').click()
            except:
                pass
        '-----------------------------Second Transaction process-----------------------------------------'

        # Get the name and address of the transfer target account
        splits = files[len1 - 1].split('--')
        driver.find_element_by_xpath(
                '/html/body/div/div/main/div/div/div[3]/article/article[1]/div[1]/div[1]/input').send_keys(splits[2])
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/section/div[2]/div/input').send_keys(50)
        # Click the hide amount button
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/a[2]').click()
        time.sleep(3)
        # Click the trade button
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/div[2]/div/a').click()
        time.sleep(3)
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[2]/section/section/div[2]/button[2]').click()
        time.sleep(5)
        driver.quit()