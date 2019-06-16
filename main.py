#!/usr/bin/env python3
import sys
sys.path.append('lib/')
import dispatcher
import logging


__author__ = 'Alessandro Rabitti'
__version__ = '0.0.1'
__license__ = 'MIT'


def main():
    logging.basicConfig(level=logging.INFO)
    dispatcher.poll()


if __name__ == '__main__':
    main()
