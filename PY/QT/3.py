import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from rc import *


class mypy(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mypy, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mp = mypy()
    mp.show()
    sys.exit(app.exec_())