import flet as ft

from sqlengine.samples.course import Course
from sqlengine.samples.grade import Grade
from sqlengine.samples.registration import Registration
from sqlengine.samples.school_year import SchoolYear
from sqlengine.samples.student import Student
from sqlengine.samples.subject import Subject


def main(page: ft.Page):
    page.title = "Flet SQLEngine example"
    page.vertical_alignment = ft.MainAxisAlignment.START

    def add_student(_):
        student = Student(
            login=txt_login.value,
            first_name=txt_first_name.value,
            last_name=txt_last_name.value)

        student.create()

        txt_login.value = ""
        txt_first_name.value = ""
        txt_last_name.value = ""

        page.update()

    lbl_title = ft.Text("Add a new student", size=20)
    txt_login = ft.TextField(label="Login")
    txt_first_name = ft.TextField(label="First Name")
    txt_last_name = ft.TextField(label="Last Name")
    btn_add = ft.ElevatedButton("Add", on_click=add_student)

    page.add(
        lbl_title,
        txt_login,
        txt_first_name,
        txt_last_name,
        btn_add
    )


ft.app(main)
