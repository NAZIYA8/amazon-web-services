import logging
logger = logging
logger.basicConfig(filename='ec2.log', level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='ec2.log', level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')