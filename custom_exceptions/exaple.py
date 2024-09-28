import sys
from exceptions import CustomException
try:
    a = "0"
    a += 2
    print(a)
except Exception as e:
    raise CustomException(e,sys)