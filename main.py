from functions import *
import logging
import time


def main():
    """
    System start: if there is no file in the folder,
    then searching for a file every 5 seconds
    """
    while True:
        file_name = file_checker()
        if file_name is None:
            time.sleep(5)
            logging.info('no files')
            continue
        else:
            logging.warning(f'file "{file_name}" is found, processing . . .')
            df = read_file(file_name)
            logging.warning(f'{result_minute(df)} errors in less than 1 Minute')
            logging.warning(f'{result_hour(df)} errors in less than 1 Hour for bundle_id')
            continue


FILE_DICT.clear()

main()
