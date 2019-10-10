#!/usr/bin/python3

from PyQt5.QtCore import *
from log import logger


class CalController(QObject):

    def __init__(self):
        super(CalController, self).__init__()


    def save(self, name):
        logger.info(type(name))
