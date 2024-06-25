from Student_class import student

#To get current time
from datetime import datetime

#serialize (pickle) your objects and store them in a file by importing pickle
import pickle

#registered_list
reg_temp = []

exit = False
path_txt = 'C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.txt'

#check number of lines in txt file
with open(path_txt, 'r') as fp:
	lines = len(fp.readlines())

# Serialize and save the first objects to a pkl file
if lines == 0 :
    with open('C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.pkl', 'wb') as f:
        reg_temp.append(student("initialize", "demo", "0", 0, 0))
        pickle.dump(reg_temp, f)

#get the id of objects right
if lines == 0 :
    id = 0
else:
    id = lines - 1

#loop to get students details
while (exit == False):
    print("Welcome New Student. Please entre following details to get registered")
    name = input("Entre your name: ")
    major = input("Entre your major: ")
    year = input("Entre your year: ")

    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    id += 1
    reg_temp.append(student(name, major, year, time, id))

    #print(list.name)
    print("Do you want to add more student")
    cont = input("Entre Y for yes or N for No: ")
    if cont == "Y":
        exit = False
    else:
        exit = True

# save list into registered_students.txt file, and making a copy as txt file
student_file = open(path_txt , "a+")
for i in reg_temp:
    student_file.write(str(i) + "\n")
student_file.close()

#leaving the dublicate initial object
if lines == 0 :
    reg_list = reg_temp[1:]
else:
    reg_list = reg_temp


def append_registered_students(filename, new_students):
    # Deserialize the existing students
    try:
        with open(filename, 'rb') as f:
            students = pickle.load(f)
    except FileNotFoundError:
        print("file does not exists")
    
    # Append new students to the list
    students.extend(new_students)
    
    # Serialize the updated list back to the file
    with open(filename, 'wb') as f:
        pickle.dump(students, f)

# Append new students to the file
path_binary = 'C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.pkl'
append_registered_students(path_binary, reg_list)