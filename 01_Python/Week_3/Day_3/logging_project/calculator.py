import logging


logger=logging.getLogger(__name__)

def division(a,b):
    try:
        result=a/b
        logger.info("Division successful")
    except ZeroDivisionError:
         logger.exception("You cant divide a number by zero")    
    except TypeError:
        logger.exception("Only use numbers in division")
           