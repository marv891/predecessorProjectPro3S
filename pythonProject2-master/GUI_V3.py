# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\louis\OneDrive\Documents\systemeTechnik\2021-2022\Pro4S\Qtdesigner\GUI_V2_16.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import traceback
from PyQt5.QtCore import QMutex, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect
import FeatureControle
from datetime import datetime
import x_y_bverHS21_Code_WassmerSpeckert2 as Off
from V2_sign_in_Ui import Ui_Dialog

cnt = 0


class Ui_MainWindow(object):
    def __init__(self):
        self._mutex = QMutex()
        self.flag = True

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1198, 843)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, 8, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Snapshot = QtWidgets.QPushButton(self.centralwidget)
        self.Snapshot.setObjectName("Snapshot")
        self.horizontalLayout.addWidget(self.Snapshot)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.ZoomInButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZoomInButton.setMaximumSize(QtCore.QSize(67, 16777215))
        self.ZoomInButton.setObjectName("ZoomInButton")
        self.horizontalLayout.addWidget(self.ZoomInButton)

        self.ZoomOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZoomOutButton.setMaximumSize(QtCore.QSize(67, 16777215))
        self.ZoomOutButton.setObjectName("ZoomOutButton")
        self.horizontalLayout.addWidget(self.ZoomOutButton)

        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setObjectName("time")
        self.horizontalLayout.addWidget(self.time)

        self.Timedisplay = QtWidgets.QLabel(self.centralwidget)
        self.Timedisplay.setObjectName("Timedisplay")
        self.horizontalLayout.addWidget(self.Timedisplay)

        self.Frames = QtWidgets.QLabel(self.centralwidget)
        self.Frames.setMinimumSize(QtCore.QSize(55, 16))
        self.Frames.setObjectName("Frames")
        self.horizontalLayout.addWidget(self.Frames, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.Framenumbers = QtWidgets.QLabel(self.centralwidget)
        self.Framenumbers.setMinimumSize(QtCore.QSize(50, 35))
        self.Framenumbers.setObjectName("Framenumbers")
        self.horizontalLayout.addWidget(self.Framenumbers, 0, QtCore.Qt.AlignRight)

        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.VideoStream = QtWidgets.QLabel(self.groupBox)
        self.VideoStream.setGeometry(QtCore.QRect(10, 20, 811, 691))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoStream.sizePolicy().hasHeightForWidth())
        self.VideoStream.setSizePolicy(sizePolicy)
        self.VideoStream.setMinimumSize(QtCore.QSize(782, 647))
        self.VideoStream.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.VideoStream.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.VideoStream.setMouseTracking(True)
        self.VideoStream.setFrameShape(QtWidgets.QFrame.Box)
        self.VideoStream.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.VideoStream.setLineWidth(1)
        self.VideoStream.setMidLineWidth(1)
        self.VideoStream.setText("")
        # self.VideoStream.setPixmap(QtGui.QPixmap("20220113_000_Anwesend_2.jpg"))
        self.VideoStream.setScaledContents(False)
        self.VideoStream.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.VideoStream.setObjectName("VideoStream")
        self.CoordinatesDisplay = QtWidgets.QLabel(self.groupBox)
        self.CoordinatesDisplay.setGeometry(QtCore.QRect(20, 540, 171, 161))
        self.CoordinatesDisplay.setMinimumSize(QtCore.QSize(0, 40))
        self.CoordinatesDisplay.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CoordinatesDisplay.setText("")
        self.CoordinatesDisplay.setPixmap(QtGui.QPixmap("bilder/koordinaten_system_final.png"))
        self.CoordinatesDisplay.setScaledContents(True)
        self.CoordinatesDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.CoordinatesDisplay.setObjectName("CoordinatesDisplay")
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.parameter_Box = QtWidgets.QTabWidget(self.centralwidget)
        self.parameter_Box.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameter_Box.sizePolicy().hasHeightForWidth())
        self.parameter_Box.setSizePolicy(sizePolicy)
        self.parameter_Box.setMinimumSize(QtCore.QSize(318, 723))
        self.parameter_Box.setMaximumSize(QtCore.QSize(328, 718))
        self.parameter_Box.setAutoFillBackground(False)
        self.parameter_Box.setElideMode(QtCore.Qt.ElideNone)
        self.parameter_Box.setObjectName("parameter_Box")
        self.Beginner_Parameter = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Beginner_Parameter.sizePolicy().hasHeightForWidth())
        self.Beginner_Parameter.setSizePolicy(sizePolicy)
        self.Beginner_Parameter.setMinimumSize(QtCore.QSize(400, 1000))
        self.Beginner_Parameter.setMaximumSize(QtCore.QSize(1000, 1027))
        self.Beginner_Parameter.setObjectName("Beginner_Parameter")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Beginner_Parameter)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 311, 411))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.StandardLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.StandardLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.StandardLayout.setContentsMargins(8, 8, 8, 8)
        self.StandardLayout.setSpacing(10)
        self.StandardLayout.setObjectName("StandardLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.StandardLayout.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.StandardLayout.addWidget(self.line)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Auto = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.Auto.setObjectName("Auto")
        self.horizontalLayout_7.addWidget(self.Auto)
        self.Manual = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.Manual.setObjectName("Manual")
        self.horizontalLayout_7.addWidget(self.Manual)
        self.StandardLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)

        self.Exposure_Time = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.Exposure_Time.setAcceptDrops(False)
        self.Exposure_Time.setMaximum(40000)
        self.Exposure_Time.setOrientation(QtCore.Qt.Horizontal)
        self.Exposure_Time.setObjectName("Exposure_Time")
        self.horizontalLayout_3.addWidget(self.Exposure_Time)
        self.Exposure_Box = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.Exposure_Box.setMaximum(40000)
        self.Exposure_Box.setObjectName("Exposure_Box")
        self.horizontalLayout_3.addWidget(self.Exposure_Box)

        self.StandardLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)

        self.Gain = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.Gain.setMaximum(250)
        self.Gain.setOrientation(QtCore.Qt.Horizontal)
        self.Gain.setObjectName("Gain")
        self.horizontalLayout_4.addWidget(self.Gain)
        self.Gain_Box = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.Gain_Box.setMaximum(250)
        self.Gain_Box.setObjectName("Gain_Box")
        self.horizontalLayout_4.addWidget(self.Gain_Box)

        self.StandardLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)

        self.TargetBrightnessslider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.TargetBrightnessslider.setMaximum(100)
        self.TargetBrightnessslider.setOrientation(QtCore.Qt.Horizontal)
        self.TargetBrightnessslider.setObjectName("TargetBrightnessslider")
        self.horizontalLayout_5.addWidget(self.TargetBrightnessslider)
        self.TargetBrightnessbox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.TargetBrightnessbox.setMaximum(100)
        self.TargetBrightnessbox.setObjectName("TargetBrightnessbox")
        self.horizontalLayout_5.addWidget(self.TargetBrightnessbox)

        self.StandardLayout.addLayout(self.horizontalLayout_5)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.StandardLayout.addWidget(self.line_3)

        self.Coordinates = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.Coordinates.setObjectName("Coordinates")
        self.StandardLayout.addWidget(self.Coordinates)

        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.StandardLayout.addWidget(self.line_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.StandardLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)

        self.TAxisReadOut = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TAxisReadOut.sizePolicy().hasHeightForWidth())
        self.TAxisReadOut.setSizePolicy(sizePolicy)
        self.TAxisReadOut.setMaximumSize(QtCore.QSize(160, 28))
        self.TAxisReadOut.setObjectName("TAxisReadOut")
        self.horizontalLayout_8.addWidget(self.TAxisReadOut, 0, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.StandardLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.UAxisReadOut = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UAxisReadOut.sizePolicy().hasHeightForWidth())
        self.UAxisReadOut.setSizePolicy(sizePolicy)
        self.UAxisReadOut.setMaximumSize(QtCore.QSize(160, 28))
        self.UAxisReadOut.setObjectName("UAxisReadOut")
        self.horizontalLayout_9.addWidget(self.UAxisReadOut)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.StandardLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ReadOffsetButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ReadOffsetButton.setObjectName("ReadOffsetButton")
        self.horizontalLayout_11.addWidget(self.ReadOffsetButton)
        self.StandardLayout.addLayout(self.horizontalLayout_11)
        self.DescriptionStandard = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionStandard.sizePolicy().hasHeightForWidth())
        self.DescriptionStandard.setSizePolicy(sizePolicy)
        self.DescriptionStandard.setObjectName("DescriptionStandard")
        self.StandardLayout.addWidget(self.DescriptionStandard)
        self.parameter_Box.addTab(self.Beginner_Parameter, "")
        self.Parameter_BoxPage2 = QtWidgets.QWidget()
        self.Parameter_BoxPage2.setObjectName("Parameter_BoxPage2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Parameter_BoxPage2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 311, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Gurulayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Gurulayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Gurulayout.setContentsMargins(8, 8, 8, 8)
        self.Gurulayout.setSpacing(7)
        self.Gurulayout.setObjectName("Gurulayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.SignInButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.SignInButton.setObjectName("SignInButton")
        self.horizontalLayout_12.addWidget(self.SignInButton)
        self.LogOut = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.LogOut.setObjectName("LogOut")
        self.horizontalLayout_12.addWidget(self.LogOut)
        self.Gurulayout.addLayout(self.horizontalLayout_12)
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.Gurulayout.addWidget(self.line_6)
        self.FeatureList = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.FeatureList.setObjectName("FeatureList")
        self.Gurulayout.addWidget(self.FeatureList)

        self.FeatureBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.FeatureBox.setEditable(False)
        self.FeatureBox.setMaxVisibleItems(20)
        self.FeatureBox.setObjectName("FeatureBox")
        self.FeatureBox.addItem("")
        self.Gurulayout.addWidget(self.FeatureBox)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Gurulayout.addWidget(self.line_5)
        self.GuruFeatureName = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.GuruFeatureName.setObjectName("GuruFeatureName")
        self.Gurulayout.addWidget(self.GuruFeatureName)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 7, 0, 7)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.BoolBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.BoolBox.setObjectName("BoolBox")
        self.horizontalLayout_2.addWidget(self.BoolBox)

        self.IntSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.IntSpinBox.setObjectName("IntSpinBox")
        self.horizontalLayout_2.addWidget(self.IntSpinBox)
        self.Gurulayout.addLayout(self.horizontalLayout_2)

        self.StringBox = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.StringBox.setMaximumSize(QtCore.QSize(16777215, 28))
        self.StringBox.setObjectName("StringBox")
        self.Gurulayout.addWidget(self.StringBox)

        self.EnumBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.EnumBox.setObjectName("EnumBox")
        self.Gurulayout.addWidget(self.EnumBox)

        self.IntSlider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.IntSlider.setOrientation(QtCore.Qt.Horizontal)
        self.IntSlider.setObjectName("IntSlider")
        self.Gurulayout.addWidget(self.IntSlider)

        self.DescriptionGuru = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionGuru.sizePolicy().hasHeightForWidth())
        self.DescriptionGuru.setSizePolicy(sizePolicy)
        self.DescriptionGuru.setMinimumSize(QtCore.QSize(305, 113))
        self.DescriptionGuru.setMaximumSize(QtCore.QSize(305, 305))
        self.DescriptionGuru.setScaledContents(True)
        self.DescriptionGuru.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.DescriptionGuru.setWordWrap(True)
        self.DescriptionGuru.setObjectName("DescriptionGuru")
        self.Gurulayout.addWidget(self.DescriptionGuru)

        self.parameter_Box.addTab(self.Parameter_BoxPage2, "")
        self.gridLayout.addWidget(self.parameter_Box, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1198, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionLoad_image = QtWidgets.QAction(MainWindow)
        self.actionLoad_image.setObjectName("actionLoad_image")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_image)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.parameter_Box.setCurrentIndex(0)
        self.FeatureBox.setCurrentIndex(0)
        self.Exposure_Time.valueChanged['int'].connect(self.Exposure_Box.setValue)
        self.Exposure_Box.valueChanged['int'].connect(self.Exposure_Time.setValue)
        self.Gain.valueChanged['int'].connect(self.Gain_Box.setValue)
        self.Gain_Box.valueChanged['int'].connect(self.Gain.setValue)
        self.TargetBrightnessslider.valueChanged['int'].connect(self.TargetBrightnessbox.setValue)
        self.TargetBrightnessbox.valueChanged['int'].connect(self.TargetBrightnessslider.setValue)
        self.IntSpinBox.valueChanged['int'].connect(self.IntSlider.setValue)
        self.IntSlider.valueChanged['int'].connect(self.IntSpinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Timer = QTimer()
        self.Timer.setInterval(10)
        self.Timer.timeout.connect(self.update)
        self.Timer.start()

        self.Timer2 = QTimer()
        self.Timer2.setInterval(1000)
        self.Timer2.timeout.connect(self.rasptime)
        self.Timer2.start()

        self.scale = 1

        self.Image = None

    def retranslateUi(self, MainWindow):
        """
Self Generated connections of widgets in GUI,but also self added connections
        :param MainWindow:
        """
        self._mutex.lock()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Snapshot.setStatusTip(_translate("MainWindow", "Allows to capture and save the current frame"))
        self.Snapshot.setText(_translate("MainWindow", "Save Frame"))
        self.ZoomInButton.setStatusTip(_translate("MainWindow", "zooming into frame"))
        self.ZoomInButton.setText(_translate("MainWindow", "Zoom in"))
        self.ZoomOutButton.setStatusTip(_translate("MainWindow", "zoom out of frame"))
        self.ZoomOutButton.setText(_translate("MainWindow", "Zoom out"))
        self.time.setText(_translate("MainWindow", "Time"))
        self.Timedisplay.setStatusTip(_translate("MainWindow", "Local time"))
        self.Timedisplay.setText(_translate("MainWindow", "00:00:00"))
        self.Frames.setText(_translate("MainWindow", "Frames:"))
        self.Framenumbers.setStatusTip(_translate("MainWindow", "Numbers of frame passed, max 9999 befor reset"))
        self.Framenumbers.setText(_translate("MainWindow", "1"))
        self.VideoStream.setToolTip(_translate("MainWindow", "Video Frames from Camera"))
        self.VideoStream.setStatusTip(_translate("MainWindow", "Frames Feed"))
        self.VideoStream.setWhatsThis(_translate("MainWindow", "Hello2"))
        self.parameter_Box.setStatusTip(_translate("MainWindow", "Parameter Control"))
        self.parameter_Box.setAccessibleDescription(_translate("MainWindow", "deuwigbw"))
        self.label_4.setText(_translate("MainWindow", "Feature"))
        self.label_5.setText(_translate("MainWindow", "Value"))
        self.Auto.setStatusTip(_translate("MainWindow", "Set Atomatic function adjustement for Exposure time and Gain"))
        self.Auto.setAccessibleDescription(_translate("MainWindow", "fhewiogbv"))
        self.Auto.setText(_translate("MainWindow", "Auto "))
        self.Manual.setStatusTip(_translate("MainWindow", "Manual adjustements of parameters"))
        self.Manual.setText(_translate("MainWindow", "Manual"))
        self.label.setText(_translate("MainWindow", "Exposure Time"))
        self.Exposure_Box.setSuffix(_translate("MainWindow", "µs"))
        self.label_2.setText(_translate("MainWindow", "Gain"))
        self.Gain_Box.setSuffix(_translate("MainWindow", "db"))
        self.label_13.setText(_translate("MainWindow", "Target Brightness"))
        self.TargetBrightnessbox.setSuffix(_translate("MainWindow", "%"))
        self.Coordinates.setStatusTip(_translate("MainWindow", "show the Coordinates on screen"))
        self.Coordinates.setText(_translate("MainWindow", "Coordinates"))
        self.label_12.setText(_translate("MainWindow", "Offset Readout"))
        self.label_8.setText(_translate("MainWindow", "T Axis"))
        self.TAxisReadOut.setStatusTip(_translate("MainWindow", "Approximate T Axis difference with laser"))
        self.label_9.setText(_translate("MainWindow", "mm"))
        self.label_10.setText(_translate("MainWindow", "U Axis"))
        self.UAxisReadOut.setStatusTip(_translate("MainWindow", "Approximate U Axis difference with laser"))
        self.label_11.setText(_translate("MainWindow", "mm"))
        self.ReadOffsetButton.setStatusTip(_translate("MainWindow", "Start the evaluation process of current frame"))
        self.ReadOffsetButton.setText(_translate("MainWindow", "read Offset"))
        # self.DescriptionStandard.setText(_translate("MainWindow", "Description"))
        self.parameter_Box.setTabText(self.parameter_Box.indexOf(self.Beginner_Parameter),
                                      _translate("MainWindow", "Standard"))
        self.SignInButton.setStatusTip(_translate("MainWindow", "Gain advanced access to features"))
        self.SignInButton.setText(_translate("MainWindow", "Sign in"))
        self.LogOut.setStatusTip(_translate("MainWindow", "Disable advanced access to features"))
        self.LogOut.setText(_translate("MainWindow", "Sign out"))
        self.FeatureList.setText(_translate("MainWindow", "Feature List"))
        self.FeatureBox.setStatusTip(_translate("MainWindow", "List of camera features"))
        self.FeatureBox.setItemText(0, _translate("MainWindow", "Choose Feature"))
        self.GuruFeatureName.setText(_translate("MainWindow", "TextLabel"))
        self.BoolBox.setText(_translate("MainWindow", "CheckBox"))
        self.DescriptionGuru.setText(_translate("MainWindow", "Description"))
        self.parameter_Box.setTabText(self.parameter_Box.indexOf(self.Parameter_BoxPage2),
                                      _translate("MainWindow", "Guru"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionLoad_image.setText(_translate("MainWindow", "Load image"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLoad_image.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+F4"))

        # initilise the values of parameters
        FeatureControle.parainit()
        # Setting the right values into the interface by checking the camera
        self.Exposure_Box.setValue(FeatureControle.getval("ExposureTime"))
        self.Exposure_Time.setValue(FeatureControle.getval("ExposureTime"))
        self.Gain_Box.setValue(FeatureControle.getval("Gain"))
        self.Gain.setValue(FeatureControle.getval("Gain"))
        self.TargetBrightnessbox.setValue(FeatureControle.getval("TargetBrightness"))
        self.TargetBrightnessslider.setValue(FeatureControle.getval("TargetBrightness"))
        self.loginstate = False

        if FeatureControle.getval("ExposureTimeAuto"):
            self.Auto.setChecked(True)
            self.Manual.setChecked(False)
            self.autoexptime()
            self.autogain()
        else:
            self.Auto.setChecked(False)
            self.Manual.setChecked(True)
            self.autoexptime()
            self.autogain()

        self.TargetBrightnessbox.setDisabled(True)
        self.TargetBrightnessslider.setDisabled(True)
        self.TAxisReadOut.setDisabled(True)
        self.UAxisReadOut.setDisabled(True)

        if not self.loginstate:
            self.FeatureBox.setDisabled(True)
            self.LogOut.setDisabled(True)
            self.BoolBox.setDisabled(True)
            self.IntSpinBox.setDisabled(True)
            self.IntSlider.setDisabled(True)
            self.EnumBox.setDisabled(True)
            self.StringBox.setDisabled(True)

        # Control connection of widget from the interface and which functions should be executed
        self.Exposure_Time.valueChanged.connect(self.setexptime)
        self.Auto.stateChanged.connect(self.autoexptime)
        self.Gain.valueChanged.connect(self.setgain)
        self.Auto.stateChanged.connect(self.autogain)
        self.Manual.stateChanged.connect(self.manualchange)

        self.TargetBrightnessslider.valueChanged.connect(self.setbrightness)

        self.Snapshot.clicked.connect(self.Captureimage)

        self.actionLoad_image.triggered.connect(self.openimage)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionSave_as.triggered.connect(self.Captureimage)

        self.ZoomInButton.clicked.connect(self.zoom_in)
        self.ZoomOutButton.clicked.connect(self.zoom_out)

        self.Coordinates.stateChanged.connect(self.coordinates)
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.0)
        self.CoordinatesDisplay.setGraphicsEffect(self.opacity_effect)

        self.ReadOffsetButton.clicked.connect(self.readoffset)

        self.FeatureBox.currentTextChanged.connect(self.autoguigenerate)

        self.SignInButton.clicked.connect(self.openlog)
        self.LogOut.clicked.connect(self.signedout)
        self.EnumBox.currentTextChanged.connect(self.featureenumset)
        self.IntSpinBox.valueChanged.connect(self.featurefloatset)
        self.BoolBox.stateChanged.connect(self.featureboolset)

        self.featurenamelist = FeatureControle.GetMasterFeatureList()
        for f in self.featurenamelist:
            self.FeatureBox.addItem(f[0])

    def update(self):
        """
Allows to generate the Streams of frames and to display them on the aproppriate
Qlabel in the interface.
Every 5 frames the watchdog will signal a flashing light
        :return: Frame for Qlabel
        """
        try:
            global cnt
            cnt = cnt + 1
            Frame = FeatureControle.getimageMono()
            # Frame = FeatureControle.getimageBGR()
            Img = Frame.scaled(self.VideoStream.size() * self.scale)
            self.VideoStream.setPixmap(QPixmap.fromImage(Img))
            self.Framenumbers.setText(str(cnt))
            if cnt > 9999:
                cnt = 0
            if cnt % 5 == 0:
                ui.flashing()
        # print(cnt)
        except Exception as e:
            print(type(e))
            traceback.print_exc()
        #return Frame

    def manualchange(self):
        if self.Manual.isChecked():
            self.Auto.setChecked(False)
        elif not self.Manual.isChecked():
            self.Auto.setChecked(True)

    def autoexptime(self):

        if self.Auto.isChecked():
            FeatureControle.AutoExpTime(True)
            self.Manual.setChecked(False)
            self.Exposure_Time.setDisabled(True)
            self.Exposure_Box.setDisabled(True)
            self.TargetBrightnessbox.setDisabled(False)
            self.TargetBrightnessslider.setDisabled(False)
            self.Exposure_Box.setValue(FeatureControle.getval("ExposureTime"))
            self.Exposure_Time.setValue(FeatureControle.getval("ExposureTime"))

        elif not self.Auto.isChecked():
            FeatureControle.AutoExpTime(False)
            self.Manual.setChecked(True)
            self.Exposure_Time.setDisabled(False)
            self.Exposure_Box.setDisabled(False)
            self.TargetBrightnessbox.setDisabled(True)
            self.TargetBrightnessslider.setDisabled(True)
            self.Exposure_Box.setValue(FeatureControle.getval("ExposureTime"))
            self.Exposure_Time.setValue(FeatureControle.getval("ExposureTime"))

    def setexptime(self):
        if not self.Auto.isChecked():
            try:
                FeatureControle.SetExpTime(self.Exposure_Time.value())
                print(FeatureControle.GetExptime())
            except Exception as e:
                print(type(e))
                traceback.print_exc()
            return

    def getexptime(self):
        exptime = FeatureControle.GetExptime()
        self.Gain.setValue(exptime)

    def autogain(self):

        if self.Auto.isChecked():
            FeatureControle.AutoGain(True)
            self.Gain.setDisabled(True)
            self.Gain_Box.setDisabled(True)
            self.Gain_Box.setValue(FeatureControle.getval("Gain"))
            self.Gain.setValue(FeatureControle.getval("Gain"))

        elif not self.Auto.isChecked():
            FeatureControle.AutoGain(False)
            self.Gain.setDisabled(False)
            self.Gain_Box.setDisabled(False)
            self.Gain_Box.setValue(FeatureControle.getval("Gain"))
            self.Gain.setValue(FeatureControle.getval("Gain"))

    def setgain(self):
        if not self.Auto.isChecked():
            try:
                FeatureControle.SetGain(self.Gain.value())
                print(FeatureControle.GetGain())
            except Exception as e:
                print(type(e))
                traceback.print_exc()
            return

    def getgain(self):
        gain = FeatureControle.GetGain()
        self.Gain.setValue(gain)

    def setbrightness(self):
        if self.Auto.isChecked():
            try:
                FeatureControle.SetBrightness(self.TargetBrightnessslider.value())
                print(FeatureControle.getval("TargetBrightness"))
            except Exception as e:
                print(type(e))
                traceback.print_exc()
            return

    def flashing(self):
        if self.flag:
            self.Frames.setStyleSheet('background-color: none; font-size: 15px')
        else:
            self.Frames.setStyleSheet('background-color: green; font-size: 15px')
        self.flag = not self.flag

    def Captureimage(self):
        try:
            FeatureControle.save()
        except Exception as e:
            print(type(e))
            traceback.print_exc()
        return

    def openimage(self):
        FeatureControle.OpenImage()

    def zoom_in(self):
        if self.scale < 2:
            self.scale *= 1.1
            print(self.scale)
            self.update()

    def zoom_out(self):
        self.scale /= 1.1
        print(self.scale)
        self.update()
        if self.scale < 1:
            self.scale = 1

    def rasptime(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # print("Current Time =", current_time)
        self.Timedisplay.setText(current_time)

    def readoffset(self):
        dist = Off.offsetread()
        # if not dist == []:
        self.TAxisReadOut.setPlainText(str(dist[0]))
        self.UAxisReadOut.setPlainText(str(dist[1]))

    def autoguigenerate(self):
        try:
            feature = self.FeatureBox.currentText()
            self.GuruFeatureName.setText(feature)
            featureval, featureinter, featuremax, featuremin, featureenumlist = FeatureControle.autogenerategui(feature)
            featuredesc = FeatureControle.featuredescrpition(feature)
            self.DescriptionGuru.setText(featuredesc)

            if featureinter == "Not Available":
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
                self.StringBox.setPlainText(featureval)

            if featureinter == "bool":
                self.BoolBox.setDisabled(False)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
                self.BoolBox.setChecked(featureval)

            elif featureinter == "int":
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(False)
                self.IntSlider.setDisabled(False)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
                if featuremax > 2147483647:
                    featuremax = featuremax / 2
                    featuremin = featuremax * -1
                self.IntSpinBox.setMaximum(int(featuremax))
                self.IntSpinBox.setMinimum(int(featuremin))
                self.IntSlider.setMaximum(int(featuremax))
                self.IntSlider.setMinimum(int(featuremin))
                self.IntSpinBox.setValue(int(featureval))

            elif featureinter == "float":
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(False)
                self.IntSlider.setDisabled(False)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(True)
                self.IntSpinBox.setMaximum(int(featuremax))
                self.IntSpinBox.setMinimum(int(featuremin))
                self.IntSlider.setMaximum(int(featuremax))
                self.IntSlider.setMinimum(int(featuremin))
                self.IntSpinBox.setValue(int(featureval))

            elif featureinter == "string":
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(True)
                self.StringBox.setDisabled(False)
                self.StringBox.setPlainText(featureval)

            elif featureinter == "enum":
                self.EnumBox.clear()
                self.BoolBox.setDisabled(True)
                self.IntSpinBox.setDisabled(True)
                self.IntSlider.setDisabled(True)
                self.EnumBox.setDisabled(False)
                self.StringBox.setDisabled(True)
                self.EnumBox.addItem(featureval)
                for f in featureenumlist:
                    if not f == featureval:
                        self.EnumBox.addItem(f)

        except Exception as e:
            print(type(e))
            traceback.print_exc()

    def featureenumset(self):
        try:
            if not self.EnumBox.currentText() is None:
                enum = self.EnumBox.currentText()
                name = self.FeatureBox.currentText()
                FeatureControle.enumsetter(name, enum)
        except Exception as e:
            print(type(e))
            traceback.print_exc()

    def featureboolset(self):
        try:
            name = self.FeatureBox.currentText()
            if self.BoolBox.checkState():
                state = "Continuous"
            elif not self.BoolBox.checkState():
                state = "Off"
            FeatureControle.boolset(name, state)
        except Exception as e:
            print(type(e))
            traceback.print_exc()

    def featurefloatset(self):
        try:
            name = self.FeatureBox.currentText()
            val = self.IntSpinBox.value()
            FeatureControle.floatset(name, val)
        except Exception as e:
            print(type(e))
            traceback.print_exc()

    def Description(self, featurename):
        desc = FeatureControle.featuredescrpition(featurename)
        self.DescriptionStandard.setText(desc)

    def openlog(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.loginbutton.clicked.connect(self.signedin)

    def signedin(self):
        if self.ui.email.text() == 'admin' and self.ui.password.text() == 'admin':
            self.ui.endmessage.setText('Successfull login')
            print('logdin')
            self.FeatureBox.setDisabled(False)
            self.LogOut.setDisabled(False)
            self.BoolBox.setDisabled(False)
            self.IntSpinBox.setDisabled(False)
            self.IntSlider.setDisabled(False)
            self.EnumBox.setDisabled(False)
            self.StringBox.setDisabled(False)
            self.SignInButton.setDisabled(True)
            self.window.close()
        else:
            print('The email or Password are incorrect')
            self.ui.endmessage.setText('The Email or Password are incorrect. Please try again')

    def signedout(self):
        self.SignInButton.setDisabled(False)
        self.FeatureBox.setDisabled(True)
        self.LogOut.setDisabled(True)
        self.BoolBox.setDisabled(True)
        self.IntSpinBox.setDisabled(True)
        self.IntSlider.setDisabled(True)
        self.EnumBox.setDisabled(True)
        self.StringBox.setDisabled(True)

    def coordinates(self):
        if self.Coordinates.isChecked():
            self.opacity_effect.setOpacity(1.0)
            self.CoordinatesDisplay.setGraphicsEffect(self.opacity_effect)

        elif not self.Coordinates.isChecked():
            self.opacity_effect.setOpacity(0.0)
            self.CoordinatesDisplay.setGraphicsEffect(self.opacity_effect)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
