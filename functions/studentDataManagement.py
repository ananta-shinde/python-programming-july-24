import random
studentList = []

def addNewStudent(list):
    student = {}
    student["name"] = input("enter your name :")
    student["rollNo"] = random.random()
    student["branch"] = input("enter your branch name :")
    list.append(student)

def getStudentsByBranch(list,branch):
    newList = []
    for s in list:
        if(s["branch"] == branch):
            newList.append(s)
    return newList



addNewStudent(studentList)
addNewStudent(studentList)
addNewStudent(studentList)
addNewStudent(studentList)

mech_students = getStudentsByBranch(studentList,"Mech")
print(mech_students)


