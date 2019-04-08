#!/usr/bin/env python3
import sys
sys.path.append('lib/')
import logging
import dispatcher

__author__ = "Alessandro Rabitti"
__version__ = "0.0.1"
__license__ = "MIT"

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
  dispatcher.poll()
