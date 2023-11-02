import sys
from PyQt6.QtWidgets import QApplication,  QFileDialog, QWidget, QGridLayout, QListWidget, QPushButton, QLabel
from PyQt6.QtCore import QUrl
from pathlib import Path
from CreateDocumentation import CreateFullDocumentation

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        path = r'C:\Users\igvdo\Desktop\documentclass{article}.pdf'
        path_to_excel = r'C:\Users\igvdo\.vscode\app_for_agroprom\names\names.xlsx'
        self.setWindowTitle('Автоматизированное составление документации')
        self.setMinimumSize(200, 300)

        

        layout = QGridLayout()
        self.setLayout(layout)


        
        #set top of file
        self.label_text = QLabel("Добавьте смету и журнал для составления документации", self)
        layout.addWidget(self.label_text, 0, 0)

        # smeta selection
        file_browse = QPushButton('Поиск')
        file_browse.clicked.connect(self.open_file_dialog)

        self.file_list_sm = QListWidget(self)
        
        layout.addWidget(QLabel('Добавьте смету:'), 1, 0)
        layout.addWidget(self.file_list_sm, 2, 0)
        layout.addWidget(file_browse, 3, 0)

        # journal selection
        file_browse = QPushButton('Поиск')
        file_browse.clicked.connect(self.open_file_dialog_journal)

        self.file_list_jr = QListWidget(self)

        layout.addWidget(QLabel('Добавьте журналы по проекту:'), 1, 1)
        layout.addWidget(self.file_list_jr, 2, 1)
        layout.addWidget(file_browse, 3, 1)

        #Smeta generation
        self.button = QPushButton('Сгенерировать смету')
        self.button.setStyleSheet('QPushButton {background-color: green;}')
        self.button.clicked.connect(self.the_button_was_clicked)
        layout.addWidget(self.button, 4, 1)

        #documentation
        document_link = QLabel('Посмотреть инструкцию по работе с приложением', self)
        document_link.setOpenExternalLinks(True)
        document_link.linkActivated.connect(self.link_clicked)
        url = bytearray(QUrl.fromLocalFile(path).toEncoded()).decode()
        text = "<a href={}>Посмотреть инструкцию> </a>".format(url)
        document_link.setText(text)
        layout.addWidget(document_link, 4, 0)

        #change data files
        document_link = QLabel('Изменить имена', self)
        document_link.setOpenExternalLinks(True)
        document_link.linkActivated.connect(self.excel_link)
        url = bytearray(QUrl.fromLocalFile(path_to_excel).toEncoded()).decode()
        text = "<a href={}>изменить имена> </a>".format(url)
        document_link.setText(text)
        layout.addWidget(document_link, 0, 1)

        #add names to names file
        # self.change_names = QLabel('')

        self.show()
    def excel_link(url):
        print('excel open', url)

    def link_clicked(url):
        print("Link clicked:", url)

    def the_button_was_clicked(self):
        items_sm = []
        for x in range(self.file_list_sm.count()):
            items_sm.append(self.file_list_sm.item(x).text())
        CreateFullDocumentation(links_to_smeta= items_sm, link = r'C:\Users\igvdo\.vscode\app_for_agroprom\results').create_docs()
        print(items_sm)

        items_jr = []
        for x in range(self.file_list_jr.count()):
            items_jr.append(self.file_list_jr.item(x).text())
        print(items_jr)
        pass

    def open_file_dialog(self):
        filenames, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Files",
            r"C:",
           
        )
        if filenames:
            self.file_list_sm.addItems([str(Path(filename))
                                     for filename in filenames])
    def open_file_dialog_journal(self):
        filenames, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Files",
            r"C:",
           
        )
        if filenames:
            self.file_list_jr.addItems([str(Path(filename))
                                     for filename in filenames])