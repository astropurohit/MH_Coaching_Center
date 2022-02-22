import json
import math
import random
from kivy.metrics import dp
import requests
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

Window.size = (300, 600)

class FrontPage(Screen):
    pass


class AdmitPage(Screen):
    pass

class RemovePage(Screen):
    pass

class UpdatePage(Screen):
    pass

class EnrollmentPage(Screen):
    pass

class SLoginPage(Screen):
    pass

class StudentFront(Screen):
    pass

class StudentProfilePage(Screen):
    pass

class Main1Page(Screen):
    pass

class Databasepage(Screen):
    def database(self):
        self.url = "https://mhpublicschool-ab437-default-rtdb.firebaseio.com/.json"
        r = requests.get(self.url)
        self.data = r.json()
        self.students = set()
        for key, value in self.data.items():
            self.students.add(key)
        layout = AnchorLayout()
        data = []
        for i in self.students:
            data.append((i, self.data[i]["Fathers name"], self.data[i]["DOB"], self.data[i]["Subject"],self.data[i]["Roll_nu"]))
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.7),
            pos_hint= {'center_y':0.4, 'center_x':0.5},
            use_pagination=True,
            column_data=[
                ("Name", dp(25)),
                ("Father", dp(30)),
                ("DOB", dp(25)),
                ("Subject", dp(30)),
                ("Student id", dp(30)),
            ],
            row_data= data
        )
        # self.add_widget(data_tables)
        # self.root.ids.data_scr.ids.data_layout.add_widget(data_tables)
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.database()

class TeacherLoginPage(Screen):
    pass


sm = ScreenManager()
sm.add_widget(FrontPage(name='frontpage'))
sm.add_widget(AdmitPage(name='admitpage'))
sm.add_widget(RemovePage(name='removepage'))
sm.add_widget(UpdatePage(name='updatepage'))
sm.add_widget(EnrollmentPage(name='enrollmentpage'))
sm.add_widget(SLoginPage(name='sloginpage'))
sm.add_widget(StudentFront(name='studentfront'))
sm.add_widget(Main1Page(name='main1page'))
sm.add_widget(Databasepage(name='databasepage'))
sm.add_widget(TeacherLoginPage(name='teacherloginpage'))

class SchoolApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        digits = "0123456789"
        self.roll = ""
        for i in range(6):
            self.roll += digits[math.floor(random.random() * 10)]
        self.roll = self.roll
        self.url = "https://mhpublicschool-ab437-default-rtdb.firebaseio.com/.json"
        r = requests.get(self.url)
        self.data = r.json()
        self.students = set()
        for key, value in self.data.items():
            self.students.add(key)

    def build(self):
        self.str = Builder.load_file("school.kv")
        return self.str

    def admit(self):
          Student_name = self.str.get_screen('admitpage').ids.student_name.text
          Fathers_name = self.str.get_screen('admitpage').ids.father_name.text
          Student_DOB = self.str.get_screen('admitpage').ids.date_label.text
          Student_sub = self.str.get_screen('admitpage').ids.student_sub.text
          if Student_name == "" or Fathers_name == "" or Student_DOB == "":
            print("wrong")
          else:
            if Student_sub == 'Web Development':
              if Student_name in self.students and Fathers_name == self.data[Student_name]["Fathers name"] and Student_DOB == self.data[Student_name]["DOB"]:
                  self.str.get_screen('admitpage').ids.note_a.text = f"You already selected a course!"
                  print("wrong")
              else:
                  signup_info = str(
                      {f'\"{Student_name}\":{{"Subject":\"{Student_sub}\","Fathers name":\"{Fathers_name}","DOB":\"{Student_DOB}\", "Roll_nu":\"{"WD"+ self.roll}"}}'})
                  signup_info = signup_info.replace(".", "-")
                  signup_info = signup_info.replace("\'", "")
                  to_database = json.loads(signup_info)
                  print((to_database))
                  res = requests.patch(url=self.url, json=to_database)
                  print(res)
                  self.str.get_screen(
                      'admitpage').ids.note_a.text = f"You were admitted! \n your enrollment {'WD'+ self.roll}"
                  self.str.get_screen('admitpage').manager.current = 'studentfront'
                  self.str.get_screen('studentfront').ids.enNumber.text = f"{'WD'+ self.roll}"
                  self.str.get_screen('studentfront').ids.subName.text = f"{Student_sub}"
                  self.str.get_screen('studentfront').ids.pannel1.text = "HTML"
                  self.str.get_screen('studentfront').ids.lecture1.text = "HTML Lecture\n comming soon!"
                  self.str.get_screen('studentfront').ids.pannel2.text = "CSS"
                  self.str.get_screen('studentfront').ids.lecture2.text = "CSS Lecture\n comming soon!"
                  self.str.get_screen('studentfront').ids.pannel3.text = "JS"
                  self.str.get_screen('studentfront').ids.lecture3.text = "JS Lecture\n comming soon!"
                  self.str.get_screen('studentprofilepage').ids.SName.text = f"{Student_name}"
                  self.str.get_screen('studentprofilepage').ids.FaName.text = f"{Fathers_name}"
                  self.str.get_screen('studentprofilepage').ids.Sdob.text = f"{Student_DOB}"
                  self.str.get_screen('studentprofilepage').ids.Sid.text = f"{'WD'+ self.roll}"
            elif Student_sub == 'App Development':
              if Student_name in self.students and Fathers_name == self.data[Student_name]["Fathers name"] and Student_DOB == self.data[Student_name]["DOB"]:
                  self.str.get_screen('admitpage').ids.note_a.text = f"You already selected a course!"
                  print("wrong")
              else:
                signup_info = str(
                    {f'\"{Student_name}\":{{"Subject":\"{Student_sub}\","Fathers name":\"{Fathers_name}","DOB":\"{Student_DOB}\", "Roll_nu":\"{"AP"+ self.roll}"}}'})
                signup_info = signup_info.replace(".", "-")
                signup_info = signup_info.replace("\'", "")
                to_database = json.loads(signup_info)
                print((to_database))
                res = requests.patch(url=self.url, json=to_database)
                print(res)
                self.str.get_screen(
                    'admitpage').ids.note_a.text = f"You were admitted! \n your enrollment {'AP' + self.roll}"
                self.str.get_screen('admitpage').manager.current = 'studentfront'
                self.str.get_screen('studentfront').ids.enNumber.text = f"{'AP'+ self.roll}"
                self.str.get_screen('studentfront').ids.subName.text = f"{Student_sub}"
                self.str.get_screen('studentfront').ids.pannel1.text = "A Studio"
                self.str.get_screen('studentfront').ids.lecture1.text = "Android Studio Lecture\n comming soon!"
                self.str.get_screen('studentfront').ids.pannel2.text = "Java"
                self.str.get_screen('studentfront').ids.lecture2.text = "Java Lecture\n comming soon!"
                self.str.get_screen('studentfront').ids.pannel3.text = "Kotlin"
                self.str.get_screen('studentfront').ids.lecture3.text = "Kotlin Lecture\n comming soon!"
                self.str.get_screen('studentprofilepage').ids.SName.text = f"{Student_name}"
                self.str.get_screen('studentprofilepage').ids.FaName.text = f"{Fathers_name}"
                self.str.get_screen('studentprofilepage').ids.Sdob.text = f"{Student_DOB}"
                self.str.get_screen('studentprofilepage').ids.Sid.text = f"{'AP'+ self.roll}"
            elif Student_sub == 'Python':
              if Student_name in self.students and Fathers_name == self.data[Student_name]["Fathers name"] and Student_DOB == self.data[Student_name]["DOB"]:
                  self.str.get_screen('admitpage').ids.note_a.text = f"You already selected a course!"
                  print("wrong")
              else:
                  signup_info = str(
                      {f'\"{Student_name}\":{{"Subject":\"{Student_sub}\","Fathers name":\"{Fathers_name}","DOB":\"{Student_DOB}\", "Roll_nu":\"{"PY"+ self.roll}"}}'})
                  signup_info = signup_info.replace(".", "-")
                  signup_info = signup_info.replace("\'", "")
                  to_database = json.loads(signup_info)
                  print((to_database))
                  res = requests.patch(url=self.url, json=to_database)
                  print(res)
                  self.str.get_screen(
                      'admitpage').ids.note_a.text = f"You were admitted! \n your enrollment {'PY' + self.roll}"
                  self.str.get_screen('admitpage').manager.current = 'studentfront'
                  self.str.get_screen('studentfront').ids.enNumber.text = f"{'PY'+ self.roll}"
                  self.str.get_screen('studentfront').ids.subName.text = f"{Student_sub}"
                  self.str.get_screen('studentfront').ids.pannel1.text = "Python"
                  self.str.get_screen('studentfront').ids.lecture1.text = "Python Lecture\n comming soon!"
                  self.str.get_screen('studentfront').ids.pannel2.text = "ML"
                  self.str.get_screen('studentfront').ids.lecture2.text = "ML Lecture\n comming soon!"
                  self.str.get_screen('studentfront').ids.pannel3.text = "DL"
                  self.str.get_screen('studentfront').ids.lecture3.text = "DL Lecture\n comming soon!"
                  self.str.get_screen('studentprofilepage').ids.SName.text = f"{Student_name}"
                  self.str.get_screen('studentprofilepage').ids.FaName.text = f"{Fathers_name}"
                  self.str.get_screen('studentprofilepage').ids.Sdob.text = f"{Student_DOB}"
                  self.str.get_screen('studentprofilepage').ids.Sid.text = f"{'PY'+ self.roll}"
            else:
                self.str.get_screen('admitpage').ids.note_a.text = "Something went wrong"
                print("wrong")

    def remove(self):
      Student_name = self.str.get_screen('removepage').ids.student_name.text
      Fathers_name = self.str.get_screen('removepage').ids.father_name.text
      Student_sub = self.str.get_screen('removepage').ids.student_sub.text
      if Student_name == "" or Fathers_name == "" or Student_sub == "":
            self.str.get_screen('removepage').ids.note_r.text = "Something went wrong"
            print("wrong1")
      else:
        if Student_name in self.students and Fathers_name == self.data[Student_name]["Fathers name"] and Student_sub == self.data[Student_name]["Subject"]:
          requests.delete(url = self.url[:-5] + Student_name + ".json")
          self.str.get_screen(
              'removepage').ids.note_r.text = f"Your admission removed \nfrom subject {self.data[Student_name]['Subject']}"
          print("r")
        else:
            self.str.get_screen('removepage').ids.note_r.text = "Something went wrong"
            print("wrong2")

    def update(self):
      Student_name = self.str.get_screen('updatepage').ids.student_name.text
      Fathers_name = self.str.get_screen('updatepage').ids.father_name.text
      Student_DOB = self.str.get_screen('updatepage').ids.date_label.text
      Subject_name = self.str.get_screen('updatepage').ids.student_sub.text
      if Student_name == "" or Fathers_name == "" or Student_DOB == "":
            self.str.get_screen('updatepage').ids.note_u.text = "Something went wrong"
            print("wrong")
      else:
        if Student_name in self.students and Fathers_name == self.data[Student_name]["Fathers name"] and Student_DOB == self.data[Student_name]["DOB"]:
          signup_info = str(
                      {f'\"{Student_name}\":{{"Subject":\"{Subject_name}\","Fathers name":\"{Fathers_name}","DOB":\"{Student_DOB}\", "Roll_nu":\"{self.data[Student_name]["Roll_nu"]}"}}'})
          signup_info = signup_info.replace(".", "-")
          signup_info = signup_info.replace("\'", "")
          to_database = json.loads(signup_info)
          print((to_database))
          res = requests.patch(url=self.url, json=to_database)
          print(res)
          self.str.get_screen('updatepage').ids.note_u.text = "Your Subject \nsuccesfully update"
        else:
            self.str.get_screen('updatepage').ids.note_u.text = "Something went wrong"
            print("wrong")

    def login(self):
      Student_name = self.str.get_screen('sloginpage').ids.student_name.text
      Roll_nu = self.str.get_screen('sloginpage').ids.roll_nu.text
      Subject_name = self.str.get_screen('sloginpage').ids.student_sub.text
      if Student_name == "" and Roll_nu == "" and Subject_name == "":
            self.str.get_screen('sloginpage').ids.note_sl.text = "Something went wrong"
            print("wrong1")
      else:
        if Student_name in self.students and Roll_nu == self.data[Student_name]["Roll_nu"]:
            self.str.get_screen('sloginpage').ids.note_sl.text = "Done !"
            print("login")
            if Subject_name == "Web Development":
                print("A")
                self.str.get_screen('sloginpage').manager.current = 'studentfront'
                self.str.get_screen('studentfront').ids.enNumber.text = self.data[Student_name]["Roll_nu"]
                self.str.get_screen('studentfront').ids.subName.text = self.data[Student_name]["Subject"]
                self.str.get_screen('studentfront').ids.pannel1.text = "HTML"
                self.str.get_screen('studentfront').ids.lecture1.text = "HTML Lecture\n comming soon!"
                self.str.get_screen('studentfront').ids.pannel2.text = "CSS"
                self.str.get_screen('studentfront').ids.lecture2.text = "CSS Lecture\n comming soon!"
                self.str.get_screen('studentfront').ids.pannel3.text = "JS"
                self.str.get_screen('studentfront').ids.lecture3.text = "JS Lecture\n comming soon!"
                self.str.get_screen('studentprofilepage').ids.SName.text = Student_name
                self.str.get_screen('studentprofilepage').ids.FaName.text = self.data[Student_name]["Fathers name"]
                self.str.get_screen('studentprofilepage').ids.Sdob.text = self.data[Student_name]["DOB"]
                self.str.get_screen('studentprofilepage').ids.Sid.text = self.data[Student_name]["Roll_nu"]
            elif Subject_name == "App Development":
                self.str.get_screen('sloginpage').manager.current = 'studentfront'
                self.str.get_screen('studentfront').ids.enNumber.text = self.data[Student_name]["Roll_nu"]
                self.str.get_screen('studentfront').ids.subName.text = self.data[Student_name]["Subject"]
                self.str.get_screen('studentfront').ids.pannel1.text = "A Studio"
                self.str.get_screen('studentfront').ids.lecture1.text = "Android Studio Lecture\n comming soon!"
                self.str.get_screen('studentfront').ids.pannel2.text = "Java"
                self.str.get_screen('studentfront').ids.lecture2.text = "Java Lecture\n comming soon!"
                self.str.get_screen('studentfront').ids.pannel3.text = "Kotlin"
                self.str.get_screen('studentfront').ids.lecture3.text = "Kotlin Lecture\n comming soon!"
                self.str.get_screen('studentprofilepage').ids.SName.text = Student_name
                self.str.get_screen('studentprofilepage').ids.FaName.text = self.data[Student_name]["Fathers name"]
                self.str.get_screen('studentprofilepage').ids.Sdob.text = self.data[Student_name]["DOB"]
                self.str.get_screen('studentprofilepage').ids.Sid.text = self.data[Student_name]["Roll_nu"]
            elif Subject_name == "Python":
                self.str.get_screen('sloginpage').manager.current = 'studentfront'
                self.str.get_screen('studentfront').ids.enNumber.text = self.data[Student_name]["Roll_nu"]
                self.str.get_screen('studentfront').ids.subName.text = self.data[Student_name]["Subject"]
                self.str.get_screen('studentfront').ids.pannel1.text = "Python"
                self.str.get_screen('studentfront').ids.lecture1.text = "Python Lecture\n comming soon!"
                self.str.get_screen('studentfront').ids.pannel2.text = "ML"
                self.str.get_screen('studentfront').ids.lecture2.text = "ML Lecture\n comming soon!"
                self.str.get_screen('studentfront').ids.pannel3.text = "DL"
                self.str.get_screen('studentfront').ids.lecture3.text = "DL Lecture\n comming soon!"
                self.str.get_screen('studentprofilepage').ids.SName.text = Student_name
                self.str.get_screen('studentprofilepage').ids.FaName.text = self.data[Student_name]["Fathers name"]
                self.str.get_screen('studentprofilepage').ids.Sdob.text = self.data[Student_name]["DOB"]
                self.str.get_screen('studentprofilepage').ids.Sid.text = self.data[Student_name]["Roll_nu"]

        else:
            self.str.get_screen('sloginpage').ids.note_sl.text = "Something went wrong"
            print("wrong")

    def enroll(self):
      Student_name = self.str.get_screen('enrollmentpage').ids.student_name.text
      Fathers_name = self.str.get_screen('enrollmentpage').ids.father_name.text
      Subject_name = self.str.get_screen('enrollmentpage').ids.student_sub.text
      if Student_name == "" or Fathers_name == "" or Subject_name == "":
            self.str.get_screen('enrollmentpage').ids.note_en.text = "Something went wrong"
            print("wrong")
      else:
        if Student_name in self.students and Fathers_name == self.data[Student_name]["Fathers name"] and Subject_name == self.data[Student_name]["Subject"]:
            self.str.get_screen('enrollmentpage').ids.note_en.text = f"Your Enrollment\n Number is {self.data[Student_name]['Roll_nu']}"

            print(self.data[Student_name]["Roll_nu"])
        else:
            self.str.get_screen('enrollmentpage').ids.note_en.text = "Something went wrong"
            print("Wrong")

    def teacher_login(self):
        Username = self.str.get_screen('teacherloginpage').ids.username.text
        password = self.str.get_screen('teacherloginpage').ids.password.text
        if Username == "Sandip_sharma" and password == "8889073836":
            self.str.get_screen('teacherloginpage').ids.note_tl.text = "Done!"
            self.str.get_screen('teacherloginpage').manager.current = 'databasepage'
        else:
            self.str.get_screen('teacherloginpage').ids.note_tl.text = "Something went wrong"

SchoolApp().run()
