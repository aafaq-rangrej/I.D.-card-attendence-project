from Student_class import student

#To get current time
from datetime import datetime

#serialize (pickle) your objects and store them in a file by importing pickle
import pickle

#registered_list
reg_list = []

exit = False

with open(r'C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.txt', 'r') as fp:
	id = len(fp.readlines())

#loop to get students details
while (exit == False):
    print("Welcome New Student. Please entre following details to get registered")
    name = input("Entre your name: ")
    major = input("Entre your major: ")
    year = input("Entre your year: ")

    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    id += 1
    reg_list.append(student(name, major, year, time, id))

    #print(list.name)
    print("Do you want to add more student")
    cont = input("Entre Y for yes or N for No: ")
    if cont == "Y":
        exit = False
    else:
        exit = True

# save list into registered_students.txt file, and making a copy as txt file
path_txt = 'C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.txt'
student_file = open(path_txt , "a+")

for i in reg_list:
    student_file.write(str(i) + "\n")
student_file.close()

# Serialize and save the first objects to a file
with open('C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.pkl', 'wb') as f:
    pickle.dump(reg_list, f)  #legacy code to create first object in path_binary file 

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
'''path_binary = 'C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.pkl'
append_registered_students(path_binary, reg_list)'''