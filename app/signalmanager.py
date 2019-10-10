#!/usr/bin/python3

from PyQt5.QtCore import *


class SignalManager(QObject):

    resultChanged = pyqtSignal(str)

    buttonClicked = pyqtSignal(str)

    def __init__(self):
        super(SignalManager, self).__init__()

signalManager = SignalManager()
