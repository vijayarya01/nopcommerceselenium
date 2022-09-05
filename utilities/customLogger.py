import logging

class LogGen:
    @staticmethod # so that we need not create object while calling it.
    def loggen():
        logging.basicConfig(filename="./Users/vijaydudhiyan/PycharmProjects/nopcommerceselenium/Logs/Automation.log",
                            format='%(asctime)s: %(levelname)s:%(message)s', datefmt= '%m%d%Y %I%M%S %p'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger