import math
import os
from domains.Student import Student
from domains.Courses import Courses
def input_stu():
    students = []
    cnt = int(input("The Number of Students: "))
    print("Please enter the information of the students:")
    for _ in range(cnt):
        stu_id = input("\tStudent's ID is: ")
        stu_name = input("\tStudent's Name is: ")
        dob = input("\tStudent's DOB is: ")
        students.append(Student(stu_id, stu_name, dob))
    with open("students.txt","w",encoding = "utf-8") as f:
        for s in students:
            f.write(f"{s.get_stu_id()},{s.get_stu_name()},{s.get_dob()}\n")
    return students
def input_cou():
    courses = []
    cnt = int(input("The Number of Courses: "))
    print("Please enter the information of the Courses:")
    for _ in range(cnt):
        cou_id = input("\tCourse ID: ")
        cou_name = input("\tCourse Name: ")
        credits = int(input("\tCourse Credits: "))
        courses.append(Courses(cou_id, cou_name, credits))
    with open("courses.txt","w",encoding = "utf-8") as f:
            for c in courses:
                f.write(f"{c.get_cou_id()},{c.get_name()},{c.get_credits()}\n")
    return courses
def input_marks(courses, students, marks):
    courses_id = input("\nSelect a course ID: ")
    selected_course = next((c for c in courses if c.get_cou_id() == courses_id), None)
    print(f"Course name: {selected_course.get_name()}\n")
    if courses_id not in marks:
        marks[courses_id] = {}  
    for stu in students:
        mark = float(input(f"\tEnter {stu.get_stu_name()}'s mark: "))
        rounded_mark = math.floor(mark * 10) / 10
        marks[courses_id][stu.get_stu_id()] = rounded_mark
    with open("marks.txt", "w", encoding="utf-8") as f:
        for c_id, stu_marks in marks.items():
            for s_id, score in stu_marks.items():
                f.write(f"{c_id},{s_id},{score}\n")
def load_data():
    students = []
    courses = []
    marks = {}
    if os.path.exists('students.txt'):
        with open('students.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    s_id, name, dob = line.strip().split(',')
                    students.append(Student(s_id, name, dob))
    if os.path.exists('courses.txt'):
        with open('courses.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    c_id, name, credits = line.strip().split(',')
                    courses.append(Courses(c_id, name, int(credits)))
    if os.path.exists('marks.txt'):
        with open('marks.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    c_id, s_id, mark = line.strip().split(',')
                    if c_id not in marks:
                        marks[c_id] = {}
                    marks[c_id][s_id] = float(mark)
    return students, courses, marks