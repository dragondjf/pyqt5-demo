#-*- coding: UTF-8 -*- 
#!/usr/bin/python
import json
from reportbro import Report, ReportBroError
import fire
import os

class PDFReporter(object):

    def tpce(self, template, data, output):
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

if __name__ == '__main__':
    fire.Fire(PDFReporter)
