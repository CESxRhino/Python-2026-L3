import os
import zipfile as zp
def exporttt():
    if os.path.exists('students.dat'):
        print("Decompress...")
        with zp.ZipFile('students.dat','r') as zipf:
            zipf.extractall()
        return True
    return False
def importt():
    import zipfile as zp
    files = ['students.txt','marks.txt','courses.txt']
    with zp.ZipFile('students.dat','w',zp.ZIP_DEFLATED) as zipf:
        for f in files:
            if os.path.exists(f):
                zipf.write(f)
    print("DONE")