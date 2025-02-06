# Description

This project is used to hold files with data used to make tables.

# Usage

The tables can be loaded as `pandas` dataframes with:

```python
from rx_tables.table_loader import TableLoader

obj = TableLoader(path='run12/rare_yields.csv')
df  = obj.get_df()
```

