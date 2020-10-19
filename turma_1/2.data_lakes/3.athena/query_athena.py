from pyathena import connect
import pandas as pd

pd.set_option('display.width', 420)
pd.set_option('display.max_columns', 15)

conn = connect(work_group='athena-data-engineer-workgroup')
df = pd.read_sql('SELECT * FROM data_lake_raw.titanic', conn)
print(df.head())