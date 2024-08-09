#define a student list
student_list = []

for x in range(2):

    #define a single student
    student = {}

    # update / add values to student
    student["fname"] = input("Enter your first name:")
    student["lname"] = input("Enter your last name:")
    student["rollNo"] =int(input("Enter your roll no :"))

    # add student to list
    student_list.append(student)




# for stud in student_list:
#     print("{rollNo}           {fname}             {lname} ".format(fname=stud["fname"],lname=stud["lname"],rollNo=stud["rollNo"]))
#

roll = int(input("enter roll no to search :"))
for stud in student_list:
    if(stud["rollNo"] == roll):
        print("{rollNo}           {fname}             {lname} ".format(fname=stud["fname"],lname=stud["lname"],rollNo=stud["rollNo"]))