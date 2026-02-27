#from logging import Handler
#import os
#import sys
#import logging


#log_dir='logs'
#LOG_FORMAT=['%(asctime)s: %(levelname)s: %(module)s: %(message)s']

#log_filepath = os.path.join(log_dir,'connections_log.log')

#os.makedirs(log_dir,exist_ok=True)

#logging.basicConfig(
#    level=logging.INFO,
#    format=LOG_FORMAT,

#    handlers=[
    
#            logging.FileHandler(log_filepath),
#            logging.StreamHandler(sys.stdout)
#    ]
#)

#logger = logging.getLogger("summarizerlogger")

import os
import sys
import logging

log_dir = "logs"
log_filepath = os.path.join(log_dir, "connections_log.log")

os.makedirs(log_dir, exist_ok=True)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"

logging.basicConfig(
    level=logging.INFO,   
    format=LOG_FORMAT,    
    handlers=[            
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("summarizerlogger")
