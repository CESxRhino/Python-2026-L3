import os
import gzip
import pickle as pic
def save_data(students,courses,marks):
    print("PERSISTING...")
    data = [students,courses,marks]
    with gzip.open('students.dat',"wb") as f:
        pic.dump(data,f)

    print("Saving data into 'students.dat' complete!")

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