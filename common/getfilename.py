#coding=utf-8
import os
'''
Find out all the filenames of the current url
'''
class GetFileName():
    def getfilename(self,url):
        for root,dir,files in os.walk(url):
            return files
