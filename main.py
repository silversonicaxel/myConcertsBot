#!/usr/bin/env python3
import logging
import dispatcher
import sys
sys.path.append('lib/')


__author__ = "Alessandro Rabitti"
__version__ = "0.0.1"
__license__ = "MIT"

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    dispatcher.poll()
