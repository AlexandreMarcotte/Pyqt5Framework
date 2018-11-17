# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
# from pyqtgraph.Qt import QtGui
import os
from functools import partial
# My packages

# from tabs.tab_widget import TabWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.win_name = 'WinName'
        self.win_icon = QtGui.QIcon('./img/polycortex_logo.png')
        self.pos = (0, 0)
        self.size = (1350, 950)
        self.win_intro_message = 'Running the experiment ...'

        self.init_mainwindow()

    def init_mainwindow(self):
        self.setWindowTitle(self.win_name)
        self.setWindowIcon(self.win_icon)
        self.setGeometry(*self.pos, *self.size)
        self.create_menu_bar()
        self.create_toolbar()
        self.statusBar().showMessage(self.win_intro_message)

        # self.main_window = TabWidget(self.gv)
        # self.setCentralWidget(self.main_window)

        self.show()

    def create_menu_bar(self):
        main_menu = self.menuBar()
        self.controlPanel = QMenu('&System Control Panel')

        self.choose_file = self.create_stream_from_file_menu()
        # Connect the btn in the menubar to the choose stream function
        for btn in [self.choose_file]:
            btn.triggered.connect(partial(self.choose_stream, btn))

        main_menu.addMenu(self.controlPanel)


    def create_stream_from_file_menu(self):
        self.from_file = QMenu(title='From file')
        self.from_file.setStatusTip(
            'Stream data from previously saved file...')
        self.controlPanel.addMenu(self.from_file)

        choose_file = QAction('Choose file...')
        choose_file.setStatusTip(
            'Choose the file from which you want to stream data...')
        self.from_file.addAction(choose_file)
        choose_file.name = 'Stream from file'
        return choose_file

    def choose_stream(self, btn):
        """Create a function that will print the name of the menubar
        btn that was selected"""
        print(btn.name)

        if btn.name == 'Stream from file':
            self.choose_streaming_file()

    def choose_streaming_file(self):
        # From: https://pythonspot.com/pyqt5-file-dialog/
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self.main_window, "QFileDialog.getOpenFileName()", "",
            "All Files (*);;Python Files (*.py)", options=options)
        if file_name:
            self.stream_path = file_name

    def create_toolbar(self):
        base_path = os.getcwd()
        path = os.path.join(base_path, 'img/exit.png')
        exitAct = QAction(QIcon(path), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)