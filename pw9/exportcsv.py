import pandas as po
sample_students = [
    {"id": "SV01", "name": "Mr. Volunteers", "dob": "2004-01-15"},
    {"id": "SV02", "name": "Le Cao Minh", "dob": "2004-05-12"},
    {"id": "SV03", "name": "Nguyen Van A", "dob": "2004-08-20"},
]

sample_courses = [
    {"course_id": "CS101", "course_name": "Data Structures", "credits": 3},
    {"course_id": "CS102", "course_name": "Operating Systems", "credits": 4},
]

sample_marks = [
    {"student_id": "SV01", "course_id": "CS101", "mark": 19.0},
    {"student_id": "SV02", "course_id": "CS101", "mark": 18.5},
    {"student_id": "SV03", "course_id": "CS102", "mark": 16.0},
]
def export_to_csv():
    po.DataFrame(sample_students).to_csv("students.csv",index = False,encoding = "utf-8")
    po.DataFrame(sample_courses).to_csv("courses.csv",index = False,encoding = "utf-8")
    po.DataFrame(sample_marks).to_csv("marks.csv",index = False,encoding = "utf-8")
    print("EXPORTING SUCCESS")
def load_dataframes():
    df_students = po.read_csv("students.csv")
    df_courses = po.read_csv("courses.csv")
    df_marks = po.read_csv("marks.csv")
    return df_students,df_courses,df_marks
def query_stu(df_stu):
    print("DANH SACH SINH VIEN:\n ")
    print(df_stu)
    print("Condition: ")
    cond = input().strip()
    try:
        results = df_stu.query(cond)
        print("RESULTS: ")
        if results.empty:
            print("NOTHING")
        else:
            print(results)
    except Exception as e:
        print("ERROR")
export_to_csv()
df_students,df_courses,df_marks = load_dataframes()
query_stu(df_students)
