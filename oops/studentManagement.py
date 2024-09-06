import random


class College:
    __id =None
    __name = None
    __contact = None
    __address = None

    def __init__(self,name):
        self.__id = int(random.random()*10000)
        self.__name = name


    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    def setContact(self,contact):
        self.__contact = contact

    def getContact(self):
        return  self.__contact



c1 = College("Mit")
print(c1.getId())
print(c1.getName())


