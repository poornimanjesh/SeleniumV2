import logging

logging.basicConfig(filename="C://Users//manju//Documents//Poornima//screen//test.log",
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    level=logging.DEBUG
                    )
logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")

