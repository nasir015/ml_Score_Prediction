import logging
import os
from datetime import datetime
'''

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok= True)


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename= LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)



if __name__ == "__main__":
    logging.info("Starting")
'''

import logging as lg

def logger(file_name , massage):
    lg.basicConfig(filename= file_name,
               level=lg.INFO,format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",filemode='a+')
    console_log = lg.StreamHandler()
    console_log.setLevel(lg.INFO)
    format_1 =  lg.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
    console_log.setFormatter(format_1)
    lg.getLogger('').addHandler(console_log)
    logger1 = lg.getLogger("Nasir")
    logger1.info(massage)













































'''
Importing necessary modules:

os: The os module provides a way to interact with the operating system, allowing you to work with directories and paths.
logging: The logging module is used for logging messages and managing log files.
datetime: The datetime module is used to work with dates and times.



Generating a log file name:

It uses the datetime.now() function to obtain the current date and time.
The strftime method is used to format this timestamp as a string in the format 'month_day_year_hour_minute_second', which is then used as the log file name.



Creating a directory for logs:

The os.path.join function is used to combine the current working directory (os.getcwd()) with a subdirectory named "logs."
The os.makedirs function is called to create this directory if it doesn't already exist (exist_ok=True ensures that the directory is created without raising an error if it already exists).


Combining the log directory and log file path:

The log_file variable holds the generated log file name.
The log_file_path variable combines the log directory path with the log file name using os.path.join.



Configuring the logging system:

The logging.basicConfig function is called to configure the logging system.
filename specifies the log file where log messages will be written. It uses the log_file_path variable from step 4.
format defines the format of log messages, including the timestamp, line number, logger name, log level, and the actual log message itself.
level sets the logging level to INFO, which means only log messages with a severity level of INFO or higher will be recorded. You can change this level to control the verbosity of your logs.




Testing the logging system:

Finally, the code logs a sample message using logging.info. This message will be written to the log file with the specified format.
This code sets up a simple logging system that creates log files with timestamps in a "logs" directory and records log messages with an "INFO" severity level. You can use logging.info, logging.warning, logging.error, etc., to log different types of messages as needed in your application.
'''