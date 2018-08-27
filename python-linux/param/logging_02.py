#!/usr/bin/env python
import logging
import logging.config

logging.config.fileConfig('logging.cnf')
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
