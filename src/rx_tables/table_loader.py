'''
Module containing TableLoader class
'''
import os
from importlib.resources import files

import pandas as pnd
from dmu.logging.log_store import LogStore

log=LogStore.add_logger('rx_tables:tuple_loader')
# --------------------------------
class TableLoader:
    '''
    Class used to load tables from CSV files into pandas dataframes
    '''
    def __init__(self, path : str):
        path = files('rx_tables_data').joinpath(path)
        path = str(path)

        if not os.path.isfile(path):
            raise FileNotFoundError(f'Cannot find: {path}')

        log.debug(f'Picking up data from: {path}')

        self._path = path
    # -------------------------
    def get_df(self) -> pnd.DataFrame:
        '''
        Returns pandas dataframe made from CSV file
        '''
        return pnd.read_csv(self._path)
# --------------------------------
