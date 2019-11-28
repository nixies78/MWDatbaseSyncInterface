import logging

class Logger:
	def __init__(self):
		self.logger = logging.getLogger('Eclinic-Microservice')
		self.logger.setLevel(logging.INFO)
		formatter = logging.Formatter('[%(levelname)s %(asctime)s %(name)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
		file_handler = logging.FileHandler('eclinic-app-log.log')
		file_handler.setFormatter(formatter)
		self.logger.addHandler(file_handler)

	def info(self, msg):
		self.logger.info(msg)

	def error(self, msg):
		self.logger.error(msg)