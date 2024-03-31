import sys

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        file_name = exc_traceback.tb_frame.f_code.co_filename 
        line_number = exc_traceback.tb_lineno
        error_message = f"Error occurred in Python script ['{file_name}'], at line [{line_number}]: error type [{error_message}]"
        super().__init__(error_message)
        self.error_message = error_message
        print(self.error_message)

    def __str__(self):
        return self.error_message





# if __name__=="__main__":
#     try:
#         result = 5/0
#         print(result)
#     except Exception as e:
#         raise CustomException(e,sys)
    