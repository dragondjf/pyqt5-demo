#!/usr/bin/python3

from PyQt5.QtCore import *
from log import logger
from model import StartModel
from app import signalManager

class CalController(QObject):

    def __init__(self):
        super(CalController, self).__init__()
        self.initData()
        self.initConnect()

    def initData(self):
        self.startModel = StartModel()

    def initConnect(self):
        signalManager.buttonClicked.connect(self.save)

    def save(self, name):
        logger.info(type(name))
        self.startModel.setIp("192.168.3.%s" % name)
        self.startModel.setPort(name)

        logger.info(self.startModel)

        t = str(self.startModel)
        logger.info(t)

        with open("%s.json" % name, "wb") as f:
            f.write(bytes(t, "utf-8"))

        signalManager.nameChanged.emit(self.startModel.getIP())
