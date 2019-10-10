#!/usr/bin/python3

from PyQt5.QtCore import *
from controller import *
from .signalmanager import signalManager
from log import logger


class CApp(QObject):

    def __init__(self):
        super(CApp, self).__init__()
        self.initControllers()

        self.initConnect()

    def initControllers(self):
    	self.calController  = CalController()
    	self.bController  = BController()
    	self.fController  = FController()
    	self.pdfController = PDFController()

    	logger.info(self.calController)
    	logger.info(self.bController)
    	logger.info(self.fController)


    def initConnect(self):
    	signalManager.buttonClicked.connect(self.pdfController.digtailPDF)
    	signalManager.buttonClicked.connect(self.calController.save)
    	pass
