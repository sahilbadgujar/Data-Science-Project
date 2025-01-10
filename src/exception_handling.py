import sys  # any kind of exception handling is done in runtime enviroment the SYS library will have that information
import logging

def error_message_detail(error, error_detail: sys):
    _,_,exc_tb = error_detail.exc_info()     
    file_name = exc_tb.tb_frame.f_code.co_filename     # will get name of file which leads to error 
    error_message = "error occoured in Python script name [{0}] lne number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

    '''here exc_info will give 3 kinds of information, 1st two are not imp for us
     but the 3rd info exc_tb will provide details about
     which file get error, which line number get error n all '''
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self. error_message

