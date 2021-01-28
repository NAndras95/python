#!/usr/bin/python

import logging

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
#   do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
