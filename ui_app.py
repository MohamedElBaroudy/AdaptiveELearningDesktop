# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_app.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 910)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Desktop/project-icons and images/icons/ninja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("border:none;")
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.register_tab = QtWidgets.QWidget()
        self.register_tab.setStyleSheet("background-color:#ffffff;")
        self.register_tab.setObjectName("register_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.register_tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.register_tab)
        self.frame_3.setStyleSheet("background-color:#b60006;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.register_tab)
        self.frame_2.setMaximumSize(QtCore.QSize(400, 400))
        self.frame_2.setStyleSheet("QFrame{bacKground-color:#b60006;}\n"
"\n"
"QLineEdit{\n"
"background-color: #ffffff;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QGroupBox{\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QRadioButton{\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:#a30000;\n"
"font-size: 16px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.register_email = QtWidgets.QLineEdit(self.frame_2)
        self.register_email.setMinimumSize(QtCore.QSize(0, 30))
        self.register_email.setStyleSheet("background-color:#ffffff;\n"
"border:none;")
        self.register_email.setAlignment(QtCore.Qt.AlignCenter)
        self.register_email.setObjectName("register_email")
        self.gridLayout_3.addWidget(self.register_email, 1, 0, 1, 2)
        self.register_password = QtWidgets.QLineEdit(self.frame_2)
        self.register_password.setMinimumSize(QtCore.QSize(50, 30))
        self.register_password.setStyleSheet("border:none;\n"
"background-color:#ffffff;\n"
"")
        self.register_password.setAlignment(QtCore.Qt.AlignCenter)
        self.register_password.setObjectName("register_password")
        self.gridLayout_3.addWidget(self.register_password, 3, 0, 1, 2)
        self.date_of_birth_label = QtWidgets.QLabel(self.frame_2)
        self.date_of_birth_label.setMinimumSize(QtCore.QSize(0, 30))
        self.date_of_birth_label.setStyleSheet("color:#ffffff;")
        self.date_of_birth_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_of_birth_label.setObjectName("date_of_birth_label")
        self.gridLayout_3.addWidget(self.date_of_birth_label, 6, 0, 1, 1)
        self.first_name = QtWidgets.QLineEdit(self.frame_2)
        self.first_name.setMinimumSize(QtCore.QSize(0, 30))
        self.first_name.setAlignment(QtCore.Qt.AlignCenter)
        self.first_name.setObjectName("first_name")
        self.gridLayout_3.addWidget(self.first_name, 0, 0, 1, 1)
        self.register_username = QtWidgets.QLineEdit(self.frame_2)
        self.register_username.setMinimumSize(QtCore.QSize(0, 30))
        self.register_username.setAlignment(QtCore.Qt.AlignCenter)
        self.register_username.setObjectName("register_username")
        self.gridLayout_3.addWidget(self.register_username, 2, 0, 1, 2)
        self.register_confirm_password = QtWidgets.QLineEdit(self.frame_2)
        self.register_confirm_password.setMinimumSize(QtCore.QSize(0, 30))
        self.register_confirm_password.setAlignment(QtCore.Qt.AlignCenter)
        self.register_confirm_password.setObjectName("register_confirm_password")
        self.gridLayout_3.addWidget(self.register_confirm_password, 4, 0, 1, 2)
        self.last_name = QtWidgets.QLineEdit(self.frame_2)
        self.last_name.setMinimumSize(QtCore.QSize(0, 30))
        self.last_name.setAlignment(QtCore.Qt.AlignCenter)
        self.last_name.setObjectName("last_name")
        self.gridLayout_3.addWidget(self.last_name, 0, 1, 1, 1)
        self.male_female_groubbox = QtWidgets.QGroupBox(self.frame_2)
        self.male_female_groubbox.setMinimumSize(QtCore.QSize(0, 70))
        self.male_female_groubbox.setStyleSheet("background-color:transparent;\n"
"color:#ffffff;")
        self.male_female_groubbox.setAlignment(QtCore.Qt.AlignCenter)
        self.male_female_groubbox.setObjectName("male_female_groubbox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.male_female_groubbox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.male = QtWidgets.QRadioButton(self.male_female_groubbox)
        self.male.setMinimumSize(QtCore.QSize(0, 30))
        self.male.setObjectName("male")
        self.horizontalLayout.addWidget(self.male)
        self.female = QtWidgets.QRadioButton(self.male_female_groubbox)
        self.female.setMinimumSize(QtCore.QSize(0, 30))
        self.female.setObjectName("female")
        self.horizontalLayout.addWidget(self.female)
        self.gridLayout_3.addWidget(self.male_female_groubbox, 5, 0, 1, 2)
        self.register_button = QtWidgets.QPushButton(self.frame_2)
        self.register_button.setMinimumSize(QtCore.QSize(50, 50))
        self.register_button.setStyleSheet("background-color:#e2161d;\n"
"color:#ffffff;\n"
"border:none;")
        self.register_button.setObjectName("register_button")
        self.gridLayout_3.addWidget(self.register_button, 9, 0, 1, 2)
        self.register_login_button = QtWidgets.QPushButton(self.frame_2)
        self.register_login_button.setMinimumSize(QtCore.QSize(50, 50))
        self.register_login_button.setStyleSheet("background-color:#e2161d;\n"
"color:#ffffff;\n"
"border:none;")
        self.register_login_button.setObjectName("register_login_button")
        self.gridLayout_3.addWidget(self.register_login_button, 10, 1, 1, 1)
        self.already_have_account_label = QtWidgets.QLabel(self.frame_2)
        self.already_have_account_label.setStyleSheet("color:#ffffff;")
        self.already_have_account_label.setAlignment(QtCore.Qt.AlignCenter)
        self.already_have_account_label.setObjectName("already_have_account_label")
        self.gridLayout_3.addWidget(self.already_have_account_label, 10, 0, 1, 1)
        self.date_of_birth = QtWidgets.QDateEdit(self.frame_2)
        self.date_of_birth.setMinimumSize(QtCore.QSize(0, 30))
        self.date_of_birth.setObjectName("date_of_birth")
        self.gridLayout_3.addWidget(self.date_of_birth, 6, 1, 2, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.register_tab)
        self.frame_4.setStyleSheet("background-color:#b60006;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2.addWidget(self.frame_4, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.register_tab)
        self.frame.setStyleSheet("background-color:#b60006;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_20 = QtWidgets.QFrame(self.frame)
        self.frame_20.setGeometry(QtCore.QRect(30, 0, 248, 270))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.targaryen_label_3 = QtWidgets.QLabel(self.frame_20)
        self.targaryen_label_3.setMaximumSize(QtCore.QSize(16777215, 265))
        self.targaryen_label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.targaryen_label_3.setObjectName("targaryen_label_3")
        self.gridLayout_17.addWidget(self.targaryen_label_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 3, 1)
        self.tabWidget.addTab(self.register_tab, "")
        self.login_tab = QtWidgets.QWidget()
        self.login_tab.setObjectName("login_tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.login_tab)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_12 = QtWidgets.QFrame(self.login_tab)
        self.frame_12.setStyleSheet("background-color:#b60006;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setGeometry(QtCore.QRect(60, 0, 248, 270))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.targaryen_label = QtWidgets.QLabel(self.frame_14)
        self.targaryen_label.setMaximumSize(QtCore.QSize(16777215, 265))
        self.targaryen_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.targaryen_label.setObjectName("targaryen_label")
        self.gridLayout_10.addWidget(self.targaryen_label, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_12, 0, 0, 3, 1)
        self.frame_11 = QtWidgets.QFrame(self.login_tab)
        self.frame_11.setStyleSheet("background-color:#b60006;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_9.addWidget(self.frame_11, 0, 1, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.login_tab)
        self.frame_10.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_10.setMaximumSize(QtCore.QSize(301, 301))
        self.frame_10.setStyleSheet("QFrame{bacKground-color:#b60006;}\n"
"\n"
"QLineEdit{\n"
"background-color: #ffffff;\n"
"font-size: 14px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QGroupBox{\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QRadioButton{\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#e2161d;\n"
"color:#ffffff;\n"
"font-size: 16px;\n"
"border:none;\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.username_or_email = QtWidgets.QLineEdit(self.frame_10)
        self.username_or_email.setMinimumSize(QtCore.QSize(0, 30))
        self.username_or_email.setStyleSheet("background-color:#ffffff;\n"
"border:none;")
        self.username_or_email.setAlignment(QtCore.Qt.AlignCenter)
        self.username_or_email.setObjectName("username_or_email")
        self.gridLayout_8.addWidget(self.username_or_email, 0, 0, 1, 2)
        self.password = QtWidgets.QLineEdit(self.frame_10)
        self.password.setMinimumSize(QtCore.QSize(50, 30))
        self.password.setStyleSheet("border:none;\n"
"background-color:#ffffff;\n"
"")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.gridLayout_8.addWidget(self.password, 1, 0, 1, 2)
        self.login_button = QtWidgets.QPushButton(self.frame_10)
        self.login_button.setMinimumSize(QtCore.QSize(50, 50))
        self.login_button.setStyleSheet("\n"
"")
        self.login_button.setObjectName("login_button")
        self.gridLayout_8.addWidget(self.login_button, 2, 0, 1, 1)
        self.forgot_password_button = QtWidgets.QPushButton(self.frame_10)
        self.forgot_password_button.setMinimumSize(QtCore.QSize(50, 50))
        self.forgot_password_button.setStyleSheet("")
        self.forgot_password_button.setObjectName("forgot_password_button")
        self.gridLayout_8.addWidget(self.forgot_password_button, 2, 1, 1, 1)
        self.gridLayout_9.addWidget(self.frame_10, 1, 1, 1, 1)
        self.frame_15 = QtWidgets.QFrame(self.login_tab)
        self.frame_15.setStyleSheet("background-color:#b60006;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_9.addWidget(self.frame_15, 2, 1, 1, 1)
        self.tabWidget.addTab(self.login_tab, "")
        self.application_tab = QtWidgets.QWidget()
        self.application_tab.setObjectName("application_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.application_tab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_5 = QtWidgets.QFrame(self.application_tab)
        self.frame_5.setStyleSheet("background-color:#ffffff;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_8.setStyleSheet("QFrame{\n"
"background-color:#004777;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:checked,QPushButton:pressed{\n"
"background-color:#00afb5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#00afb5;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.ninja_label = QtWidgets.QPushButton(self.frame_8)
        self.ninja_label.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.ninja_label.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.ninja_label.setStyleSheet("border-style:hidden;\n"
"")
        self.ninja_label.setText("")
        self.ninja_label.setIcon(icon)
        self.ninja_label.setAutoExclusive(False)
        self.ninja_label.setObjectName("ninja_label")
        self.gridLayout_4.addWidget(self.frame_8, 0, 0, 1, 2)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("background-color:#efd28d;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame_7)
        self.tabWidget_2.setStyleSheet("border:none")
        self.tabWidget_2.setTabBarAutoHide(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.tabWidget_2.addTab(self.home_tab, "")
        self.my_courses_tab = QtWidgets.QWidget()
        self.my_courses_tab.setObjectName("my_courses_tab")
        self.tabWidget_2.addTab(self.my_courses_tab, "")
        self.my_classrooms_tab = QtWidgets.QWidget()
        self.my_classrooms_tab.setObjectName("my_classrooms_tab")
        self.tabWidget_2.addTab(self.my_classrooms_tab, "")
        self.teacher_dashboard_tab = QtWidgets.QWidget()
        self.teacher_dashboard_tab.setObjectName("teacher_dashboard_tab")
        self.tabWidget_2.addTab(self.teacher_dashboard_tab, "")
        self.parent_dashboard_tab = QtWidgets.QWidget()
        self.parent_dashboard_tab.setObjectName("parent_dashboard_tab")
        self.tabWidget_2.addTab(self.parent_dashboard_tab, "")
        self.saved_courses_tab = QtWidgets.QWidget()
        self.saved_courses_tab.setObjectName("saved_courses_tab")
        self.tabWidget_2.addTab(self.saved_courses_tab, "")
        self.accomplished_courses_tab = QtWidgets.QWidget()
        self.accomplished_courses_tab.setObjectName("accomplished_courses_tab")
        self.tabWidget_2.addTab(self.accomplished_courses_tab, "")
        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_7, 1, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_6.setStyleSheet("QFrame{\n"
"background-color:#ff7700;\n"
"color:#fff5dc;\n"
"}\n"
"\n"
"QToolButton{\n"
"background-color:transparent;\n"
"color:#fff5dc;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed{\n"
"background-color:#e66b00;\n"
"}\n"
"QToolButton:hover{\n"
"background-color:#e66b00;\n"
"}\n"
"QToolButton::checked:hover{\n"
"background-color:#red;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_button = QtWidgets.QToolButton(self.frame_6)
        self.home_button.setMinimumSize(QtCore.QSize(174, 0))
        self.home_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.home_button.setStyleSheet("")
        self.home_button.setAutoExclusive(True)
        self.home_button.setObjectName("home_button")
        self.verticalLayout.addWidget(self.home_button)
        self.my_courses_button = QtWidgets.QToolButton(self.frame_6)
        self.my_courses_button.setMinimumSize(QtCore.QSize(174, 0))
        self.my_courses_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.my_courses_button.setStyleSheet("")
        self.my_courses_button.setAutoExclusive(True)
        self.my_courses_button.setObjectName("my_courses_button")
        self.verticalLayout.addWidget(self.my_courses_button)
        self.my_classrooms_button = QtWidgets.QToolButton(self.frame_6)
        self.my_classrooms_button.setMinimumSize(QtCore.QSize(174, 0))
        self.my_classrooms_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.my_classrooms_button.setStyleSheet("")
        self.my_classrooms_button.setAutoExclusive(True)
        self.my_classrooms_button.setObjectName("my_classrooms_button")
        self.verticalLayout.addWidget(self.my_classrooms_button)
        self.teacher_dashboard_button = QtWidgets.QToolButton(self.frame_6)
        self.teacher_dashboard_button.setMinimumSize(QtCore.QSize(174, 0))
        self.teacher_dashboard_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.teacher_dashboard_button.setStyleSheet("")
        self.teacher_dashboard_button.setAutoExclusive(True)
        self.teacher_dashboard_button.setObjectName("teacher_dashboard_button")
        self.verticalLayout.addWidget(self.teacher_dashboard_button)
        self.parent_dashboard_button = QtWidgets.QToolButton(self.frame_6)
        self.parent_dashboard_button.setMinimumSize(QtCore.QSize(174, 0))
        self.parent_dashboard_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.parent_dashboard_button.setStyleSheet("")
        self.parent_dashboard_button.setAutoExclusive(True)
        self.parent_dashboard_button.setObjectName("parent_dashboard_button")
        self.verticalLayout.addWidget(self.parent_dashboard_button)
        self.saved_courses_button = QtWidgets.QToolButton(self.frame_6)
        self.saved_courses_button.setMinimumSize(QtCore.QSize(174, 0))
        self.saved_courses_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.saved_courses_button.setStyleSheet("")
        self.saved_courses_button.setAutoExclusive(True)
        self.saved_courses_button.setObjectName("saved_courses_button")
        self.verticalLayout.addWidget(self.saved_courses_button)
        self.accomplished_courses_button = QtWidgets.QToolButton(self.frame_6)
        self.accomplished_courses_button.setMinimumSize(QtCore.QSize(174, 0))
        self.accomplished_courses_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.accomplished_courses_button.setStyleSheet("")
        self.accomplished_courses_button.setAutoExclusive(True)
        self.accomplished_courses_button.setObjectName("accomplished_courses_button")
        self.verticalLayout.addWidget(self.accomplished_courses_button)
        self.exit_button = QtWidgets.QToolButton(self.frame_6)
        self.exit_button.setMinimumSize(QtCore.QSize(174, 0))
        self.exit_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.exit_button.setStyleSheet("")
        self.exit_button.setAutoExclusive(True)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        self.gridLayout_4.addWidget(self.frame_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.application_tab, "")
        self.admin_tab = QtWidgets.QWidget()
        self.admin_tab.setObjectName("admin_tab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.admin_tab)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame_18 = QtWidgets.QFrame(self.admin_tab)
        self.frame_18.setMaximumSize(QtCore.QSize(478, 430))
        self.frame_18.setStyleSheet("background-color:#ff7700;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_18)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.gridLayout_15.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_18, 2, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.admin_tab)
        self.frame_9.setMaximumSize(QtCore.QSize(478, 429))
        self.frame_9.setStyleSheet("background-color:#ff7700;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout_14.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_9, 0, 0, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.admin_tab)
        self.frame_19.setMaximumSize(QtCore.QSize(478, 430))
        self.frame_19.setStyleSheet("QFrame{background-color:#ff7700;}\n"
"\n"
"QLineEdit{\n"
"border:none;\n"
"background-color:#ffffff;\n"
"}\n"
"\n"
"QPushButton{\n"
"border:none;\n"
"background:#e2161d;\n"
"color:#ffffff;\n"
"}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_16.setContentsMargins(100, 100, 100, 100)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.category_to_be_approved = QtWidgets.QLineEdit(self.frame_19)
        self.category_to_be_approved.setMinimumSize(QtCore.QSize(0, 0))
        self.category_to_be_approved.setMaximumSize(QtCore.QSize(100, 50))
        self.category_to_be_approved.setAlignment(QtCore.Qt.AlignCenter)
        self.category_to_be_approved.setObjectName("category_to_be_approved")
        self.gridLayout_16.addWidget(self.category_to_be_approved, 0, 0, 1, 1)
        self.approve_category = QtWidgets.QPushButton(self.frame_19)
        self.approve_category.setMaximumSize(QtCore.QSize(100, 50))
        self.approve_category.setObjectName("approve_category")
        self.gridLayout_16.addWidget(self.approve_category, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_19, 2, 1, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.admin_tab)
        self.frame_16.setMaximumSize(QtCore.QSize(478, 430))
        self.frame_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_16.setStyleSheet("QFrame{background-color:#ff7700;}\n"
"\n"
"QLineEdit{\n"
"border:none;\n"
"background-color:#ffffff;\n"
"}\n"
"\n"
"QPushButton{\n"
"border:none;\n"
"background:#e2161d;\n"
"color:#ffffff;\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_13.setContentsMargins(100, 100, 100, 100)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.approve_teaching = QtWidgets.QPushButton(self.frame_16)
        self.approve_teaching.setMaximumSize(QtCore.QSize(100, 50))
        self.approve_teaching.setObjectName("approve_teaching")
        self.gridLayout_13.addWidget(self.approve_teaching, 2, 0, 1, 1)
        self.claimer_id = QtWidgets.QLineEdit(self.frame_16)
        self.claimer_id.setMinimumSize(QtCore.QSize(0, 0))
        self.claimer_id.setMaximumSize(QtCore.QSize(100, 50))
        self.claimer_id.setAlignment(QtCore.Qt.AlignCenter)
        self.claimer_id.setObjectName("claimer_id")
        self.gridLayout_13.addWidget(self.claimer_id, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_16, 0, 1, 1, 1)
        self.tabWidget.addTab(self.admin_tab, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.exit_button.clicked.connect(MainWindow.close)
        self.ninja_label.clicked.connect(self.home_button.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ninja Learning"))
        self.register_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.register_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.date_of_birth_label.setText(_translate("MainWindow", "Date of birth"))
        self.first_name.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.register_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.register_confirm_password.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.last_name.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.male_female_groubbox.setTitle(_translate("MainWindow", "Gender"))
        self.male.setText(_translate("MainWindow", "Male"))
        self.female.setText(_translate("MainWindow", "Female"))
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.register_login_button.setText(_translate("MainWindow", " Login"))
        self.already_have_account_label.setText(_translate("MainWindow", "Already Have Account ?"))
        self.targaryen_label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/resources/index2_updated.png\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.register_tab), _translate("MainWindow", "Register"))
        self.targaryen_label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/resources/index2_updated.png\"/></p></body></html>"))
        self.username_or_email.setPlaceholderText(_translate("MainWindow", "Username or Email"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.forgot_password_button.setText(_translate("MainWindow", "Forgot password ?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login_tab), _translate("MainWindow", "Login"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.home_tab), _translate("MainWindow", "Home"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.my_courses_tab), _translate("MainWindow", "My Courses"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.my_classrooms_tab), _translate("MainWindow", "My Classrooms"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.teacher_dashboard_tab), _translate("MainWindow", "Teacher Dashboard"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.parent_dashboard_tab), _translate("MainWindow", "Parent Dashboard"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.saved_courses_tab), _translate("MainWindow", "Saved_Courses"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.accomplished_courses_tab), _translate("MainWindow", "Accomplished Courses"))
        self.home_button.setText(_translate("MainWindow", "Home"))
        self.my_courses_button.setText(_translate("MainWindow", "My Courses"))
        self.my_classrooms_button.setText(_translate("MainWindow", "My Classrooms"))
        self.teacher_dashboard_button.setText(_translate("MainWindow", "Teacher Dashboard"))
        self.parent_dashboard_button.setText(_translate("MainWindow", "Parent Dashboard"))
        self.saved_courses_button.setText(_translate("MainWindow", "Saved Courses"))
        self.accomplished_courses_button.setText(_translate("MainWindow", "Accomplished Courses"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.application_tab), _translate("MainWindow", "Application"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "category"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "claimer id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "claimer name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "claimer email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "is approved"))
        self.category_to_be_approved.setPlaceholderText(_translate("MainWindow", "category"))
        self.approve_category.setText(_translate("MainWindow", "approve"))
        self.approve_teaching.setText(_translate("MainWindow", "approve"))
        self.claimer_id.setPlaceholderText(_translate("MainWindow", "id of claimer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.admin_tab), _translate("MainWindow", "Administrator"))

import targaryen_rc
