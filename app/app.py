#!/usr/bin/python3

from PyQt5.QtCore import *
from controller import *
from view import Calculator
from .signalmanager import signalManager
from log import logger


class CApp(QObject):

    def __init__(self):
        super(CApp, self).__init__()

        self.initView()
        self.initControllers()

        self.initConnect()

    def initView(self):
        self.calculator = Calculator()

    def initControllers(self):
        self.calController  = CalController()
        self.bController  = BController()
        self.fController  = FController()
        self.pdfController = PDFController()

        logger.info(self.calController)
        logger.info(self.bController)
        logger.info(self.fController)


    def initConnect(self):
        pass

    def show(self):
        self.calculator.show()
