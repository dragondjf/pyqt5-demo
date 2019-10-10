#!/usr/bin/python3

from PyQt5.QtCore import *
import os
import json
from reportbro import Report, ReportBroError


class PDFController(QObject):

    def __init__(self):
        super(PDFController, self).__init__()
        self.template = os.sep.join([os.getcwd(), "controller", "tpce-simple.json"])
        self.data = os.sep.join([os.getcwd(), "controller", "data.json"])

    def digtailPDF(self, name):
    	self.pdf(self.template, self.data, "%s.pdf" % name)

    def pdf(self, template, data, output):
        if os.path.exists(template):
            with open(template, "rb") as f:
                report_definition = json.loads(f.read())
        else:
            report_definition = json.loads(template)

        if os.path.exists(data):
            with open(data, "rb") as f:
                data = json.loads(f.read())
        else:
            data = json.loads(data)

        additional_fonts = [dict(value='firefly',filename='fireflysung.ttf')]
        is_test_data = {}
        report = Report(report_definition, data, is_test_data, additional_fonts=additional_fonts)
        report_file = report.generate_pdf(filename=output, add_watermark=False)
