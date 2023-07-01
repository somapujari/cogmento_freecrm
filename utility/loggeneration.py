import inspect
import logging

class Loggen:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        file = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\cogmento_freecrm\loggs\logs.log')
        formatter = logging.Formatter('%(message)s : %(asctime)s : %(name)s : %(levelname)s : %(funcName)s  : %('
                                      'lineno)s')
        file.setFormatter(formatter)
        logger.addHandler(file)
        return logger
