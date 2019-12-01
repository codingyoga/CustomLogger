import custom_logging
import sys, os

logging = custom_logging.CustomLogging(name=os.path.realpath(sys.argv[0]), log_file='custom_logging2.log', level='INFO')
logger = logging.get_logger()

################
# Example 3
################
dict_log = {
               'datasetname':'db_name',
               'columnid':'',
               'datasetid':'',
               'status':'status',
               'errormsg':'this data is present'
           }

logger.error(dict_log)