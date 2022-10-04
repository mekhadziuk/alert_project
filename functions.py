import os
import os.path
from os.path import isfile, join
import pandas as pd
import config


FILENUM = 0
FILE_DICT = {}


def file_checker() -> str:
    """
    Checking for files in a folder
    :return: file name in the folder
    """
    global FILENUM
    global FILE_DICT
    path = './project'
    list_of_files = [i for i in os.listdir(path) if isfile(join(path, i)) and i.endswith('.csv')]
    if len(list_of_files) == 0:
        print("no files in this folder")

    for file_name in list_of_files:
        if file_name in FILE_DICT.values():
            continue
        else:
            FILE_DICT[FILENUM] = file_name
            FILENUM += 1
            return file_name


def read_file(file_name: str) -> pd.DataFrame:
    """
    Reading a file if the file is in the folder
    :return: dataflame
    """
    df = pd.read_csv(f'./project/{file_name}')
    df.columns = config.columns
    df['date'] = pd.to_datetime(df['date'], unit='s')
    return df


def result_minute(df: pd.DataFrame) -> int:
    """
    This function returns the number of errors in less than 1 minute
    :return: function result
    """
    result_minute = df.query('severity == "Error"')\
        .groupby(pd.Grouper(key='date', freq='1Min', dropna=True))['severity'].count()
    rm = result_minute[result_minute > 10].count()
    return rm


def result_hour(df: pd.DataFrame) -> int:
    """
    This function returns the number of errors in less than 1 hour for bundle_id
    :return: function result
    """
    result_hour = df.query('severity == "Error"')\
        .groupby([pd.Grouper(key='date', freq='60Min', dropna=True), 'bundle_id'])['severity'].count()
    rh = result_hour[result_hour > 10].count()
    return rh
