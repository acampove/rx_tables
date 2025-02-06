'''
Module holding tests for TableLoader class
'''

from dmu.logging.log_store  import LogStore
from rx_tables.table_loader import TableLoader

log=LogStore.add_logger('rx_tables:test_tuple_loader')

def test_simple():
    '''
    Simplest test
    '''
    obj = TableLoader(path='run12/rare_yields.csv')
    df  = obj.get_df()
    print('\n')
    print(df)
