#!/usr/bin/python2.6
#-*- coding:utf-8 -*-

import gflags
import logging
import sys
FLAGS=gflags.FLAGS
gflags.DEFINE_string('log_level','debug', 'log level')

LEVELS={'debug':logging.DEBUG,
         'info':logging.INFO,
         'warning':logging.WARNING,
         'error':logging.ERROR,
         'critical':logging.CRITICAL}

def ParseFlags(argv):
  try:
    argv = FLAGS(argv)
    level_name = FLAGS.log_level
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level,
        format='[%(asctime)s:%(levelname)s:%(filename)s(%(lineno)d)]: %(message)s',
        datefmt='%m/%d/%H:%M:%S')
  except gflags.FlagsError, e:
    logging.critical('%s\\nUsage: %s ARGS\\n%s' % (e, sys.argv[0], FLAGS))


if __name__ == "__main__":
  print '''python base.py --log_level=info'''
  ParseFlags(sys.argv)
  logging.debug('This is a debug')
  logging.info('This is a info')
  logging.warning('This is a warning')
