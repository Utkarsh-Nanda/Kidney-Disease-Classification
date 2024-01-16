import os
import sys
import logging
# logging string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# logging file directory from the project path
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# configuring the logging instance
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
# so that we can use this logger object in other modules by importing it
logger = logging.getLogger("cnnClassifierLogger")