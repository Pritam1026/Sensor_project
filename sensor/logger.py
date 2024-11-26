#Libraries
import logging
import os
import sys
from datetime import datetime

# Making the file name for logger
current_time=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
LOG_FILE=f"{current_time}.log"

# Making the folder
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

# File for logging
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

# Basic configuration of logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",
    level=logging.INFO,
)