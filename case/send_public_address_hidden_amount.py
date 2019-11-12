#coding=utf-8
from common.browser_engine import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from common.getfilename import GetFileName
import random
import os
import time
from common.writeexcel import WriteExcel
class SendPublicAddressHiddenAmount():
    '''
    This class is public-address hidden amount transfer
    '''
    def send_public_address_hidden_amount(self):
        driver=Browser().open_browser()
        #Enter the page
        driver.get('https://wallet.trias.one/')
        driver.find_element_by_xpath('/html/body/div/div/main/div/a[2]/div[1]/h2').click()
        #gets all filenames in the downloadfile
        dir = os.path.abspath('..')
        url = dir + "\\downloadfile\\"
        files=GetFileName().getfilename(url)
        # 计算文件夹长度
        len1 = len(os.listdir(url))
        v1 = url + files[len1 - 2]

        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="fselector"]')))
        #Upload a file
        driver.find_element_by_xpath('//*[@id="fselector"]').send_keys(v1)
        driver.implicitly_wait(5)
        #enter the password
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(123456789)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[contains(text(),"UNLOCK")]')))
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(Keys.TAB)
        #to login
        time.sleep(8)
        try:
            driver.find_element_by_xpath(
                '/html/body/div/div/main/div/div/article[1]/div[2]/article/div/div[3]/a').click()
        except:
            print('This element was not found')
        #Transaction process
        #Get account amount information
        time.sleep(2)
        for i in range(50):
            time.sleep(1)
            account_total_amount=driver.find_element_by_xpath(
                '/html/body/div/div/main/div/div/div[2]/div[1]/div[2]/ul/li/span').text
            public_address_amount=driver.find_element_by_xpath(
                '/html/body/div/div/main/div/div/div[2]/div[2]/div[1]/ul/li/span').text
            public_address_hideen_amount=driver.find_element_by_xpath(
                '/html/body/div/div/main/div/div/div[2]/div[2]/div[2]/ul/li/span').text
            private_address_amount=driver.find_element_by_xpath(
                '/html/body/div/div/main/div/div/div[2]/div[2]/div[3]/ul/li/span').text
            private_address_hidden_amount=driver.find_element_by_xpath(
                '/html/body/div/div/main/div/div/div[2]/div[2]/div[4]/ul/li/span').text
            if int(account_total_amount) != 0:
                break
        #Get the name and address of the transfer target account
        splits=files[len1-1].split('--')
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/div[1]/div[1]/input').send_keys(splits[2])
        #random transfer amount
        rand=random.randint(1,150)
        driver.find_element_by_xpath(
            '/html/body/div/div/main/div/div/div[3]/article/article[1]/section/div[2]/div/input').send_keys(rand)
        #Click the hide amount button
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
        time.sleep(2)
        for i in range(100):
            time.sleep(2)
            #enter the homepage
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/ul/li[1]/a/span').click()
            #click the view account info
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/ul/li[4]/a/span').click()
            #Upload a file
            driver.find_element_by_xpath('//*[@id="fselector"]').send_keys(v1)
            driver.implicitly_wait(5)
            #enter the password
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(123456789)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[contains(text(),"UNLOCK")]')))
            driver.find_element_by_xpath(
                '//*[@id="app"]/div/main/div/div/article[1]/div[2]/article/div/div[2]/input').send_keys(Keys.TAB)
            #登陆
            time.sleep(8)
            try:
                driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/article[1]/div[2]/article/div/div[3]/a').click()
            except:
                print('This element was not found')
            #get account_total_amount again
            time.sleep(2)
            for i in range(50):
                account_total_amount_second=driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/div[2]/div[1]/div[2]/ul/li/span').text
                time.sleep(2)
                if int(account_total_amount_second) !=0:
                    break
            if int(account_total_amount_second) != int(account_total_amount):
                #Record the account amount and store it in XLS
                public_address_amount2 = driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/div[2]/div[2]/div[1]/ul/li/span').text
                public_address_hideen_amount2 = driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/div[2]/div[2]/div[2]/ul/li/span').text
                private_address_amount2 = driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/div[2]/div[2]/div[3]/ul/li/span').text
                private_address_hidden_amount2 = driver.find_element_by_xpath(
                    '/html/body/div/div/main/div/div/div[2]/div[2]/div[4]/ul/li/span').text
                flag=True
                if (int(public_address_amount)+int(public_address_hideen_amount)-rand)!=(int(public_address_amount2)+int(public_address_hideen_amount2)):
                    flag=False
                WriteExcel().write_excel_xls_append([public_address_amount,
                                          public_address_hideen_amount,
                                          private_address_amount,
                                          private_address_hidden_amount,
                                          'send public adress hidden amount: '+str(rand)+'TRY',
                                          public_address_amount2,
                                          public_address_hideen_amount2,
                                          private_address_amount2,
                                          private_address_hidden_amount2,
                                          flag])
                print('The account has been updated. Please check')
                break
        time.sleep(5)
        driver.quit()