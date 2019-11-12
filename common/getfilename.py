#coding=utf-8
import os
class GetFileName():
    '''
    Find out all the filenames of the current url
    '''
    def getfilename(self,url):
        for root,dir,files in os.walk(url):
            return files
