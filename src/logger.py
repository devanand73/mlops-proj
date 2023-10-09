# Import the logging, os, and datetime modules
import logging
import os
from datetime import datetime

'''This code snippet performs the following functions:

1. It imports the necessary modules for logging, file operations, and date/time handling.
2. It generates a unique log file name based on the current date and time using the `strftime()` function.
3. It defines the path where log files will be stored, including creating a "logs" subdirectory if it doesn't exist.
4. It configures the logging module to save log messages to the specified log file with a specific format and logging level.

In summary, this code sets up a logging system in Python that creates timestamped log files in a "logs" directory, allowing developers to record and analyze application events and errors.'''
# Generate a log file name based on the current date and time using strftime()
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where logs will be stored using os.path.join()
# It's using the current working directory, a subdirectory called "logs", and the generated LOG_FILE
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the "logs" directory if it doesn't exist using os.makedirs()
os.makedirs(logs_path, exist_ok=True)

# Define the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module using basicConfig()
# - filename: Specifies the log file where logs will be saved.
# - format: Specifies the format of the log messages using placeholders.
#   - %(asctime)s: Timestamp of the log message.
#   - %(lineno)d: Line number where the logging call occurred.
#   - %(name)s: Name of the logger (typically the module name).
#   - %(levelname)s: Log level (e.g., INFO, ERROR).
#   - %(message)s: The actual log message.
# - level: Sets the logging level to INFO, which logs messages with INFO level and above.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
