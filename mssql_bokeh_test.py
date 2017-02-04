# -*- coding: utf-8 -*-

import pandas as pd
import pymssql

# MS SQL server configuration
server = "localhost\FOSS_FI"
user = ""
password = ""
base = "test_base"

# MS SQL server connection and data processing
conn = pymssql.connect(server, user, password, base)
df = pd.read_sql("select * from consumer_complaints", con = conn)
conn.close()