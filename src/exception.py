import sys


def error_massage_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_massage = "Error occured in file: {}, line: {}, error: {}".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_massage 
    



class CustomException(Exception):
    
    def __init__(self,error_detail:sys):
        self.error_detail = error_detail
        self.error_massage = error_massage_detail(error_massage, error_detail= error_detail)
    
    def __str__(self):
        return self.error_massage