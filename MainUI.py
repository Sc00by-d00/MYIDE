# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\OM\Desktop\hello.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


# from qtpy.QtCore import Qt

class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 665)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 460))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.ProblemTab = QtWidgets.QTabWidget(self.splitter)
        self.ProblemTab.setObjectName("ProblemTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.ProblemList = QtWebEngineWidgets.QWebEngineView(self.tab)
        self.ProblemList.setObjectName("ProblemList")
        self.gridLayout.addWidget(self.ProblemList, 0, 0, 1, 1)
        self.ProblemTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ProblemStatement = QtWebEngineWidgets.QWebEngineView(self.tab_2)
        self.ProblemStatement.setObjectName("ProblemStatement")
        self.gridLayout_2.addWidget(self.ProblemStatement, 0, 0, 1, 1)
        self.ProblemTab.addTab(self.tab_2, "")
        self.CodeTab = QtWidgets.QTabWidget(self.splitter)
        self.CodeTab.setObjectName("CodeTab")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_3.addWidget(self.textEdit_5, 0, 0, 1, 1)
        self.CodeTab.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_4.addWidget(self.textEdit_6, 0, 0, 1, 1)
        self.CodeTab.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.splitter)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InputTC = QtWidgets.QTextEdit(self.frame)
        self.InputTC.setObjectName("InputTC")
        self.horizontalLayout.addWidget(self.InputTC)
        self.OutputTC = QtWidgets.QTextEdit(self.frame)
        self.OutputTC.setObjectName("OutputTC")
        self.horizontalLayout.addWidget(self.OutputTC)
        self.Verdict = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Verdict.sizePolicy().hasHeightForWidth())
        self.Verdict.setSizePolicy(sizePolicy)
        self.Verdict.setMinimumSize(QtCore.QSize(100, 0))
        self.Verdict.setAlignment(QtCore.Qt.AlignCenter)
        self.Verdict.setObjectName("Verdict")
        self.horizontalLayout.addWidget(self.Verdict)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Language = QtWidgets.QComboBox(self.frame_2)
        self.Language.setObjectName("Language")
        self.Language.addItem("")
        self.Language.addItem("")
        self.Language.addItem("")
        self.Language.addItem("")
        self.verticalLayout_2.addWidget(self.Language)
        self.Platform = QtWidgets.QComboBox(self.frame_2)
        self.Platform.setObjectName("Platform")
        self.Platform.addItem("")
        self.Platform.addItem("")
        self.verticalLayout_2.addWidget(self.Platform)
        self.Tag = QtWidgets.QLineEdit(self.frame_2)
        self.Tag.setObjectName("Tag")
        self.verticalLayout_2.addWidget(self.Tag)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(225, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Compile = QtWidgets.QPushButton(self.frame_3)
        self.Compile.setObjectName("Compile")
        self.Compile.setMinimumSize(QtCore.QSize(100, 25))
        self.verticalLayout_3.addWidget(self.Compile)
        self.Submit = QtWidgets.QPushButton(self.frame_3)
        self.Submit.setObjectName("Submit")
        self.Submit.setMinimumSize(QtCore.QSize(100, 25))
        self.verticalLayout_3.addWidget(self.Submit)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTemplates = QtWidgets.QMenu(self.menubar)
        self.menuTemplates.setObjectName("menuTemplates")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionManage = QtWidgets.QAction(MainWindow)
        self.actionManage.setObjectName("actionManage")
        self.actionDownload = QtWidgets.QAction(MainWindow)
        self.actionDownload.setObjectName("actionDownload")
        self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        self.actionLight_Theme = QtWidgets.QAction(MainWindow)
        self.actionLight_Theme.setObjectName("actionLight_Theme")
        self.actionDark_Theme = QtWidgets.QAction(MainWindow)
        self.actionDark_Theme.setObjectName("actionDark_Theme")
        self.actionCustom_Theme = QtWidgets.QAction(MainWindow)
        self.actionCustom_Theme.setObjectName("actionCustom_Theme")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuTemplates.addAction(self.actionManage)
        self.menuTemplates.addAction(self.actionDownload)
        self.menuPreferences.addAction(self.actionFont)
        self.menuPreferences.addAction(self.actionLight_Theme)
        self.menuPreferences.addAction(self.actionDark_Theme)
        self.menuPreferences.addAction(self.actionCustom_Theme)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTemplates.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())

        self.retranslateUi(MainWindow)
        self.ProblemTab.setCurrentIndex(0)
        self.CodeTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ProblemTab.setTabText(self.ProblemTab.indexOf(self.tab), _translate("MainWindow", "Problem List"))
        self.ProblemTab.setTabText(self.ProblemTab.indexOf(self.tab_2), _translate("MainWindow", "Problem Statement"))
        self.CodeTab.setTabText(self.CodeTab.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.CodeTab.setTabText(self.CodeTab.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.Verdict.setText(_translate("MainWindow", "Verdict"))
        self.Language.setItemText(0, _translate("MainWindow", "C"))
        self.Language.setItemText(1, _translate("MainWindow", "C++"))
        self.Language.setItemText(2, _translate("MainWindow", "Java"))
        self.Language.setItemText(3, _translate("MainWindow", "Python"))
        self.Platform.setItemText(0, _translate("MainWindow", "CodeChef"))
        self.Platform.setItemText(1, _translate("MainWindow", "Codeforces"))
        self.Platform.setItemData(0,
                                  "https://www.codechef.com/")  # The website is added for Platform selection choicebox as itemdata
        self.Platform.setItemData(1, "https://codeforces.com/")
        self.Tag.setPlaceholderText(_translate("MainWindow", "Enter Contest Tag"))
        self.Compile.setText(_translate("MainWindow", "Compile and Test"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTemplates.setTitle(_translate("MainWindow", "Templates"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionManage.setText(_translate("MainWindow", "Manage"))
        self.actionDownload.setText(_translate("MainWindow", "Download"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionLight_Theme.setText(_translate("MainWindow", "Light Theme"))
        self.actionDark_Theme.setText(_translate("MainWindow", "Dark Theme"))
        self.actionCustom_Theme.setText(_translate("MainWindow", "Custom Theme"))
        # self.Platform.activated.connect(self.loadProblemList)
        self.Platform.activated.connect(self.loadProblemList)
        '''When the choicebox option get changes the above line switches the platform accordingly from CF to CC or vice versa'''

        self.Tag.returnPressed.connect(lambda: self.loadProblemList(1))  # press enter after typing contest tag
        self.connectActions()  # connect actions to the menu
        self.setTheme("light")  # default theme is light
        self.loadProblemList(0)  # opens CodeChef by default
        self.KeyboardShortcuts()  # responsible for calling keyboard shortcuts

    def KeyboardShortcuts(self):
        '''All methods responsible for the working of keyboard shortcuts are called in this method'''
        self.Tag.returnPressed.connect(
            self.loadProblemList)  # opens desired page when pressed enter after entering tag in Tag lineEdit
        self.RefreshPage()  # Refreshes current page when F5 is pressed
        self.CompileAndTestKeyboardShortcut()  # calls method CompileAndTest() when F9 is pressed
        self.SubmitKeyboardShortcut()  # calls method SubmitMethod() when F10 is pressed

    def RefreshPage(self):
        '''Refreshes the current page of the user when the user presses F5 key'''
        # create shortcut
        self.refreshProblemList = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F5), self.ProblemList)

        # connect its 'activated' signal to your function loadProblemList
        self.refreshProblemList.activated.connect(lambda: self.loadProblemList(
            0))  # argument in loadProblemList is totally useless but magically it resolves the runtime error

        # create shortcut
        self.refreshProblemStatement = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F5), self.ProblemStatement)

        # connect its 'activated' signal to your function loadProblemList
        self.refreshProblemStatement.activated.connect(self.loadProblemStatement)

    def loadProblemList(self, index):
        '''This function is responsible for fetching tag data and opening the respective website contest problem list in
        ProblemList web viewer.'''
        index = self.Platform.currentIndex()
        if index == 0:
            self.ProblemList.load(QtCore.QUrl(self.Platform.itemData(index) + self.Tag.text().upper()))
        else:
            self.ProblemList.load(QtCore.QUrl(self.Platform.itemData(index) + (
                'contest/' if self.Tag.text() != '' else '') + self.Tag.text().upper()))  # atleast open the homepage

    def loadProblemStatement(self):
        '''Loads problem statement selected from Problem List
        filhaal ye kuch ni krta h'''
        print('ProblemStatement')

    def CompileAndTestKeyboardShortcut(self):
        '''Keyboard Shortcut for Compile and Test button via F9 key'''
        # create shortcut
        self.compileAndTest = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F9), self.CodeTab)

        # connect its 'activated' signal to your function loadProblemList
        self.compileAndTest.activated.connect(self.CompileAndTest)

    def CompileAndTest(self):
        '''Gets data from active textEdit and stores into ProblemTag.langext in specified folder then compiles and runs that
        with specified input and produces output. Right now it just reads text and stores into a file. nothing else'''
        print(self.CodeTab.currentIndex())
        print(self.CodeTab.currentWidget())
        # print(self.CodeTab.

    def SubmitKeyboardShortcut(self):
        '''Keyboard Shortcut for Submit button via F10 key'''
        # create shortcut
        self.submit = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F10), self.CodeTab)

        # connect its 'activated' signal to your function loadProblemList
        self.submit.activated.connect(self.SubmitMethod)

    def SubmitMethod(self):
        '''Submits the compiled code to the website
        filhaal ye kuch ni krta h'''
        print('submit')

    def connectActions(self):
        '''Connects all the actions to the menu eg themes, file -> save, open etc'''
        self.actionDark_Theme.triggered.connect(lambda: self.setTheme("dark"))
        self.actionLight_Theme.triggered.connect(lambda: self.setTheme("light"))

    def setTheme(self, theme_name):
        '''sets the theme according to the arguement provided'''
        MainWindow.setStyleSheet(open(theme_name + ".qss", "r").read())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

