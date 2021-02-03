import logging

logging.basicConfig(filename="C://Users//manju//Documents//Poornima//screen//test.log",
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',)
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("this is debug message")
logger.info("this is info message")
logger.warning("this is warning message")
logger.error("this is error message")
logger.critical("this is critical message")