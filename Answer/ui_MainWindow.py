# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setBaseSize(QtCore.QSize(900, 500))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 430))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(670, 100))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.gridLayout.addWidget(self.groupBox_5, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 320))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chk_A = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_A.setObjectName("chk_A")
        self.verticalLayout.addWidget(self.chk_A)
        self.chk_B = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_B.setObjectName("chk_B")
        self.verticalLayout.addWidget(self.chk_B)
        self.chk_D = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_D.setObjectName("chk_D")
        self.verticalLayout.addWidget(self.chk_D)
        self.chk_C = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_C.setObjectName("chk_C")
        self.verticalLayout.addWidget(self.chk_C)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(190, 60))
        self.groupBox_3.setMaximumSize(QtCore.QSize(190, 60))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rab_dan = QtWidgets.QRadioButton(self.groupBox_4)
        self.rab_dan.setObjectName("rab_dan")
        self.horizontalLayout_3.addWidget(self.rab_dan)
        self.rab_duo = QtWidgets.QRadioButton(self.groupBox_4)
        self.rab_duo.setObjectName("rab_duo")
        self.horizontalLayout_3.addWidget(self.rab_duo)
        self.rab_pan = QtWidgets.QRadioButton(self.groupBox_4)
        self.rab_pan.setObjectName("rab_pan")
        self.horizontalLayout_3.addWidget(self.rab_pan)
        self.gridLayout.addWidget(self.groupBox_4, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actOpen_File = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/open.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actOpen_File.setIcon(icon)
        self.actOpen_File.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actOpen_File.setObjectName("actOpen_File")
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon1)
        self.actQuit.setObjectName("actQuit")
        self.mainToolBar.addAction(self.actOpen_File)
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "题号"))
        self.groupBox_5.setTitle(_translate("MainWindow", "标题"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">说明:1,先点击打开文件,选择加载的文件,(使用提供的修改后文件)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">2.再点击类型里面的单选或者多选或者判断</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">3.在题号里面选择题目</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">4.点击查看答案可以查看当前题目的答案</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "选项"))
        self.chk_A.setText(_translate("MainWindow", "CheckBox"))
        self.chk_B.setText(_translate("MainWindow", "CheckBox"))
        self.chk_D.setText(_translate("MainWindow", "CheckBox"))
        self.chk_C.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox.setText(_translate("MainWindow", "查看答案"))
        self.groupBox_4.setTitle(_translate("MainWindow", "类型"))
        self.rab_dan.setText(_translate("MainWindow", "单选题"))
        self.rab_duo.setText(_translate("MainWindow", "多选题"))
        self.rab_pan.setText(_translate("MainWindow", "判断题"))
        self.actOpen_File.setText(_translate("MainWindow", "打开文件"))
        self.actQuit.setText(_translate("MainWindow", "退出"))
import res_rc
