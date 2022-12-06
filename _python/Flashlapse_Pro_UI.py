# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Flashlapse_Pro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../_image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Preview_Frame = QtWidgets.QLabel(self.centralwidget)
        self.Preview_Frame.setGeometry(QtCore.QRect(660, 10, 350, 349))
        self.Preview_Frame.setToolTip("")
        self.Preview_Frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.Preview_Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Preview_Frame.setLineWidth(3)
        self.Preview_Frame.setText("")
        self.Preview_Frame.setPixmap(QtGui.QPixmap("../_image/Background.png"))
        self.Preview_Frame.setScaledContents(True)
        self.Preview_Frame.setObjectName("Preview_Frame")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 640, 550))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 611, 241))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image_Title = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Title.setObjectName("Image_Title")
        self.verticalLayout.addWidget(self.Image_Title)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.title_lineEdit.setEnabled(True)
        self.title_lineEdit.setToolTip("")
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.horizontalLayout_2.addWidget(self.title_lineEdit)
        self.addDate_pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.addDate_pushButton.setEnabled(False)
        self.addDate_pushButton.setObjectName("addDate_pushButton")
        self.horizontalLayout_2.addWidget(self.addDate_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Image_Interval = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Interval.setObjectName("Image_Interval")
        self.verticalLayout.addWidget(self.Image_Interval)
        self.ICI_spinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.ICI_spinBox.setEnabled(True)
        self.ICI_spinBox.setMinimum(2)
        self.ICI_spinBox.setMaximum(99999999)
        self.ICI_spinBox.setProperty("value", 2)
        self.ICI_spinBox.setObjectName("ICI_spinBox")
        self.verticalLayout.addWidget(self.ICI_spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Image_Duration = QtWidgets.QLabel(self.layoutWidget_2)
        self.Image_Duration.setObjectName("Image_Duration")
        self.verticalLayout_2.addWidget(self.Image_Duration)
        self.ISD_spinBox = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.ISD_spinBox.setEnabled(True)
        self.ISD_spinBox.setMinimum(2)
        self.ISD_spinBox.setMaximum(99999999)
        self.ISD_spinBox.setProperty("value", 2)
        self.ISD_spinBox.setObjectName("ISD_spinBox")
        self.verticalLayout_2.addWidget(self.ISD_spinBox)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.directory_label = QtWidgets.QLabel(self.layoutWidget_2)
        self.directory_label.setEnabled(True)
        self.directory_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.directory_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.directory_label.setAlignment(QtCore.Qt.AlignCenter)
        self.directory_label.setObjectName("directory_label")
        self.verticalLayout_2.addWidget(self.directory_label)
        self.directory_pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.directory_pushButton.setEnabled(True)
        self.directory_pushButton.setCheckable(False)
        self.directory_pushButton.setObjectName("directory_pushButton")
        self.verticalLayout_2.addWidget(self.directory_pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 440, 611, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Progress_Label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.Progress_Label_2.setObjectName("Progress_Label_2")
        self.verticalLayout_7.addWidget(self.Progress_Label_2, 0, QtCore.Qt.AlignHCenter)
        self.Progress_Bar_2 = QtWidgets.QProgressBar(self.layoutWidget)
        self.Progress_Bar_2.setEnabled(False)
        self.Progress_Bar_2.setProperty("value", 0)
        self.Progress_Bar_2.setObjectName("Progress_Bar_2")
        self.verticalLayout_7.addWidget(self.Progress_Bar_2)
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setGeometry(QtCore.QRect(10, 260, 611, 171))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 591, 154))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 4, 1, 1)
        self.CoreCtr_label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.CoreCtr_label_6.setObjectName("CoreCtr_label_6")
        self.gridLayout_2.addWidget(self.CoreCtr_label_6, 3, 2, 1, 1)
        self.yAxis_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.yAxis_label.setObjectName("yAxis_label")
        self.gridLayout_2.addWidget(self.yAxis_label, 3, 4, 1, 1)
        self.xAxis_horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.xAxis_horizontalSlider.setMaximum(100)
        self.xAxis_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.xAxis_horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.xAxis_horizontalSlider.setObjectName("xAxis_horizontalSlider")
        self.gridLayout_2.addWidget(self.xAxis_horizontalSlider, 3, 0, 1, 1)
        self.JPG_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.JPG_radioButton.setChecked(True)
        self.JPG_radioButton.setObjectName("JPG_radioButton")
        self.gridLayout_2.addWidget(self.JPG_radioButton, 6, 0, 1, 1)
        self.yAxis_horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.yAxis_horizontalSlider.setMinimum(1)
        self.yAxis_horizontalSlider.setMaximum(100)
        self.yAxis_horizontalSlider.setProperty("value", 100)
        self.yAxis_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.yAxis_horizontalSlider.setInvertedAppearance(False)
        self.yAxis_horizontalSlider.setInvertedControls(False)
        self.yAxis_horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.yAxis_horizontalSlider.setObjectName("yAxis_horizontalSlider")
        self.gridLayout_2.addWidget(self.yAxis_horizontalSlider, 3, 3, 1, 1)
        self.resolution_label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.resolution_label_3.setObjectName("resolution_label_3")
        self.gridLayout_2.addWidget(self.resolution_label_3, 2, 2, 1, 1)
        self.PNG_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.PNG_radioButton.setObjectName("PNG_radioButton")
        self.gridLayout_2.addWidget(self.PNG_radioButton, 6, 3, 1, 1)
        self.resolution_label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.resolution_label_2.setObjectName("resolution_label_2")
        self.gridLayout_2.addWidget(self.resolution_label_2, 5, 2, 1, 1)
        self.y_resolution_spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.y_resolution_spinBox.setMinimum(50)
        self.y_resolution_spinBox.setMaximum(2464)
        self.y_resolution_spinBox.setProperty("value", 2464)
        self.y_resolution_spinBox.setObjectName("y_resolution_spinBox")
        self.gridLayout_2.addWidget(self.y_resolution_spinBox, 1, 3, 1, 1)
        self.xAxis_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.xAxis_label.setObjectName("xAxis_label")
        self.gridLayout_2.addWidget(self.xAxis_label, 3, 1, 1, 1)
        self.x_resolution_spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.x_resolution_spinBox.setMinimum(50)
        self.x_resolution_spinBox.setMaximum(3240)
        self.x_resolution_spinBox.setProperty("value", 2464)
        self.x_resolution_spinBox.setObjectName("x_resolution_spinBox")
        self.gridLayout_2.addWidget(self.x_resolution_spinBox, 1, 0, 1, 1)
        self.resolution_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.resolution_label.setObjectName("resolution_label")
        self.gridLayout_2.addWidget(self.resolution_label, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_2.addWidget(self.line_10, 5, 0, 1, 2)
        self.line_11 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_2.addWidget(self.line_11, 5, 3, 1, 2)
        self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 2, 3, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.motion_control_frame = QtWidgets.QFrame(self.tab_2)
        self.motion_control_frame.setGeometry(QtCore.QRect(219, 10, 191, 501))
        self.motion_control_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.motion_control_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.motion_control_frame.setObjectName("motion_control_frame")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.motion_control_frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 171, 481))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.motion_increment_spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.motion_increment_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.motion_increment_spinBox.setMinimum(1)
        self.motion_increment_spinBox.setMaximum(10)
        self.motion_increment_spinBox.setProperty("value", 5)
        self.motion_increment_spinBox.setObjectName("motion_increment_spinBox")
        self.gridLayout_3.addWidget(self.motion_increment_spinBox, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 7, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        self.up_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.up_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.up_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../_image/Arrows-Up.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_pushButton.setIcon(icon1)
        self.up_pushButton.setIconSize(QtCore.QSize(32, 32))
        self.up_pushButton.setAutoDefault(False)
        self.up_pushButton.setObjectName("up_pushButton")
        self.gridLayout_3.addWidget(self.up_pushButton, 1, 0, 1, 1)
        self.down_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.down_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.down_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../_image/Arrows-Down.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_pushButton.setIcon(icon2)
        self.down_pushButton.setIconSize(QtCore.QSize(64, 32))
        self.down_pushButton.setObjectName("down_pushButton")
        self.gridLayout_3.addWidget(self.down_pushButton, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 8, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.spinBox.setMinimum(65)
        self.spinBox.setMaximum(155)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 9, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem5, 5, 0, 1, 1)
        self.motion_settings_frame = QtWidgets.QFrame(self.tab_2)
        self.motion_settings_frame.setGeometry(QtCore.QRect(418, 10, 201, 501))
        self.motion_settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.motion_settings_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.motion_settings_frame.setObjectName("motion_settings_frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.motion_settings_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 181, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.dial = QtWidgets.QDial(self.verticalLayoutWidget_2)
        self.dial.setMinimum(1)
        self.dial.setMaximum(5)
        self.dial.setSliderPosition(3)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.verticalLayout_8.addWidget(self.dial)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.dial_2 = QtWidgets.QDial(self.verticalLayoutWidget_2)
        self.dial_2.setMinimum(1)
        self.dial_2.setMaximum(5)
        self.dial_2.setProperty("value", 3)
        self.dial_2.setNotchesVisible(True)
        self.dial_2.setObjectName("dial_2")
        self.verticalLayout_8.addWidget(self.dial_2)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.motion_stop_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.motion_stop_pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../_image/Emergency_Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.motion_stop_pushButton.setIcon(icon3)
        self.motion_stop_pushButton.setIconSize(QtCore.QSize(128, 128))
        self.motion_stop_pushButton.setObjectName("motion_stop_pushButton")
        self.verticalLayout_8.addWidget(self.motion_stop_pushButton)
        self.motion_slider_frame = QtWidgets.QFrame(self.tab_2)
        self.motion_slider_frame.setGeometry(QtCore.QRect(9, 10, 201, 501))
        self.motion_slider_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.motion_slider_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.motion_slider_frame.setObjectName("motion_slider_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.motion_slider_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 181, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.motion_position_verticalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.motion_position_verticalSlider.setMinimumSize(QtCore.QSize(40, 0))
        self.motion_position_verticalSlider.setMinimum(65)
        self.motion_position_verticalSlider.setMaximum(155)
        self.motion_position_verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.motion_position_verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.motion_position_verticalSlider.setTickInterval(5)
        self.motion_position_verticalSlider.setObjectName("motion_position_verticalSlider")
        self.verticalLayout_6.addWidget(self.motion_position_verticalSlider, 0, QtCore.Qt.AlignHCenter)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.motion_rangefinder_text_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.motion_rangefinder_text_label.setObjectName("motion_rangefinder_text_label")
        self.verticalLayout_6.addWidget(self.motion_rangefinder_text_label)
        self.motion_rangefinder_data_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.motion_rangefinder_data_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.motion_rangefinder_data_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.motion_rangefinder_data_label.setAlignment(QtCore.Qt.AlignCenter)
        self.motion_rangefinder_data_label.setObjectName("motion_rangefinder_data_label")
        self.verticalLayout_6.addWidget(self.motion_rangefinder_data_label)
        self.motion_target_position_text_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.motion_target_position_text_label.setObjectName("motion_target_position_text_label")
        self.verticalLayout_6.addWidget(self.motion_target_position_text_label)
        self.motion_target_position_setting_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.motion_target_position_setting_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.motion_target_position_setting_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.motion_target_position_setting_label.setAlignment(QtCore.Qt.AlignCenter)
        self.motion_target_position_setting_label.setObjectName("motion_target_position_setting_label")
        self.verticalLayout_6.addWidget(self.motion_target_position_setting_label)
        self.TOF_update_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.TOF_update_pushButton.setObjectName("TOF_update_pushButton")
        self.verticalLayout_6.addWidget(self.TOF_update_pushButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 601, 481))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 10, 600, 481))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tabWidget_3.addTab(self.tab_16, "")
        self.tabWidget.addTab(self.tab_5, "")
        self.Capture_frame = QtWidgets.QFrame(self.centralwidget)
        self.Capture_frame.setEnabled(True)
        self.Capture_frame.setGeometry(QtCore.QRect(840, 370, 171, 191))
        self.Capture_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Capture_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Capture_frame.setObjectName("Capture_frame")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Capture_frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 15, 161, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.snapshot_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.snapshot_pushButton.setEnabled(True)
        self.snapshot_pushButton.setObjectName("snapshot_pushButton")
        self.verticalLayout_17.addWidget(self.snapshot_pushButton)
        self.preview_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.preview_pushButton.setObjectName("preview_pushButton")
        self.verticalLayout_17.addWidget(self.preview_pushButton)
        self.rotate_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.rotate_pushButton.setEnabled(True)
        self.rotate_pushButton.setObjectName("rotate_pushButton")
        self.verticalLayout_17.addWidget(self.rotate_pushButton)
        self.startImaging_pushButton = QtWidgets.QPushButton(self.Capture_frame)
        self.startImaging_pushButton.setEnabled(False)
        self.startImaging_pushButton.setGeometry(QtCore.QRect(10, 120, 161, 61))
        self.startImaging_pushButton.setToolTip("")
        self.startImaging_pushButton.setObjectName("startImaging_pushButton")
        self.Capture_frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.Capture_frame_2.setEnabled(True)
        self.Capture_frame_2.setGeometry(QtCore.QRect(660, 370, 171, 191))
        self.Capture_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Capture_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Capture_frame_2.setObjectName("Capture_frame_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setEnabled(False)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCreate_Timelapse = QtWidgets.QAction(MainWindow)
        self.actionCreate_Timelapse.setObjectName("actionCreate_Timelapse")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashLapse Commad Point"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "LIGHTING"))
        self.Image_Title.setText(_translate("MainWindow", "Image Sequence Title"))
        self.addDate_pushButton.setText(_translate("MainWindow", "Add Date"))
        self.Image_Interval.setText(_translate("MainWindow", "Image Capture Interval"))
        self.ICI_spinBox.setSuffix(_translate("MainWindow", " min"))
        self.Image_Duration.setText(_translate("MainWindow", "Image Sequence Duration"))
        self.ISD_spinBox.setSuffix(_translate("MainWindow", " min"))
        self.directory_label.setText(_translate("MainWindow", "Sequence Title Required"))
        self.directory_pushButton.setText(_translate("MainWindow", "Select Storage Directory"))
        self.Progress_Label_2.setText(_translate("MainWindow", "Progress: 0 / 1"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">[ 50 , 2464 ]</span></p></body></html>"))
        self.CoreCtr_label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.yAxis_label.setText(_translate("MainWindow", "Zoom Axis B: 1.00"))
        self.xAxis_horizontalSlider.setToolTip(_translate("MainWindow", "Zoom controls, snapshot is taken when released, useful during focusing"))
        self.JPG_radioButton.setText(_translate("MainWindow", ".JPG"))
        self.yAxis_horizontalSlider.setToolTip(_translate("MainWindow", "Zoom controls, snapshot is taken when released, useful during focusing"))
        self.resolution_label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Zoom Control</span></p></body></html>"))
        self.PNG_radioButton.setText(_translate("MainWindow", ".PNG"))
        self.resolution_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Image Format</span></p></body></html>"))
        self.y_resolution_spinBox.setSuffix(_translate("MainWindow", " px"))
        self.xAxis_label.setText(_translate("MainWindow", "Zoom Axis A: 0.00"))
        self.x_resolution_spinBox.setSuffix(_translate("MainWindow", " px"))
        self.resolution_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Imaging Resolution</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">[ 50 , 3240 ]</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "IMAGING"))
        self.motion_increment_spinBox.setSuffix(_translate("MainWindow", " mm"))
        self.label_8.setText(_translate("MainWindow", "Move to New Position:"))
        self.label_5.setText(_translate("MainWindow", "Motion Increment:"))
        self.spinBox.setSuffix(_translate("MainWindow", " mm"))
        self.label_6.setText(_translate("MainWindow", "Speed Level: 3"))
        self.label_7.setText(_translate("MainWindow", "Torque Level: 3"))
        self.motion_rangefinder_text_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Rangefinder Data:</span></p></body></html>"))
        self.motion_rangefinder_data_label.setText(_translate("MainWindow", "N/A mm"))
        self.motion_target_position_text_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Target Position:</span></p></body></html>"))
        self.motion_target_position_setting_label.setText(_translate("MainWindow", "N/A mm"))
        self.TOF_update_pushButton.setText(_translate("MainWindow", "Update Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "MOTION"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Temperature"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Humidity"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Oxygen Sensor"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Carbon Dioxide Sensor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "AMBIENT SENSORS"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "Temperature"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Humidity"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "Electrical Conductivity"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("MainWindow", "pH"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("MainWindow", "Nitrogen"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("MainWindow", "Phosphorus"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), _translate("MainWindow", "Potassium "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "SOIL SENSORS"))
        self.snapshot_pushButton.setToolTip(_translate("MainWindow", "Takes a quick snapshot"))
        self.snapshot_pushButton.setText(_translate("MainWindow", "SNAPSHOT"))
        self.preview_pushButton.setToolTip(_translate("MainWindow", "Takes a image with current settings"))
        self.preview_pushButton.setText(_translate("MainWindow", "PREVIEW"))
        self.rotate_pushButton.setToolTip(_translate("MainWindow", "Rotate image 90 degrees"))
        self.rotate_pushButton.setText(_translate("MainWindow", "ROTATE IMAGE"))
        self.startImaging_pushButton.setText(_translate("MainWindow", "START TIMELAPSE"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))
