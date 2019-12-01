import logging

class CustomLogging:
    levels = {'DEBUG': logging.DEBUG,
              'INFO': logging.INFO,
              'WARN': logging.WARN,
              'ERROR': logging.ERROR,
              'CRITICAL': logging.CRITICAL}

    def __init__(self, name, log_file, level):
        self.name = name
        self.logfile = log_file
        self.level = CustomLogging.levels[level]
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        f_handler = logging.FileHandler(self.logfile)
        f_handler.setLevel(self.level)
        logging.getLogger().setLevel(logging.INFO)
        f_handler.setFormatter(self.formatter)
        logger.addHandler(f_handler)
        return logger





