
myfile = open("data.txt",'r')
data = myfile.readlines()
print(data)
for line in data :
    print(line.split(" ")[4])




