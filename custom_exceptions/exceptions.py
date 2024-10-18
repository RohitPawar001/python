import sys
import traceback


def exception_details(error,error_message_details) -> str:
    
    _,err,exec_traceback = error_message_details.exc_info()
    error_list = traceback.extract_tb(exec_traceback)
    
    for error in error_list:
        error_message = f"You got an error as {err}\n \
            in line no  {error.lineno} \n \
            at {error.line} \n \
            in {error.name} \n \
            {error.filename}"
    
    return error_message


class CustomException(Exception):
    def __init__(self,error,error_details:sys):
        self.error = error
        self.error_details = error_details
        self.error_msg = exception_details(error,error_details)
    
    def __str__(self):
        return self.error_msg