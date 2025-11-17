import sys
from src.logger import logging

# Simple helper that formats an error message including file and line
# where the exception occurred. It expects the `sys` module (or a
# compatible object exposing `exc_info()`) as `error_detail` so callers
# can pass `sys` directly.

def error_message_detail(error,error_detail:sys):
    # Get the current exception info (type, value, traceback)
    _,_,exc_tb=error_detail.exc_info()
    # Extract filename from the innermost traceback frame
    file_name=exc_tb.tb_frame.f_code.co_filename
    # Build a concise, human-readable error message
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    """Custom exception that stores a formatted error message.

    Initialize with the original error/message and `sys` (or similar)
    so the class can build a detailed message including file and line.
    """
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        # Prepare and store a detailed error string for printing/logging
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        # Return the stored, formatted message when the exception is printed
        return self.error_message
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero exception occurred")
        raise CustomException(e,sys)