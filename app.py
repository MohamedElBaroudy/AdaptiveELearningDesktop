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
        self.user = {}
        self.hot_courses = []
        self.new_courses = []
        self.top_courses = []

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
        self.approve_teaching.clicked.connect(self.admin_approve_teaching_request)
        self.reload_category_request.clicked.connect(self.update_category_request)
        self.approve_category.clicked.connect(self.admin_approve_category)
        self.add_category_button.clicked.connect(self.admin_add_category)

    def button_not_implemented_yet(self):
        QMessageBox.warning(self, "Warning", "Not implementd yet.")

    def enter_login_page(self):
        self.tabWidget.setCurrentIndex(1)

    def enter_register_page(self):
        self.tabWidget.setCurrentIndex(0)

    def enter_home_page(self):
        self.application_tab_2.setCurrentIndex(0)
        self.get_hot_courses()
        self.get_new_courses()
        self.get_top_courses()

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

    def set_hot_courses_frames_invisible(self, i):
        if i == 0:
            self.hot_frame1.setVisible(False)
            return
        if i == 1:
            self.hot_frame2.setVisible(False)
            return
        if i == 2:
            self.hot_frame3.setVisible(False)
            return
        if i == 3:
            self.hot_frame4.setVisible(False)
            return
        if i == 4:
            self.hot_frame5.setVisible(False)
            return
        if i == 5:
            self.hot_frame6.setVisible(False)
            return
        if i == 6:
            self.hot_frame7.setVisible(False)
            return
        if i == 7:
            self.hot_frame8.setVisible(False)
            return
        if i == 8:
            self.hot_frame9.setVisible(False)
            return
        if i == 9:
            self.hot_frame10.setVisible(False)
            return

    def hot_courses_frames_occupy(self, i):
        if i == 0:
            self.hot_1_label.setText(self.hot_courses[i]["title"])
            self.hot_1_button.setText("Enroll")
            return
        if i == 1:
            self.hot_2_label.setText(self.hot_courses[i]["title"])
            self.hot_2_button.setText("Enroll")
            return
        if i == 2:
            self.hot_3_label.setText(self.hot_courses[i]["title"])
            self.hot_3_button.setText("Enroll")
            return
        if i == 3:
            self.hot_4_label.setText(self.hot_courses[i]["title"])
            self.hot_4_button.setText("Enroll")
            return
        if i == 4:
            self.hot_5_label.setText(self.hot_courses[i]["title"])
            self.hot_5_button.setText("Enroll")
            return
        if i == 5:
            self.hot_6_label.setText(self.hot_courses[i]["title"])
            self.hot_6_button.setText("Enroll")
            return
        if i == 6:
            self.hot_7_label.setText(self.hot_courses[i]["title"])
            self.hot_7_button.setText("Enroll")
            return
        if i == 7:
            self.hot_8_label.setText(self.hot_courses[i]["title"])
            self.hot_8_button.setText("Enroll")
            return
        if i == 8:
            self.hot_9_label.setText(self.hot_courses[i]["title"])
            self.hot_9_button.setText("Enroll")
            return
        if i == 9:
            self.hot_10_label.setText(self.hot_courses[i]["title"])
            self.hot_10_button.setText("Enroll")
            return

    def set_new_courses_frames_invisible(self, i):
        if i == 0:
            self.new_frame1.setVisible(False)
            return
        if i == 1:
            self.new_frame2.setVisible(False)
            return
        if i == 2:
            self.new_frame3.setVisible(False)
            return
        if i == 3:
            self.new_frame4.setVisible(False)
            return
        if i == 4:
            self.new_frame5.setVisible(False)
            return
        if i == 5:
            self.new_frame6.setVisible(False)
            return
        if i == 6:
            self.new_frame7.setVisible(False)
            return
        if i == 7:
            self.new_frame8.setVisible(False)
            return
        if i == 8:
            self.new_frame9.setVisible(False)
            return
        if i == 9:
            self.new_frame10.setVisible(False)
            return

    def new_courses_frames_occupy(self, i):
        if i == 0:
            self.new_label_1.setText(self.new_courses[i]["title"])
            self.new_button_1.setText("Enroll")
            return
        if i == 1:
            self.new_label_2.setText(self.new_courses[i]["title"])
            self.new_button_2.setText("Enroll")
            return
        if i == 2:
            self.new_label_3.setText(self.new_courses[i]["title"])
            self.new_button_3.setText("Enroll")
            return
        if i == 3:
            self.new_label_4.setText(self.new_courses[i]["title"])
            self.new_button_4.setText("Enroll")
            return
        if i == 4:
            self.new_label_5.setText(self.new_courses[i]["title"])
            self.new_button_5.setText("Enroll")
            return
        if i == 5:
            self.new_label_6.setText(self.new_courses[i]["title"])
            self.new_button_6.setText("Enroll")
            return
        if i == 6:
            self.new_label_7.setText(self.new_courses[i]["title"])
            self.new_button_7.setText("Enroll")
            return
        if i == 7:
            self.new_label_8.setText(self.new_courses[i]["title"])
            self.new_button_8.setText("Enroll")
            return
        if i == 8:
            self.new_label_9.setText(self.new_courses[i]["title"])
            self.new_button_9.setText("Enroll")
            return
        if i == 9:
            self.new_label_10.setText(self.new_courses[i]["title"])
            self.new_button_10.setText("Enroll")
            return

    def set_top_courses_frames_invisible(self, i):
        if i == 0:
            self.top_frame1.setVisible(False)
            return
        if i == 1:
            self.top_frame2.setVisible(False)
            return
        if i == 2:
            self.top_frame3.setVisible(False)
            return
        if i == 3:
            self.top_frame4.setVisible(False)
            return
        if i == 4:
            self.top_frame5.setVisible(False)
            return
        if i == 5:
            self.top_frame6.setVisible(False)
            return
        if i == 6:
            self.top_frame7.setVisible(False)
            return
        if i == 7:
            self.top_frame8.setVisible(False)
            return
        if i == 8:
            self.top_frame9.setVisible(False)
            return
        if i == 9:
            self.top_frame10.setVisible(False)
            return

    def top_courses_frames_occupy(self, i):
        if i == 0:
            self.top_label_1.setText(self.top_courses[i]["title"])
            self.top_button_1.setText("Enroll")
            return
        if i == 1:
            self.top_label_2.setText(self.top_courses[i]["title"])
            self.top_button_2.setText("Enroll")
            return
        if i == 2:
            self.top_label_3.setText(self.top_courses[i]["title"])
            self.top_button_3.setText("Enroll")
            return
        if i == 3:
            self.top_label_4.setText(self.top_courses[i]["title"])
            self.top_button_4.setText("Enroll")
            return
        if i == 4:
            self.top_label_5.setText(self.top_courses[i]["title"])
            self.top_button_5.setText("Enroll")
            return
        if i == 5:
            self.top_label_6.setText(self.top_courses[i]["title"])
            self.top_button_6.setText("Enroll")
            return
        if i == 6:
            self.top_label_7.setText(self.top_courses[i]["title"])
            self.top_button_7.setText("Enroll")
            return
        if i == 7:
            self.top_label_8.setText(self.top_courses[i]["title"])
            self.top_button_8.setText("Enroll")
            return
        if i == 8:
            self.top_label_9.setText(self.top_courses[i]["title"])
            self.top_button_9.setText("Enroll")
            return
        if i == 9:
            self.top_label_10.setText(self.top_courses[i]["title"])
            self.top_button_10.setText("Enroll")
            return

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
            warnings.append('Enter a valid first name')
        if last_name == "" or len(last_name) < 2:
            warnings.append('Enter a valid last name')
        if username == "" or len(username) < 4:
            warnings.append('Enter a valid username')
        if not validate_email(email):
            warnings.append('Enter a valid email')
        if len(password) < 8 or password != confirm_password:
            warnings.append('enter a valid password and confirm it correctly')
        if gender != "1" and gender != "2":
            warnings.append('You must choose your gender')
        age = int(datetime.datetime.now().year) - int(date_of_birth[2])
        if age < 12:
            warnings.append('You supposed to registered by your parent')
        if len(warnings) > 0:
            warnings_str = "\n".join(warnings)
            QMessageBox.warning(self, "Warnings", warnings_str)
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
            self.first_name.setText("")
            self.last_name.setText("")
            self.register_username.setText("")
            self.register_email.setText("")
            self.register_password.setText("")
            self.register_confirm_password.setText("")
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
            warnings_str = "\n".join(warnings)
            QMessageBox.warning(self, "Warnings", warnings_str)
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
        else:
            self.reload_category_request.click()
            self.reload_teaching_request.click()
        self.get_profile()
        self.tabWidget.setCurrentIndex(2)
        self.home_button.click()
        self.username_or_email.setText("")
        self.password.setText("")

    def get_profile(self):
        request = (self.server + mapping.PROFILE + "?"
                   + parameters.ACCESS_TOKEN + "=" + self.token)
        response = requests.get(request)
        if response.status_code == 200:
            profile = json.loads(response.text)
            self.user = profile
            self.profile_button.setText(profile["firstName"])

            self.profile_first_name.setText(profile["firstName"])
            self.profile_last_name.setText(profile["lastName"])
            self.profile_email.setText(profile["email"])
            self.profile_username.setText(profile["username"])
            self.profile_gender.setText(profile["gender"])
            self.profile_age.setText(str(profile["age"]))
            self.profile_date_of_birth.setText(profile["dateOfBirth"])

    def get_hot_courses(self):
        request = (self.server + mapping.HOT_COURSES)
        response = requests.get(request)
        if response.status_code == 200:
            self.hot_courses = json.loads(response.text)
            for i in range(len(self.hot_courses)):
                self.hot_courses_frames_occupy(i)
            for i in range(len(self.hot_courses), 10):
                self.set_hot_courses_frames_invisible(i)

    def get_new_courses(self):
        request = (self.server + mapping.NEW_COURSES)
        response = requests.get(request)
        if response.status_code == 200:
            self.new_courses = json.loads(response.text)
            for i in range(len(self.new_courses)):
                self.new_courses_frames_occupy(i)
            for i in range(len(self.new_courses), 10):
                self.set_new_courses_frames_invisible(i)

    def get_top_courses(self):
        request = (self.server + mapping.TOP_RATED_COURSES)
        response = requests.get(request)
        if response.status_code == 200:
            self.top_courses = json.loads(response.text)
            for i in range(len(self.top_courses)):
                self.top_courses_frames_occupy(i)
            for i in range(len(self.top_courses), 10):
                self.set_top_courses_frames_invisible(i)

    def admin_approve_teaching_request(self):
        claimer_id = self.claimer_id.text()
        request = (self.server + mapping.APPROVE_TEACHING_REQUEST + "?"
                   + parameters.ACCESS_TOKEN + "=" + self.token + "&"
                   + parameters.USER_ID + "=" + claimer_id)
        response = requests.put(request)
        self.update_teaching_request()
        QMessageBox.information(self, "Info", response.text)

    def admin_approve_category(self):
        category_id = self.category_to_be_approved.text()
        request = (self.server + mapping.APPROVE_CATEGORY + "?"
                   + parameters.ACCESS_TOKEN + "=" + self.token + "&"
                   + parameters.CATEGORY_ID + "=" + category_id)
        response = requests.put(request)
        self.update_category_request()
        QMessageBox.information(self, "Info", response.text)

    def admin_add_category(self):
        category = self.category_to_be_added.text()
        request = (self.server + mapping.ALL_CATEGORIES + "?"
                   + parameters.ACCESS_TOKEN + "=" + self.token + "&"
                   + parameters.CATEGORY + "=" + category)
        response = requests.post(request)
        self.update_category_request()
        QMessageBox.information(self, "Info", response.text)

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
