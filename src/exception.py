import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  # sys.exc_info() gives the complete tracebacks of the execution (this is taking message from the exception class) 
    file_name=exc_tb.tb_frame.f_code.co_filename # from that traceback we get the tb frame , tb code and tb file name 

    error_message="Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message


class CustomException(Exception): # inherit the exception class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)  # call the constructor of the parent class (initializing/passing the error messsage to the exception class)
        self.error_message=error_message_detail(error_message,error_detail=error_detail) # this error_detail is a sys module

    # whenever we print the object name we get the all details of our message for this str method will be called
    def __str__(self):
        return self.error_message