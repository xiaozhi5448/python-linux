#!/usr/bin/env python
import logging


logging.basicConfig(filename='app.log',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                   level=logging.INFO)

logging.info('info')
logging.debug('debug')
logging.warn('warn')
logging.error('error')
logging.critical('critical')
