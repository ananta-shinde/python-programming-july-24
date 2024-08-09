studentList = [{"name":"Ananta","city":"Pune"},{"name":"Shubham","city":"Vaijapur"},{"name":"Ram","city":"Ayodhya"}]

print(studentList)

for student in studentList:
    if(student["city"] != "Pune"):
        print(student)