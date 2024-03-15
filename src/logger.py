import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # here taking the latest time in a particular format(.log is the file extension)
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  # joint the file to our current working directory 

os.makedirs(logs_path,exist_ok=True)   # create the logging file with the details of the logging 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)  # join the newly created logging file to the current directory 

# format of the logging file 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s',
    level=logging.INFO,
)