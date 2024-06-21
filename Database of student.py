import os
os.system('cls' if os.name == 'nt' else 'clear')   #the code in line 1,2 is to clear the terminal screen

from Student_class import student

#To get current time
from datetime import datetime

#Retrieving Objects from a File using pickle module
import pickle

# Deserialize and load the objects from the file
with open('C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.pkl', 'rb') as f:
    students = pickle.load(f)

# Print the loaded objects
for person in students:
    print(person.name)

#print(students[0].name)

#function to register attendence of given id 
def attendence(entered_id):
    index_in_students = entered_id - 1
    print("Last attendence: " + str(students[index_in_students].time))
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    students[index_in_students] = time
    print("New attencdence: " + str(students[index_in_students]))

attendence(int(input("Entre your student id for attendence: ")))

'''# Serialize the updated list back to the file
with open('C:\\Users\\BCS\\Documents\\Python\\I.D. card program\\registered students.pkl', 'wb') as f:
    pickle.dump(students, f)'''