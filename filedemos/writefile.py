file_reader = open("../list_dict_demos/dictdemo01.py", "r")
file_writer= open("demo.txt","w")

data = file_reader.read()

file_writer.write(data)

