import sys
import os

def error_message_detail(error_message,error_detail):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    lineno=exc_tb.tb_lineno
    error=str(error_message)

    error_message=f"error occured and the file name is [{filename}] and the linenumber is [{lineno}] and error is [{error}]"

    return error_message

class SensorException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message