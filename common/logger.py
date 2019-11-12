#coding=utf-8
import logging
import time
class Logger(object):

    def __init__(self):
        'specify file path to save log, log level, and call file to save log to specified file'

        # create a logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # Create a handler to write to the log file
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

        log_dir = '../logs/'
        log_name = log_dir + rq + '.log'
        fh = logging.FileHandler(log_name)

        fh.setLevel(logging.INFO)

        # Create another handler for the output to the console
        ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
        # Define the output format of the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        # self.logger.setLevel(level=logging.INFO)
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # log_dir = '../logs/'
        # log_name = log_dir + rq + '.log'
        # handler = logging.FileHandler(log_name)
        # handler.setLevel(logging.INFO)
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        #
        # console = logging.StreamHandler()
        # console.setLevel(logging.INFO)
        #
        # self.logger.addHandler(handler)
        # self.logger.addHandler(console)

    def getlog(self):
        return self.logger