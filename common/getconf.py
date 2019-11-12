#coding=utf-8
import configparser
import os
import codecs
dir = os.path.abspath('..')
url=dir + "\\config\\config.ini"
class GetConf():
    def __init__(self):
        fd = open(url)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(url, "w")
            file.write(data)
            file.close()
        fd.close()
        self.config = configparser.ConfigParser()
        self.config.read(url)

    #get config name theCoins
    def get_coins(self,key,name):
        value=self.config.get(key,name)
        return value
