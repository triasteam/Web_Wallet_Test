#coding=utf-8
from common.browser_engine import Browser
from common.basepage import BasePage
from common.getfilename import GetFileName
from common.getconf import GetConf
import time
import os
class GetHiddenCoin():
    '''
    the class is for creat hidden TRY coin
    '''
    @staticmethod
    def get_hidden_coin():
        #get config TRY coins
        hidden_coin=GetConf().get_coins('theCoins','hidden_coin')

        driver=Browser().open_browser()
        bs=BasePage(driver)
        driver.get('https://wallet.trias.one/api/getCoinbase/')
        #Gets the file name under the downloadfile folder
        dir = os.path.abspath('..')
        url = dir + "\\downloadfile\\"
        files=GetFileName().getfilename(url)
        #Calculate folder length
        len1=len(os.listdir(url))
        w=files[len1-2]
        w1=w.split('--')[2]
        #Check the private address
        time.sleep(10)
        driver.find_element_by_name('user').send_keys(w1)

        element0 = driver.find_elements_by_xpath("//*[@id='send_type_select']/label")
        for ele0 in element0:
            if ele0.is_displayed():
                ele0.click()
        time.sleep(3)
        '''
        creat  hidden TRY coin
        '''
        for i in range(int(hidden_coin)//100):
            bs.find_element('classname<=>content-form-signup').click()
            time.sleep(1)
        driver.quit()