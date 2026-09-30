import os
import gzip
import pickle as pic
import threading as thr
def save_data_work(students,courses,marks):
    print("COMPRESSING...")
    data = [students,courses,marks]
    with gzip.open('students.dat',"wb") as f:
        pic.dump(data,f)
    print("Saving data into 'students.dat' complete!")
def save_data_back(students,courses,marks):
    save_thread = thr.Thread(
        target = save_data_work,
        args = (students,courses,marks),
        name = "PersistThread",
    )
    save_thread.start()
    return save_thread
def load_data():
    if not os.path.exists('students.dat'):
        return None
    print('LOADING DATA...')
    try:
        with gzip.open('students.dat',"wb") as f:
            data = pic.load(f)
        return data['students'],data['courses'],data['marks']
    except Exception as e:
        print(f"ERROR: {e}")
        return None