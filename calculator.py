# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(307, 386)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("padding:-10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("padding:-10px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.frame_5)
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout_4.addWidget(self.openGLWidget)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_4.addWidget(self.pushButton_13)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_4.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_4.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_4.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_4.addWidget(self.pushButton_9)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setStyleSheet("padding:-10px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_20.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_5.addWidget(self.pushButton_20)
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_27.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_5.addWidget(self.pushButton_27)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_19.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_5.addWidget(self.pushButton_19)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_18.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_5.addWidget(self.pushButton_18)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_17.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_5.addWidget(self.pushButton_17)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_5.addWidget(self.pushButton_16)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_15.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_5.addWidget(self.pushButton_15)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("padding:-10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_26.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_26.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\delet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon)
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout_6.addWidget(self.pushButton_26)
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_28.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_28.setObjectName("pushButton_28")
        self.verticalLayout_6.addWidget(self.pushButton_28)
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_25.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout_6.addWidget(self.pushButton_25)
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_24.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_6.addWidget(self.pushButton_24)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_23.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout_6.addWidget(self.pushButton_23)
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_22.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: white;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #F2F2F2;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_6.addWidget(self.pushButton_22)
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"            width: fit-content;\n"
"            min-width: 20px;\n"
"            height: 20px;\n"
"            padding: 8px;\n"
"            border-radius: 12px;\n"
"            border: 2.5px solid #E0E1E4;\n"
"            box-shadow: 0px 0px 20px -20px;\n"
"            cursor: pointer;\n"
"            background-color: #0cf30c;\n"
"            transition: all 0.2s ease-in-out 0ms;\n"
"            user-select: none;\n"
"            font-family: \'Poppins\', sans-serif;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #3bdd09;box-shadow: 0px 0px 20px -18px;\n"
"        }")
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_6.addWidget(self.pushButton_21)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>0</p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "2nd"))
        self.pushButton.setText(_translate("Dialog", "("))
        self.pushButton_8.setText(_translate("Dialog", "1/x"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_6.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "1"))
        self.pushButton_4.setText(_translate("Dialog", "+/-"))
        self.pushButton_14.setText(_translate("Dialog", "%"))
        self.pushButton_2.setText(_translate("Dialog", ")"))
        self.pushButton_13.setText(_translate("Dialog", "x²"))
        self.pushButton_12.setText(_translate("Dialog", "8"))
        self.pushButton_11.setText(_translate("Dialog", "5"))
        self.pushButton_10.setText(_translate("Dialog", "2"))
        self.pushButton_9.setText(_translate("Dialog", "0"))
        self.pushButton_20.setText(_translate("Dialog", "C"))
        self.pushButton_27.setText(_translate("Dialog", "n!"))
        self.pushButton_19.setText(_translate("Dialog", "√"))
        self.pushButton_18.setText(_translate("Dialog", "9"))
        self.pushButton_17.setText(_translate("Dialog", "6"))
        self.pushButton_16.setText(_translate("Dialog", "3"))
        self.pushButton_15.setText(_translate("Dialog", "."))
        self.pushButton_28.setText(_translate("Dialog", "π"))
        self.pushButton_25.setText(_translate("Dialog", "÷"))
        self.pushButton_24.setText(_translate("Dialog", "×"))
        self.pushButton_23.setText(_translate("Dialog", "-"))
        self.pushButton_22.setText(_translate("Dialog", "+"))
        self.pushButton_21.setText(_translate("Dialog", "="))
