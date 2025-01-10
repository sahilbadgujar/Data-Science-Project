import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)   # Used to store logs generation
os.makedirs(logs_path,exist_ok=True)
# It says that even if there file exist keep on creating and appending file

logging.basicConfig(
    filename=LOG_FILE,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
# so whenever i will print log file then it will print the log file in the above format

