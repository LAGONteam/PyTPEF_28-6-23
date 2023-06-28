
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EnkiuXhZtO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1558, 1054)
        self.verticalLayout_19 = QVBoxLayout(Form)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_10 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_38 = QFrame(self.frame)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.Spectre = PlotWidget(self.frame_38)
        self.Spectre.setObjectName(u"Spectre")
        self.Spectre.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.horizontalLayout_17.addWidget(self.Spectre)


        self.verticalLayout_2.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.Power = PlotWidget(self.frame_39)
        self.Power.setObjectName(u"Power")

        self.horizontalLayout_18.addWidget(self.Power)


        self.verticalLayout_2.addWidget(self.frame_39)


        self.horizontalLayout_10.addWidget(self.frame)

        self.frame_2 = QFrame(self.tab_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(320, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(400, 16777215))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.spb_integration = QSpinBox(self.frame_7)
        self.spb_integration.setObjectName(u"spb_integration")
        self.spb_integration.setMaximumSize(QSize(100, 16777215))
        self.spb_integration.setMinimum(100)
        self.spb_integration.setMaximum(20000)
        self.spb_integration.setSingleStep(50)

        self.horizontalLayout_5.addWidget(self.spb_integration)

        self.ckb_super_fast = QCheckBox(self.frame_7)
        self.ckb_super_fast.setObjectName(u"ckb_super_fast")
        self.ckb_super_fast.setMaximumSize(QSize(200, 16777215))
        self.ckb_super_fast.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_5.addWidget(self.ckb_super_fast)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.spb_scan = QSpinBox(self.frame_3)
        self.spb_scan.setObjectName(u"spb_scan")
        self.spb_scan.setMaximumSize(QSize(100, 16777215))
        self.spb_scan.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spb_scan.setMinimum(1)
        self.spb_scan.setMaximum(100)

        self.horizontalLayout_7.addWidget(self.spb_scan)

        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_7.addWidget(self.label_35)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_27 = QFrame(self.frame_5)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(100, 0))
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_27)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn_jod = QRadioButton(self.frame_27)
        self.btn_jod.setObjectName(u"btn_jod")

        self.verticalLayout_18.addWidget(self.btn_jod)

        self.btn_dmans = QRadioButton(self.frame_27)
        self.btn_dmans.setObjectName(u"btn_dmans")

        self.verticalLayout_18.addWidget(self.btn_dmans)


        self.horizontalLayout_2.addWidget(self.frame_27)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(200, 0))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btn_calibration = QPushButton(self.frame_13)
        self.btn_calibration.setObjectName(u"btn_calibration")

        self.verticalLayout_17.addWidget(self.btn_calibration)


        self.horizontalLayout_2.addWidget(self.frame_13)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_35 = QFrame(self.frame_6)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lcd_intensity = QLCDNumber(self.frame_35)
        self.lcd_intensity.setObjectName(u"lcd_intensity")
        self.lcd_intensity.setMaximumSize(QSize(100, 16777215))
        self.lcd_intensity.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.lcd_intensity.setDigitCount(5)
        self.lcd_intensity.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_16.addWidget(self.lcd_intensity)

        self.label_4 = QLabel(self.frame_35)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_16.addWidget(self.label_4)

        self.btn_zero_intensity = QPushButton(self.frame_35)
        self.btn_zero_intensity.setObjectName(u"btn_zero_intensity")

        self.horizontalLayout_16.addWidget(self.btn_zero_intensity)


        self.verticalLayout_4.addWidget(self.frame_35)

        self.frame_19 = QFrame(self.frame_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.frame_19)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)


        self.verticalLayout_4.addWidget(self.frame_19)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(300, 16777215))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spb_wavelength_tuning = QSpinBox(self.frame_12)
        self.spb_wavelength_tuning.setObjectName(u"spb_wavelength_tuning")
        self.spb_wavelength_tuning.setMinimum(680)
        self.spb_wavelength_tuning.setMaximum(1080)
        self.spb_wavelength_tuning.setSingleStep(2)
        self.spb_wavelength_tuning.setDisplayIntegerBase(10)

        self.horizontalLayout_4.addWidget(self.spb_wavelength_tuning)

        self.btn_set_wavelength = QPushButton(self.frame_12)
        self.btn_set_wavelength.setObjectName(u"btn_set_wavelength")

        self.horizontalLayout_4.addWidget(self.btn_set_wavelength)


        self.verticalLayout_4.addWidget(self.frame_12)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(300, 16777215))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_go = QPushButton(self.frame_8)
        self.btn_go.setObjectName(u"btn_go")
        self.btn_go.setMaximumSize(QSize(100, 16777215))
        self.btn_go.setCheckable(True)
        self.btn_go.setChecked(False)

        self.horizontalLayout_13.addWidget(self.btn_go)

        self.ls_terminal_calibration = QListWidget(self.frame_8)
        self.ls_terminal_calibration.setObjectName(u"ls_terminal_calibration")
        self.ls_terminal_calibration.setMaximumSize(QSize(350, 300))
        self.ls_terminal_calibration.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.ls_terminal_calibration.setAutoScrollMargin(16)
        self.ls_terminal_calibration.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ls_terminal_calibration.setProperty("showDropIndicator", False)
        self.ls_terminal_calibration.setSelectionMode(QAbstractItemView.NoSelection)
        self.ls_terminal_calibration.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.ls_terminal_calibration.setProperty("isWrapping", False)
        self.ls_terminal_calibration.setLayoutMode(QListView.SinglePass)
        self.ls_terminal_calibration.setSpacing(0)
        self.ls_terminal_calibration.setWordWrap(False)
        self.ls_terminal_calibration.setSortingEnabled(False)

        self.horizontalLayout_13.addWidget(self.ls_terminal_calibration)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(300, 16777215))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_28 = QFrame(self.frame_10)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(100, 16777215))
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_28)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_stop = QPushButton(self.frame_28)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_7.addWidget(self.btn_stop)


        self.horizontalLayout_11.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_10)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(100, 16777215))
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_reset = QPushButton(self.frame_29)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.btn_reset)


        self.horizontalLayout_11.addWidget(self.frame_29)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(300, 16777215))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_9)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.frame_32 = QFrame(self.frame_9)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(300, 16777215))
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lcd_power = QLCDNumber(self.frame_32)
        self.lcd_power.setObjectName(u"lcd_power")
        self.lcd_power.setMaximumSize(QSize(100, 16777215))
        self.lcd_power.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.lcd_power.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_15.addWidget(self.lcd_power)

        self.btn_zero_power = QPushButton(self.frame_32)
        self.btn_zero_power.setObjectName(u"btn_zero_power")

        self.horizontalLayout_15.addWidget(self.btn_zero_power)


        self.verticalLayout_6.addWidget(self.frame_32)

        self.label_dial_power = QLabel(self.frame_9)
        self.label_dial_power.setObjectName(u"label_dial_power")

        self.verticalLayout_6.addWidget(self.label_dial_power)

        self.dial_power = QDial(self.frame_9)
        self.dial_power.setObjectName(u"dial_power")
        self.dial_power.setMaximum(90)

        self.verticalLayout_6.addWidget(self.dial_power)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(300, 16777215))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressbar_calibration = QProgressBar(self.frame_11)
        self.progressbar_calibration.setObjectName(u"progressbar_calibration")
        self.progressbar_calibration.setMaximumSize(QSize(300, 16777215))
        self.progressbar_calibration.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressbar_calibration)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.btn_experiment_status = QPushButton(self.frame_9)
        self.btn_experiment_status.setObjectName(u"btn_experiment_status")
        self.btn_experiment_status.setMaximumSize(QSize(300, 16777215))
        self.btn_experiment_status.setFlat(False)

        self.verticalLayout_6.addWidget(self.btn_experiment_status)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout_10.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_8 = QVBoxLayout(self.tab_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_41 = QFrame(self.tab_7)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_41)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_43 = QFrame(self.frame_41)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_43)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_50 = QFrame(self.frame_43)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(16777215, 40))
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_50)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_9 = QLabel(self.frame_50)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_9)


        self.verticalLayout_20.addWidget(self.frame_50)

        self.frame_49 = QFrame(self.frame_43)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_52 = QFrame(self.frame_49)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_52)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btn_set_fluorescein = QRadioButton(self.frame_52)
        self.btn_set_fluorescein.setObjectName(u"btn_set_fluorescein")

        self.verticalLayout_22.addWidget(self.btn_set_fluorescein)

        self.btn_set_nile_red = QRadioButton(self.frame_52)
        self.btn_set_nile_red.setObjectName(u"btn_set_nile_red")

        self.verticalLayout_22.addWidget(self.btn_set_nile_red)


        self.horizontalLayout_21.addWidget(self.frame_52)

        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.le_ref_concentration = QLineEdit(self.frame_51)
        self.le_ref_concentration.setObjectName(u"le_ref_concentration")
        self.le_ref_concentration.setGeometry(QRect(10, 30, 113, 20))
        self.le_ref_concentration.setMaximumSize(QSize(113, 16777215))
        self.le_ref_concentration.setInputMethodHints(Qt.ImhNone)
        self.label_10 = QLabel(self.frame_51)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 0, 151, 20))
        self.label_10.setMinimumSize(QSize(151, 0))
        self.label_10.setMaximumSize(QSize(151, 16777215))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.frame_51)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(130, 30, 47, 13))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.frame_51)


        self.verticalLayout_20.addWidget(self.frame_49)


        self.horizontalLayout.addWidget(self.frame_43)

        self.line_2 = QFrame(self.frame_41)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.frame_44 = QFrame(self.frame_41)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_15 = QFrame(self.frame_44)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_check_calibration = QCheckBox(self.frame_15)
        self.btn_check_calibration.setObjectName(u"btn_check_calibration")
        self.btn_check_calibration.setMaximumSize(QSize(151, 16777215))
        self.btn_check_calibration.setCheckable(True)

        self.verticalLayout_9.addWidget(self.btn_check_calibration)

        self.btn_check_reference = QCheckBox(self.frame_15)
        self.btn_check_reference.setObjectName(u"btn_check_reference")
        self.btn_check_reference.setMaximumSize(QSize(151, 16777215))
        self.btn_check_reference.setCheckable(True)

        self.verticalLayout_9.addWidget(self.btn_check_reference)

        self.btn_check_samples = QCheckBox(self.frame_15)
        self.btn_check_samples.setObjectName(u"btn_check_samples")
        self.btn_check_samples.setMaximumSize(QSize(171, 16777215))
        self.btn_check_samples.setCheckable(True)

        self.verticalLayout_9.addWidget(self.btn_check_samples)

        self.btn_check_power = QCheckBox(self.frame_15)
        self.btn_check_power.setObjectName(u"btn_check_power")
        self.btn_check_power.setMaximumSize(QSize(151, 16777215))

        self.verticalLayout_9.addWidget(self.btn_check_power)

        self.btn_check_wavelength = QCheckBox(self.frame_15)
        self.btn_check_wavelength.setObjectName(u"btn_check_wavelength")
        self.btn_check_wavelength.setMaximumSize(QSize(171, 16777215))

        self.verticalLayout_9.addWidget(self.btn_check_wavelength)


        self.horizontalLayout_6.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.frame_44)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_14)


        self.horizontalLayout.addWidget(self.frame_44)


        self.verticalLayout_8.addWidget(self.frame_41)

        self.line = QFrame(self.tab_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.frame_42 = QFrame(self.tab_7)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_16 = QFrame(self.frame_42)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.btn_create_sample_number = QPushButton(self.frame_16)
        self.btn_create_sample_number.setObjectName(u"btn_create_sample_number")
        self.btn_create_sample_number.setGeometry(QRect(370, 30, 91, 31))
        self.label_26 = QLabel(self.frame_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(180, 0, 180, 30))
        self.label_26.setMinimumSize(QSize(0, 30))
        self.label_26.setMaximumSize(QSize(16777215, 30))
        self.label_26.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.le_set_sample_name = QLineEdit(self.frame_16)
        self.le_set_sample_name.setObjectName(u"le_set_sample_name")
        self.le_set_sample_name.setEnabled(True)
        self.le_set_sample_name.setGeometry(QRect(170, 50, 113, 20))
        self.label_31 = QLabel(self.frame_16)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 50, 151, 20))
        self.label_31.setMinimumSize(QSize(151, 0))
        self.label_31.setMaximumSize(QSize(151, 16777215))
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_32 = QLabel(self.frame_16)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 80, 151, 20))
        self.label_32.setMinimumSize(QSize(151, 0))
        self.label_32.setMaximumSize(QSize(151, 16777215))
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btn_delete_sample = QPushButton(self.frame_16)
        self.btn_delete_sample.setObjectName(u"btn_delete_sample")
        self.btn_delete_sample.setGeometry(QRect(370, 80, 91, 31))
        self.ls_list_of_samples = QListWidget(self.frame_16)
        self.ls_list_of_samples.setObjectName(u"ls_list_of_samples")
        self.ls_list_of_samples.setGeometry(QRect(480, 10, 161, 201))
        self.ls_list_of_samples.setMaximumSize(QSize(200, 16777215))
        self.label_29 = QLabel(self.frame_16)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 110, 151, 20))
        self.label_29.setMinimumSize(QSize(151, 0))
        self.label_29.setMaximumSize(QSize(151, 16777215))
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_set_sample_concentration = QLineEdit(self.frame_16)
        self.le_set_sample_concentration.setObjectName(u"le_set_sample_concentration")
        self.le_set_sample_concentration.setGeometry(QRect(170, 110, 113, 20))
        self.label_30 = QLabel(self.frame_16)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(290, 110, 47, 13))
        self.label_30.setScaledContents(True)
        self.line_5 = QFrame(self.frame_16)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(640, 0, 20, 221))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_33 = QLabel(self.frame_16)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 140, 151, 20))
        self.label_33.setMinimumSize(QSize(151, 0))
        self.label_33.setMaximumSize(QSize(151, 16777215))
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_set_fluo_qy = QLineEdit(self.frame_16)
        self.le_set_fluo_qy.setObjectName(u"le_set_fluo_qy")
        self.le_set_fluo_qy.setGeometry(QRect(170, 140, 113, 20))
        self.ls_solvent = QListWidget(self.frame_16)
        self.ls_solvent.setObjectName(u"ls_solvent")
        self.ls_solvent.setGeometry(QRect(180, 170, 191, 41))
        self.ls_solvent.setMaximumSize(QSize(300, 41))
        self.label_34 = QLabel(self.frame_16)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 180, 151, 20))
        self.label_34.setMinimumSize(QSize(151, 0))
        self.label_34.setMaximumSize(QSize(151, 16777215))
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ls_terminal_parameters = QListWidget(self.frame_16)
        self.ls_terminal_parameters.setObjectName(u"ls_terminal_parameters")
        self.ls_terminal_parameters.setGeometry(QRect(660, 10, 231, 201))
        self.btn_sample_info = QPushButton(self.frame_16)
        self.btn_sample_info.setObjectName(u"btn_sample_info")
        self.btn_sample_info.setGeometry(QRect(370, 130, 91, 31))
        self.btn_open = QDialogButtonBox(self.frame_16)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setGeometry(QRect(180, 80, 91, 23))
        self.btn_open.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.btn_open.setStandardButtons(QDialogButtonBox.Open)
        self.btn_open.setCenterButtons(True)
        self.ls_terminal_information_for_users_parameters = QListWidget(self.frame_16)
        self.ls_terminal_information_for_users_parameters.setObjectName(u"ls_terminal_information_for_users_parameters")
        self.ls_terminal_information_for_users_parameters.setGeometry(QRect(1050, 0, 231, 291))

        self.horizontalLayout_19.addWidget(self.frame_16)


        self.verticalLayout_8.addWidget(self.frame_42)

        self.line_3 = QFrame(self.tab_7)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.frame_40 = QFrame(self.tab_7)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_47 = QFrame(self.frame_40)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(406, 16777215))
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_47)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_12 = QLabel(self.frame_47)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_12)

        self.frame_54 = QFrame(self.frame_47)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(386, 16777215))
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_54)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_53 = QFrame(self.frame_54)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_6)

        self.label_13 = QLabel(self.frame_53)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_13)

        self.spb_set_wavelength_min = QSpinBox(self.frame_53)
        self.spb_set_wavelength_min.setObjectName(u"spb_set_wavelength_min")
        self.spb_set_wavelength_min.setMaximumSize(QSize(200, 16777215))
        self.spb_set_wavelength_min.setMinimum(680)
        self.spb_set_wavelength_min.setMaximum(1080)

        self.horizontalLayout_22.addWidget(self.spb_set_wavelength_min)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_3)


        self.verticalLayout_26.addWidget(self.frame_53)

        self.frame_57 = QFrame(self.frame_54)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_7)

        self.label_14 = QLabel(self.frame_57)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_14)

        self.spb_set_wavelength_pitch = QDoubleSpinBox(self.frame_57)
        self.spb_set_wavelength_pitch.setObjectName(u"spb_set_wavelength_pitch")
        self.spb_set_wavelength_pitch.setMaximumSize(QSize(200, 16777215))
        self.spb_set_wavelength_pitch.setDecimals(0)
        self.spb_set_wavelength_pitch.setMinimum(1.000000000000000)
        self.spb_set_wavelength_pitch.setMaximum(10000.000000000000000)

        self.horizontalLayout_23.addWidget(self.spb_set_wavelength_pitch)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_4)


        self.verticalLayout_26.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_54)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)

        self.label_15 = QLabel(self.frame_58)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_15)

        self.spb_set_wavelength_max = QSpinBox(self.frame_58)
        self.spb_set_wavelength_max.setObjectName(u"spb_set_wavelength_max")
        self.spb_set_wavelength_max.setMaximumSize(QSize(100, 16777215))
        self.spb_set_wavelength_max.setMinimum(680)
        self.spb_set_wavelength_max.setMaximum(1080)

        self.horizontalLayout_24.addWidget(self.spb_set_wavelength_max)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_5)


        self.verticalLayout_26.addWidget(self.frame_58)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.btn_check_opo = QCheckBox(self.frame_54)
        self.btn_check_opo.setObjectName(u"btn_check_opo")
        self.btn_check_opo.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_check_opo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_26.addLayout(self.horizontalLayout_9)


        self.verticalLayout_23.addWidget(self.frame_54)


        self.horizontalLayout_20.addWidget(self.frame_47)

        self.line_4 = QFrame(self.frame_40)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_4)

        self.frame_48 = QFrame(self.frame_40)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(406, 16777215))
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_48)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_60 = QFrame(self.frame_48)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(386, 16777215))
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_60)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_16 = QLabel(self.frame_60)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_16)


        self.verticalLayout_24.addWidget(self.frame_60)

        self.frame_56 = QFrame(self.frame_48)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_9)

        self.label_17 = QLabel(self.frame_56)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_17)

        self.spb_set_power_max = QSpinBox(self.frame_56)
        self.spb_set_power_max.setObjectName(u"spb_set_power_max")
        self.spb_set_power_max.setMaximumSize(QSize(100, 16777215))
        self.spb_set_power_max.setMaximum(2000)

        self.horizontalLayout_25.addWidget(self.spb_set_power_max)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_12)


        self.verticalLayout_24.addWidget(self.frame_56)

        self.frame_59 = QFrame(self.frame_48)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_10)

        self.label_18 = QLabel(self.frame_59)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_18)

        self.spb_set_power_min = QSpinBox(self.frame_59)
        self.spb_set_power_min.setObjectName(u"spb_set_power_min")
        self.spb_set_power_min.setMaximumSize(QSize(100, 16777215))
        self.spb_set_power_min.setMaximum(2000)

        self.horizontalLayout_26.addWidget(self.spb_set_power_min)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_13)


        self.verticalLayout_24.addWidget(self.frame_59)

        self.frame_55 = QFrame(self.frame_48)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_11)

        self.label_24 = QLabel(self.frame_55)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.label_24)

        self.spb_set_number_of_power_measure = QSpinBox(self.frame_55)
        self.spb_set_number_of_power_measure.setObjectName(u"spb_set_number_of_power_measure")
        self.spb_set_number_of_power_measure.setMaximumSize(QSize(100, 16777215))
        self.spb_set_number_of_power_measure.setMaximum(1000)
        self.spb_set_number_of_power_measure.setValue(1)

        self.horizontalLayout_27.addWidget(self.spb_set_number_of_power_measure)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_14)

        self.label_25 = QLabel(self.frame_55)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_27.addWidget(self.label_25)


        self.verticalLayout_24.addWidget(self.frame_55)


        self.horizontalLayout_20.addWidget(self.frame_48)


        self.verticalLayout_8.addWidget(self.frame_40)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.S2Spectrum = PlotWidget(self.tab_4)
        self.S2Spectrum.setObjectName(u"S2Spectrum")
        self.S2Spectrum.setGeometry(QRect(10, 10, 831, 251))
        self.FluoIntensitySpectrum = PlotWidget(self.tab_4)
        self.FluoIntensitySpectrum.setObjectName(u"FluoIntensitySpectrum")
        self.FluoIntensitySpectrum.setGeometry(QRect(10, 270, 831, 261))
        self.ls_list_of_all_samples = QListWidget(self.tab_4)
        self.ls_list_of_all_samples.setObjectName(u"ls_list_of_all_samples")
        self.ls_list_of_all_samples.setGeometry(QRect(30, 620, 111, 211))
        self.ls_done_wavelengths = QListWidget(self.tab_4)
        self.ls_done_wavelengths.setObjectName(u"ls_done_wavelengths")
        self.ls_done_wavelengths.setGeometry(QRect(170, 620, 111, 281))
        self.btn_set_sample = QPushButton(self.tab_4)
        self.btn_set_sample.setObjectName(u"btn_set_sample")
        self.btn_set_sample.setGeometry(QRect(30, 580, 111, 25))
        self.btn_set_sample.setFlat(True)
        self.btn_set_sample_wavelength = QPushButton(self.tab_4)
        self.btn_set_sample_wavelength.setObjectName(u"btn_set_sample_wavelength")
        self.btn_set_sample_wavelength.setGeometry(QRect(170, 580, 111, 25))
        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(380, 560, 101, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(self.tab_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(490, 560, 101, 20))
        self.label_27.setFont(font)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_28 = QLabel(self.tab_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(590, 560, 151, 20))
        self.label_28.setFont(font)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.btn_new_measure_data = QPushButton(self.tab_4)
        self.btn_new_measure_data.setObjectName(u"btn_new_measure_data")
        self.btn_new_measure_data.setGeometry(QRect(790, 750, 131, 71))
        self.btn_remove_data = QPushButton(self.tab_4)
        self.btn_remove_data.setObjectName(u"btn_remove_data")
        self.btn_remove_data.setGeometry(QRect(790, 890, 131, 71))
        self.btn_refresh = QPushButton(self.tab_4)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(200, 930, 61, 25))
        self.btn_run_tpa = QPushButton(self.tab_4)
        self.btn_run_tpa.setObjectName(u"btn_run_tpa")
        self.btn_run_tpa.setGeometry(QRect(1010, 850, 131, 101))
        self.btn_show_sigma_2 = QPushButton(self.tab_4)
        self.btn_show_sigma_2.setObjectName(u"btn_show_sigma_2")
        self.btn_show_sigma_2.setGeometry(QRect(20, 870, 121, 71))
        self.FPSpectrum_2 = PlotWidget(self.tab_4)
        self.FPSpectrum_2.setObjectName(u"FPSpectrum_2")
        self.FPSpectrum_2.setGeometry(QRect(870, 10, 651, 251))
        self.label_f_5 = QLabel(self.tab_4)
        self.label_f_5.setObjectName(u"label_f_5")
        self.label_f_5.setGeometry(QRect(360, 760, 111, 20))
        self.label_P_5 = QLabel(self.tab_4)
        self.label_P_5.setObjectName(u"label_P_5")
        self.label_P_5.setGeometry(QRect(490, 760, 91, 21))
        self.label_Quad_5 = QLabel(self.tab_4)
        self.label_Quad_5.setObjectName(u"label_Quad_5")
        self.label_Quad_5.setGeometry(QRect(600, 760, 121, 21))
        self.ls_terminal_information_for_users_measurement = QListWidget(self.tab_4)
        self.ls_terminal_information_for_users_measurement.setObjectName(u"ls_terminal_information_for_users_measurement")
        self.ls_terminal_information_for_users_measurement.setGeometry(QRect(950, 280, 571, 531))
        self.ls_terminal_information_for_users_measurement.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.ls_terminal_information_for_users_measurement.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ls_terminal_information_for_users_measurement.setSelectionMode(QAbstractItemView.NoSelection)
        self.ls_terminal_information_for_users_measurement.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ls_terminal_information_for_users_measurement.setMovement(QListView.Free)
        self.btn_simulation = QPushButton(self.tab_4)
        self.btn_simulation.setObjectName(u"btn_simulation")
        self.btn_simulation.setGeometry(QRect(790, 610, 131, 81))
        self.progressbar_measurement = QProgressBar(self.tab_4)
        self.progressbar_measurement.setObjectName(u"progressbar_measurement")
        self.progressbar_measurement.setGeometry(QRect(1250, 860, 261, 23))
        self.progressbar_measurement.setValue(0)
        self.btn_experiment_status_2 = QPushButton(self.tab_4)
        self.btn_experiment_status_2.setObjectName(u"btn_experiment_status_2")
        self.btn_experiment_status_2.setGeometry(QRect(1250, 900, 261, 25))
        self.btn_experiment_status_2.setMaximumSize(QSize(16777215, 16777215))
        self.btn_experiment_status_2.setFlat(False)
        self.ls_measure_data = QListWidget(self.tab_4)
        self.ls_measure_data.setObjectName(u"ls_measure_data")
        self.ls_measure_data.setGeometry(QRect(330, 600, 421, 391))
        self.ls_measure_data.setSelectionMode(QAbstractItemView.MultiSelection)
        self.ls_measure_data.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.label_19 = QLabel(self.tab_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(320, 560, 61, 20))
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.btn_reset_power_angle_conversion_file = QPushButton(self.tab)
        self.btn_reset_power_angle_conversion_file.setObjectName(u"btn_reset_power_angle_conversion_file")
        self.btn_reset_power_angle_conversion_file.setGeometry(QRect(1150, 590, 351, 101))
        self.btn_filter_FF01650 = QRadioButton(self.tab)
        self.btn_filter_FF01650.setObjectName(u"btn_filter_FF01650")
        self.btn_filter_FF01650.setGeometry(QRect(120, 90, 191, 17))
        self.btn_filter_E650sp2p = QRadioButton(self.tab)
        self.btn_filter_E650sp2p.setObjectName(u"btn_filter_E650sp2p")
        self.btn_filter_E650sp2p.setGeometry(QRect(120, 130, 201, 17))
        self.btn_filter_E750sp2p = QRadioButton(self.tab)
        self.btn_filter_E750sp2p.setObjectName(u"btn_filter_E750sp2p")
        self.btn_filter_E750sp2p.setGeometry(QRect(120, 170, 191, 17))
        self.btn_filter_E650 = QRadioButton(self.tab)
        self.btn_filter_E650.setObjectName(u"btn_filter_E650")
        self.btn_filter_E650.setGeometry(QRect(120, 210, 82, 17))
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 40, 131, 16))
        self.btn_filter_FES700 = QRadioButton(self.tab)
        self.btn_filter_FES700.setObjectName(u"btn_filter_FES700")
        self.btn_filter_FES700.setGeometry(QRect(120, 250, 82, 17))
        self.btn_filter_FES750 = QRadioButton(self.tab)
        self.btn_filter_FES750.setObjectName(u"btn_filter_FES750")
        self.btn_filter_FES750.setGeometry(QRect(120, 290, 82, 17))
        self.btn_filter_FES800 = QRadioButton(self.tab)
        self.btn_filter_FES800.setObjectName(u"btn_filter_FES800")
        self.btn_filter_FES800.setGeometry(QRect(120, 330, 82, 17))
        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_19.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.ls_terminal_calibration.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.spb_integration.setSuffix(QCoreApplication.translate("Form", u" ms", None))
        self.ckb_super_fast.setText(QCoreApplication.translate("Form", u"Super-Fast", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Scan", None))
        self.btn_jod.setText(QCoreApplication.translate("Form", u"JOD", None))
        self.btn_dmans.setText(QCoreApplication.translate("Form", u"DMANs", None))
        self.btn_calibration.setText(QCoreApplication.translate("Form", u"Run CCD calibration", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Intensity", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">10</span><span style=\" font-size:12pt; vertical-align:super;\">6</span><span style=\" font-size:12pt;\"> cps</span></p></body></html>", None))
        self.btn_zero_intensity.setText(QCoreApplication.translate("Form", u"Zero", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Laser wavelength", None))
        self.spb_wavelength_tuning.setSuffix(QCoreApplication.translate("Form", u" nm", None))
        self.btn_set_wavelength.setText(QCoreApplication.translate("Form", u"Set wavelength", None))
        self.btn_go.setText(QCoreApplication.translate("Form", u"Go", None))
        self.btn_stop.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.btn_reset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.label.setText(QCoreApplication.translate("Form", u"Power", None))
        self.btn_zero_power.setText(QCoreApplication.translate("Form", u"Zero", None))
        self.label_dial_power.setText("")
        self.btn_experiment_status.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Calibration", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Reference", None))
        self.btn_set_fluorescein.setText(QCoreApplication.translate("Form", u"Fluorescein", None))
        self.btn_set_nile_red.setText(QCoreApplication.translate("Form", u"Nile Red", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Concentration", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"mol/L", None))
        self.btn_check_calibration.setText(QCoreApplication.translate("Form", u"Calibration", None))
        self.btn_check_reference.setText(QCoreApplication.translate("Form", u"Reference", None))
        self.btn_check_samples.setText(QCoreApplication.translate("Form", u"Sample(s)", None))
        self.btn_check_power.setText(QCoreApplication.translate("Form", u"Power range", None))
        self.btn_check_wavelength.setText(QCoreApplication.translate("Form", u"Wavelength range", None))
        self.btn_create_sample_number.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Sample", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Name of the sample", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Emission file", None))
        self.btn_delete_sample.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Concentration of the sample", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"mol/L", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Fluorescence QY of the sample", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Solvent", None))
        self.btn_sample_info.setText(QCoreApplication.translate("Form", u"Infos", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Wavelength range", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Start at</span></p></body></html>", None))
        self.spb_set_wavelength_min.setSuffix(QCoreApplication.translate("Form", u" nm", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Steps</span></p></body></html>", None))
        self.spb_set_wavelength_pitch.setSuffix(QCoreApplication.translate("Form", u" nm", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Finish at</span></p></body></html>", None))
        self.spb_set_wavelength_max.setSuffix(QCoreApplication.translate("Form", u" nm", None))
        self.btn_check_opo.setText(QCoreApplication.translate("Form", u"OPO", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Power range", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Start at</span></p></body></html>", None))
        self.spb_set_power_max.setSuffix(QCoreApplication.translate("Form", u" mW", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Finish at</span></p></body></html>", None))
        self.spb_set_power_min.setSuffix(QCoreApplication.translate("Form", u" mW", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Steps</span></p></body></html>", None))
        self.spb_set_number_of_power_measure.setSuffix("")
        self.label_25.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("Form", u"Parameters", None))
        self.btn_set_sample.setText(QCoreApplication.translate("Form", u"Sample", None))
        self.btn_set_sample_wavelength.setText(QCoreApplication.translate("Form", u"Wavelength", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"F", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"P", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"F/P\u00b2", None))
        self.btn_new_measure_data.setText(QCoreApplication.translate("Form", u"New Measure", None))
        self.btn_remove_data.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.btn_refresh.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.btn_run_tpa.setText(QCoreApplication.translate("Form", u"RUN", None))
        self.btn_show_sigma_2.setText(QCoreApplication.translate("Form", u"Show Sigma 2", None))
        self.label_f_5.setText("")
        self.label_P_5.setText("")
        self.label_Quad_5.setText("")
        self.btn_simulation.setText(QCoreApplication.translate("Form", u"Simulation", None))
        self.btn_experiment_status_2.setText("")
        self.label_19.setText(QCoreApplication.translate("Form", u"#", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Measurement", None))
        self.btn_reset_power_angle_conversion_file.setText(QCoreApplication.translate("Form", u"Reset Power angle conversion file", None))
        self.btn_filter_FF01650.setText(QCoreApplication.translate("Form", u"Semrock FF01-650/SP25", None))
        self.btn_filter_E650sp2p.setText(QCoreApplication.translate("Form", u"Chroma E650sp-2p", None))
        self.btn_filter_E750sp2p.setText(QCoreApplication.translate("Form", u"Chroma E750sp-2p", None))
        self.btn_filter_E650.setText(QCoreApplication.translate("Form", u"E650", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Emission filter", None))
        self.btn_filter_FES700.setText(QCoreApplication.translate("Form", u"FES700", None))
        self.btn_filter_FES750.setText(QCoreApplication.translate("Form", u"FES750", None))
        self.btn_filter_FES800.setText(QCoreApplication.translate("Form", u"FES800", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Advanced calibration", None))
    # retranslateUi

