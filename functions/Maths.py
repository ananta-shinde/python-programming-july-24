
from reusabilitydemo import sumOfListOfNumbers
def addition(n1,n2):
    return n1+n2

def square(num):
    return num*num;

def cube(num):
    return num*num*num

def validate_aadhar(aadhar_id):
    if(len(aadhar_id) == 12):
        return True
    else:
        return False


list_numbers = [20,15,23,56]
print(sumOfListOfNumbers(list_numbers))


marks = [25,56,25,45]
result = sumOfListOfNumbers(marks)
print(result)
