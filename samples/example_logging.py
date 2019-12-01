import custom_logging
import sys, os

logging = custom_logging.CustomLogging(name=os.path.realpath(sys.argv[0]), log_file='custom_logging.log', level='INFO')
logger = logging.get_logger()

################
# Example 1
################

logger.error("this is an error")
logger.info("this is info")
logger.debug("this is debug")
logger.critical("this is critical")
logger.warn("this is warn")

################
# Example 2
################
a = 5
b = 0
logger.info("a is" + str(a) + " b is" + str(b))

try:
    c = a / b
except Exception as e:
    logger.exception("Exception occurred ", exc_info=True)


