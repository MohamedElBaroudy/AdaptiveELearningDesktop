# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import dragon
import requests
import json
from validate_email import validate_email
import datetime
from Constants import mapping, parameters


class Dragon(QMainWindow, dragon.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        local_server = "http://localhost:8080"
        online_server = "https://graduation-server.herokuapp.com"
        self.server = online_server

        self.tabWidget.tabBar().hide()
        self.application_tab_2.tabBar().hide()
        self.tabWidget.setCurrentIndex(0)
        self.application_tab_2.setCurrentIndex(0)

        # Register page buttons
        self.register_login_button.clicked.connect(self.enter_login_page)
        self.register_button.clicked.connect(self.register)

        # Login page buttons
        self.forgot_password_button.clicked.connect(self.button_not_implemented_yet)
        self.login_button.clicked.connect(self.login)
        self.login_register_button.clicked.connect(self.enter_register_page)

        # Application buttons
        # Main tabs
        self.home_button.clicked.connect(self.enter_home_page)
        self.my_courses_button.clicked.connect(self.enter_my_courses_page)
        self.my_classrooms_button.clicked.connect(self.enter_my_classrooms_page)
        self.teacher_dashboard_button.clicked.connect(self.enter_teacher_dashboard_page)
        self.parent_dashboard_button.clicked.connect(self.enter_parent_dashboard_page)
        self.saved_courses_button.clicked.connect(self.enter_saved_courses_page)
        self.accomplished_courses_button.clicked.connect(self.enter_accomplished_courses_page)
        self.admin_button.clicked.connect(self.enter_admin_dashboard_page)
        self.profile_button.clicked.connect(self.enter_profile_page)
        # Admin dashboard buttons
        self.reload_teaching_request.clicked.connect(self.update_teaching_request)
        self.approve_teaching.clicked.connect(self.approve_teaching_request)
        self.reload_category_request.clicked.connect(self.update_category_request)

    def button_not_implemented_yet(self):
        QMessageBox.warning(self, "Warning", "Not implementd yet.")

    def enter_login_page(self):
        self.tabWidget.setCurrentIndex(1)

    def enter_register_page(self):
        self.tabWidget.setCurrentIndex(0)

    def enter_home_page(self):
        self.application_tab_2.setCurrentIndex(0)

    def enter_my_courses_page(self):
        self.application_tab_2.setCurrentIndex(1)

    def enter_my_classrooms_page(self):
        self.application_tab_2.setCurrentIndex(2)

    def enter_teacher_dashboard_page(self):
        self.application_tab_2.setCurrentIndex(3)

    def enter_parent_dashboard_page(self):
        self.application_tab_2.setCurrentIndex(4)

    def enter_saved_courses_page(self):
        self.application_tab_2.setCurrentIndex(5)

    def enter_accomplished_courses_page(self):
        self.application_tab_2.setCurrentIndex(6)

    def enter_profile_page(self):
        self.application_tab_2.setCurrentIndex(7)

    def enter_admin_dashboard_page(self):
        self.application_tab_2.setCurrentIndex(8)

    def register(self):
        warnings = []
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        username = self.register_username.text()
        email = self.register_email.text()
        password = self.register_password.text()
        confirm_password = self.register_confirm_password.text()
        gender = "0"
        if self.male.isChecked():
            gender = "1"
        elif self.female.isChecked():
            gender = "2"
        date_of_birth = self.date_of_birth.text().split("/")
        if len(date_of_birth[0]) < 2:
            date_of_birth[0] = "0" + date_of_birth[0]
        if len(date_of_birth[1]) < 2:
            date_of_birth[1] = "0" + date_of_birth[1]
        date_of_birth_string = date_of_birth[2] + "-" + date_of_birth[0] + "-" + date_of_birth[1]
        if first_name == "" or len(first_name) < 2:
            warnings.apppend('Enter a valid first name')
        if last_name == "" or len(last_name) < 2:
            warnings.apppend('Enter a valid last name')
        if username == "" or len(username) < 4:
            warnings.apppend('Enter a valid username')
        if not validate_email(email):
            warnings.apppend('Enter a valid email')
        if len(password) < 8 or password != confirm_password:
            warnings.append('enter a valid password and confirm it correctly')
        if gender != "1" and gender != "2":
            warnings.append('You must choose your gender')
        age = int(datetime.datetime.now().year) - int(date_of_birth[2])
        if age < 12:
            warnings.append('You supposed to registered by your parent')
        if len(warnings) > 0:
            QMessageBox.Warning(self, "Warnings", " , ".join(warnings))
            return
        request = (self.server + mapping.REGISTER + "?"
                                 + parameters.FIRST_NAME + "=" + first_name + "&"
                                 + parameters.LAST_NAME + "=" + last_name + "&"
                                 + parameters.EMAIL + "=" + email + "&"
                                 + parameters.USERNAME + "=" + username + "&"
                                 + parameters.PASSWORD + "=" + password + "&"
                                 + parameters.GENDER + "=" + gender + "&"
                                 + parameters.DATE_OF_BIRTH + "=" + date_of_birth_string)
        response = requests.post(request)
        if response.status_code == 200:
            QMessageBox.information(self, "Info", "Created Successfully.")
            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Warning", response.text + " with code :" + str(response.status_code))

    def login(self):
        warnings = []
        username = ""
        email = ""
        username_or_email = self.username_or_email.text()
        password = self.password.text()
        if username_or_email == "" or len(username_or_email) < 4:
            warnings.append('Enter a valid username')
        if len(password) < 8:
            warnings.append('enter a valid password')
        if len(warnings) > 0:
            QMessageBox.Warning(self, "Warnings", ",".join(warnings))
            return
        request = ""
        if validate_email(username_or_email):
            email = username_or_email
            request = (self.server + mapping.LOGIN + "?"
                       + parameters.EMAIL + "=" + email + "&"
                       + parameters.PASSWORD + "=" + password)
        else:
            username = username_or_email
            request = (self.server + mapping.LOGIN + "?"
                       + parameters.USERNAME + "=" + username + "&"
                       + parameters.PASSWORD + "=" + password)
        response = requests.get(request)
        if response.status_code != 200:
            QMessageBox.warning(self, "Warning", response.text)
            return
        self.token = response.text
        if username_or_email != "Admin" and username_or_email != "admin@gmail.com":
            self.admin_button.setVisible(False)
        self.tabWidget.setCurrentIndex(2)

    def approve_teaching_request(self):
        claimer_id = self.claimer_id.text()
        response = requests.put("http://graduation-server.herokuapp.com/admin/approve_teaching?token="+self.token+"&user_id="+claimer_id)
        self.update_teaching_request()

    def update_teaching_request(self):
        self.tableWidget.setRowCount(0)
        request = (self.server + mapping.REQUESTS + "?"
                   + parameters.ACCESS_TOKEN + "=" + self.token)
        response = requests.get(request)
        table = json.loads(response.text)
        self.tableWidget.setRowCount(len(table))
        for i in range(len(table)):
            request = table[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(request["claimerId"])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(request["claimerName"]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(request["claimerEmail"])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(request["approved"])))

    def update_category_request(self):
        self.tableWidget_2.setRowCount(0)
        request = (self.server + mapping.ALL_CATEGORIES + "?"
                   + parameters.ACCESS_TOKEN + "=" + self.token)
        response = requests.get(request)
        table = json.loads(response.text)
        self.tableWidget_2.setRowCount(len(table))
        for i in range(len(table)):
            request = table[i]
            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(request["categoryId"])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(request["categoryStr"]))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(request["approved"])))


app = QApplication(sys.argv)
dragon = Dragon()
dragon.show()
app.exec_()
