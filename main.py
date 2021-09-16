from PyQt5 import QtWidgets
from mainwindow import MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())