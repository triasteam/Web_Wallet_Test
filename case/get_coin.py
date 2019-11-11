#coding=utf-8
from common.browser_engine import Browser
from common.basepage import BasePage
from common.getfilename import GetFileName
from common.getconf import GetConf
import time
import os
'''
the class is for get TRY coin
'''
class GetCoin():
    def getcoin(self):
        #get config TRY coins
        coin=GetConf().get_coins('theCoins','coin')

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
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="change_margin_1"]/input').send_keys(w1)
        time.sleep(3)
        '''
        creat  TRY coin
        '''
        for i in range(int(coin)//100):
            bs.find_element('classname<=>content-form-signup').click()
            time.sleep(1)
        driver.quit()