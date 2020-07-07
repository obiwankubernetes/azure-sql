# 3 ways to connect to sql db

# 1. downloand sql manager locally and use signin

# 2. use querry (in preview) in the portal on home page of the db resource

# 3. by script (in python)

import pyodbc
server = '<servername>.database.windows.net'
database = '<databasename>'
username = '<username>'
password = '<password>'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()