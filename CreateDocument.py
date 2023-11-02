from openpyxl import load_workbook
import os

class CreateDocument():
    def __init__(self, name, type, link, number):
        self.type = type
        self.name = name
        self.number = number
        self.template = load_workbook('template_excel.xlsx')
        self.ws = self.template.active
        self.link = link
    def create_document(self):
        for i in range(1, self.ws.max_row):
            if self.ws[f'B{i}'].value == 'К освидетельствованию предъявлены следующие работы':
                self.ws[f'I{i}'].value = self.name
        os.mkdir(fr'C:\Users\igvdo\.vscode\app_for_agroprom\results\{self.type} №{self.number}')
        self.template.save(fr'C:\Users\igvdo\.vscode\app_for_agroprom\results\{self.type} №{self.number}\{self.type} {self.number}test.xlsx')
