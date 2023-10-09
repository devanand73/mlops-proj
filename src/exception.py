import sys  # Import the sys module for working with system-related information.
from src.logger import logging  # Import a custom logger (not shown in the provided code).

'''The provided code is a Python script that defines a custom exception class called `CustomException` and related functions for handling and generating detailed error messages. Here's a summary of its function:

1. It imports the `sys` module for working with system-related information and a custom logger (imported from `src.logger`, not shown in the provided code).

2. It defines a function `error_message_detail` that generates a detailed error message by extracting information about the current exception, including the filename and line number where the error occurred.

3. It defines a custom exception class called `CustomException` that takes an error message and system-related information as input. This class generates a detailed error message using the `error_message_detail` function and stores it as an attribute.

4. The `__str__` method of the `CustomException` class returns the detailed error message when the exception is converted to a string.

In summary, this code provides a mechanism for creating and handling custom exceptions with detailed error messages, making it easier to diagnose and troubleshoot issues in Python scripts.'''

# Define a function to generate a detailed error message.
def error_message_detail(error, error_detail: sys):
    # Get information about the exception currently being handled.
    _, _, exc_tb = error_detail.exc_info()
    
    # Extract the filename and line number where the error occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message

# Define a custom exception class called CustomException.
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Generate a detailed error message using the error_message_detail function.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
