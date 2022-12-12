import json
import requests

class Student:
  def __init__(self, full_name, age, level, mobile_number):

    self.id = Student.id
    self.full_name = full_name
    self.age = age
    self.level = level
    self.mobile_number = mobile_number
    Student.id += 1

s = Student("131","dssds",32,"A",424232)

while True:
    print("1- Regester new student\n2- Edit student details\n3- Delete student\n4- Export student to text file\n5- Export studet details to text file")
    option = input("Select option number: ")

    if option == '1':
        response= requests.post('http://staging.bldt.ca/api/method/build_it.test.register_student', data={'full_name':s.full_name,'age':s.age,'level':s.level,'mobile_number':s.mobile_number})
        if response.status_code == 200:
            print('Student Added Success')
        else:
            print('Somthing Wrong!!!')

    if option == '2':
        response= requests.post('http://staging.bldt.ca/api/method/build_it.test.edit_student', data={'full_name':s.full_name,'age':s.age,'level':s.level,'mobile_number':s.mobile_number,})
        if response.status_code == 200:
            print('Student Edited Success')
        else:
            print('Somthing Wrong!!!')
#    wrong
    if option == '3':
        well_deleted = input("Select student you want to delete: ")
        response= requests.delete(f'http://staging.bldt.ca/api/method/build_it.test.delete_student/{well_deleted}')
#    wrong
    if option == '4':
        students = requests.get('http://staging.bldt.ca/api/method/build_it.test.get_students/{s.id}')
        with open("txt.json", "w") as outfile:
            json.dump(students, outfile)

