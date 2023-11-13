import sys
from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
from GetNamesFromExcel import GetNamesFromExcel
from CreateDocument import CreateDocument
from CreateDocumentation import CreateFullDocumentation
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
