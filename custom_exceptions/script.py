import sys
from exceptions import CustomException

def my_fault():
    try:
        1/0
    except Exception as e:
        error = CustomException(e,sys)
        print(error)
        
my_fault()