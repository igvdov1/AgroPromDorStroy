import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QSizePolicy, QFileDialog
from PyQt6.QtGui import QIcon
from CreateDocumentation import CreateFullDocumentation
from pathlib import Path

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        label = QLabel('Main App', parent=self)


class AdditionalMaterialsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Дополнительные материалы')
        self.setWindowIcon(QIcon(''))
        
        self.setMinimumSize(600, 200)

        layout = QGridLayout()
        self.setLayout(layout)

        self.labels = {}
        self.lineEdits = {}


        #set labels
        self.labels['Объект Капитального'] = QLabel('Объект Капитального строительства')
        self.labels['Застройщик'] = QLabel('Застройщик (технический заказчик, эксплуатирующая организация или региональный оператор)')
        self.labels['Лицо осущ строй'] = QLabel('Лицо, осуществляющее строительство')
        self.labels['Лицо осущ документ'] = QLabel('Лицо осуществляющее подготовку проектной документации')
        self.labels['Представитель застройщика'] = QLabel('Представитель застройщика')
        self.labels['Представитель лица строительства'] = QLabel('Представитель лица, осуществляющего строительство')
        self.labels['Представитель лица строительства2'] = QLabel('Представитель лица, осуществляющего строительство, по вопросам строительного контроля')
        self.labels['Представитель лица документации'] = QLabel('Представитель лица, осуществляющего подготовку проектной документации')
        self.labels['Представитель лица работы'] = QLabel('Представитель лица, выполнившего работы, подлежащие освидетельствованию')
        self.labels['иные представители'] = QLabel('а также иные представители лиц, участвующих в освидетельствовании')
        self.labels['произвели осмотр'] = QLabel('произвели осмотр работ, выполненных')
        self.labels['Работы выполнены пд'] = QLabel('Работы выполнены по проектной документации')
        self.labels['При выполнении применены'] = QLabel('При выполнении применены:')
        self.labels['Предъявлены доки'] = QLabel('Предъявлены документы, подтверждающие соответствие работ предъявляемым к ним требованиям:')
        self.labels['приложения'] = QLabel('Приложения:')
        self.labels['link'] = QLabel('Выберите куда сохранить')


        self.labels['Объект Капитального'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Застройщик'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Лицо осущ строй'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Лицо осущ документ'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Представитель застройщика'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Представитель лица строительства'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Представитель лица строительства2'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Представитель лица документации'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Представитель лица работы'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['иные представители'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Работы выполнены пд'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['При выполнении применены'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['Предъявлены доки'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['приложения'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.labels['link'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            
        #set field to fill
        self.lineEdits['Объект Капитального'] = QLineEdit()
        self.lineEdits['Застройщик'] = QLineEdit()
        self.lineEdits['Лицо осущ строй'] = QLineEdit()
        self.lineEdits['Лицо осущ документ'] = QLineEdit()
        self.lineEdits['Представитель застройщика'] = QLineEdit()
        self.lineEdits['Представитель лица строительства'] = QLineEdit()
        self.lineEdits['Представитель лица строительства2'] = QLineEdit()
        self.lineEdits['Представитель лица документации'] = QLineEdit()
        self.lineEdits['Представитель лица работы'] = QLineEdit()
        self.lineEdits['иные представители'] = QLineEdit()
        self.lineEdits['Работы выполнены пд'] = QLineEdit()
        self.lineEdits['При выполнении применены'] = QLineEdit()
        self.lineEdits['Предъявлены доки'] = QLineEdit()
        self.lineEdits['приложения'] = QLineEdit()
        self.lineEdits['link'] = QPushButton('Поиск')
        self.lineEdits['link'].clicked.connect(self.open_file_dialog)

        layout.addWidget(self.labels['Объект Капитального'],            0, 0, 1, 1)
        layout.addWidget(self.lineEdits['Объект Капитального'],    0, 1, 1, 3)

        layout.addWidget(self.labels['Застройщик'],            1, 0, 1, 1)
        layout.addWidget(self.lineEdits['Застройщик'],    1, 1, 1, 3)

        layout.addWidget(self.labels['Лицо осущ строй'], 2, 0, 1, 1)
        layout.addWidget(self.lineEdits['Лицо осущ строй'], 2, 1, 1, 3)
        
        layout.addWidget(self.labels['Лицо осущ документ'], 3, 0, 1, 1)
        layout.addWidget(self.lineEdits['Лицо осущ документ'], 3, 1, 1, 3)

        layout.addWidget(self.labels['Представитель застройщика'], 4, 0, 1, 1)
        layout.addWidget(self.lineEdits['Представитель застройщика'], 4, 1,1,3)

        layout.addWidget(self.labels['Представитель лица строительства'], 5, 0, 1, 1)
        layout.addWidget(self.lineEdits['Представитель лица строительства'], 5, 1,1,3)

        layout.addWidget(self.labels['Представитель лица строительства2'], 6, 0, 1, 1)
        layout.addWidget(self.lineEdits['Представитель лица строительства2'], 6, 1,1,3)

        layout.addWidget(self.labels['Представитель лица документации'], 7, 0, 1, 1)
        layout.addWidget(self.lineEdits['Представитель лица документации'], 7, 1,1,3)

        layout.addWidget(self.labels['Представитель лица работы'], 8, 0, 1, 1)
        layout.addWidget(self.lineEdits['Представитель лица работы'], 8, 1,1,3)

        layout.addWidget(self.labels['иные представители'], 9, 0, 1, 1)
        layout.addWidget(self.lineEdits['иные представители'], 9, 1, 1, 3)

        layout.addWidget(self.labels['Работы выполнены пд'], 10, 0, 1, 1)
        layout.addWidget(self.lineEdits['Работы выполнены пд'], 10, 1, 1, 3)

        layout.addWidget(self.labels['При выполнении применены'], 11, 0, 1, 1)
        layout.addWidget(self.lineEdits['При выполнении применены'], 11, 1, 1, 3)

        layout.addWidget(self.labels['Предъявлены доки'], 12, 0, 1, 1)
        layout.addWidget(self.lineEdits['Предъявлены доки'], 12, 1, 1, 3)

        layout.addWidget(self.labels['приложения'], 13, 0, 1, 1)
        layout.addWidget(self.lineEdits['приложения'], 13, 1, 1, 3)

        layout.addWidget(self.labels['link'],            19, 0, 1, 1)
        layout.addWidget(self.lineEdits['link'],    19, 1, 1, 3)

        
        button_login = QPushButton('Готово', clicked=self.checkCredential)
        layout.addWidget(button_login,                  20, 3, 1, 1)

        # self.status = QLabel('')
        # self.status.setStyleSheet('font-size: 25px; color: red;')
        # layout.addWidget(self.status, 3, 0, 1, 3)

        # self.connectToDB()
    def open_file_dialog(self):
        self.folder_name = QFileDialog.getExistingDirectory(self, 'Select an awesome directory'
           
            
            r"C:",
           
        )
        # if filenames:
        #     self.file_list_sm.addItems([str(Path(filename))
        #                              for filename in filenames])
    def get_links(self, links):
        self.links = links

    def connectToDB(self):
        pass

    def checkCredential(self):
        CreateFullDocumentation(links_to_smeta= self.links, link = r'C:\Users\igvdo\.vscode\app_for_agroprom\results', additional_materials = self.lineEdits).create_docs()
        print(self.links)
        self.close()
    


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 25px;
        }
        QLineEdit {
            height: 200px;
        }
    ''')
    
    loginWindow = AdditionalMaterialsWindow()
    loginWindow.show()
    
    try:
        sys.exit(app.exec())

    except SystemExit:
        print('Closing Window...')