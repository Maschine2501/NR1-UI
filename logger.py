# Copyright (c) 2021 Rene Juen
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import logging
from logging.handlers import RotatingFileHandler

class Logger:

    def __init__(self, name, debug):
        self.name = name
        self.level = debug
        if self.level:
            self.loglevelflag = logging.DEBUG
        else:
            self.loglevelflag = logging.INFO
        self._config()

    def start(self):
        pass

    def stop(self):
        pass

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def _config(self):
        self.logger = logging.getLogger(self.name)
        filename = '/var/log/nr1ui.log'
        hdlr = RotatingFileHandler(filename, mode='a', maxBytes=5*1024*1024,backupCount=2, encoding=None, delay=0)
        formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(self.loglevelflag)