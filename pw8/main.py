import input as ui_input
import output as ui_output
from persist import save_data_back, load_data
if load_data() is not None:
    students,courses,marks = load_data()
    print("Persisting Success...")
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
    ui_output.cal_gpa(students, courses, marks)
    students.sort(reverse = True,key = lambda s:s.get_stu_gpa())
    ui_output.list_stu(students)
    print("RUNNING...")
    th = save_data_back(students,courses,marks)
    th.join()
    print("DONE!!!")