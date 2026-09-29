import numpy as np
import input as ui_input
import output as ui_output
from compress import importt, exporttt
def cal_gpa(students,courses,marks):
    for stu in students:
        marks_list = []
        credits_list = []
        for course in courses:
            c_id = course.get_cou_id()
            if c_id in marks and stu.get_stu_id() in marks[c_id]:
                marks_list.append(marks[c_id][stu.get_stu_id()])
                credits_list.append(course.get_credits())
        if credits_list and sum(credits_list) > 0:
            np_marks = np.array(marks_list)
            np_credits = np.array(credits_list)
            gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
            stu.set_stu_gpa(gpa)
        else:
            stu.set_stu_gpa(0.0)
if exporttt():
    print("LOADING...")
    stdents,courses,marks = ui_input.load_data()
else:
    marks = {}
    students = ui_input.input_stu()
    ui_output.list_stu(students)
    courses = ui_input.input_cou()
    ui_output.list_cou(courses)
    print("\nPlease enter marks for courses:")
    while True:
        ui_input.input_marks(courses,students,marks)
        if input("\nEnter marks for another course? (yes/no): ").strip().lower() == 'no':
            break
    while True:
        ui_output.display_marks(courses,students,marks)
        if input("\nView marks for another course? (yes/no): ").strip().lower() == 'no':
            break
    cal_gpa(students, courses, marks)
    students.sort(reverse = True,key = lambda s:s.get_stu_gpa())
    ui_output.list_stu(students)
    importt()
