import sys, os, threading
import pyperclip as clipboard

from pynput import keyboard
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

array_list = []
indice = 0

def on_right_list():
    global indice
    if len(array_list) > 0:
        if indice < 0:
            indice = indice * -1
        indice += 1
        indice = indice % len(array_list)
        clipboard.copy(array_list[indice])
        print(array_list[indice])

def on_left_list():
    global indice
    if len(array_list) > 0:
        if indice < 0:
            indice = indice * -1
        indice -= 1
        indice = indice % len(array_list)
        clipboard.copy(array_list[indice])
        print(array_list[indice])

def load_clip():
    with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+d': on_right_list,
        '<ctrl>+<alt>+a': on_left_list}) as h:
        h.join()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("multiclip.ui", self)

        self.setWindowTitle("MultiClip")
        self.setWindowIcon(QtGui.QIcon('icono.ico')) 

        self.ListClipBoard.setEnabled(True)
        self.Refresh.clicked.connect(self.load)
        app.aboutToQuit.connect(self.closeEvent)
        t = threading.Thread(target=load_clip)
        t.start()

    def load(self):
        global array_list
        list = self.ListClipBoard.toPlainText()
        delimiter = '\n'
        array_list = list.split(delimiter)
        clipboard.copy(array_list[indice])
        print(array_list[indice])

    def closeEvent(self):
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    tryicon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("icono.ico"), app)
    tryicon.show()
    widget.show()
    app.exec_()
