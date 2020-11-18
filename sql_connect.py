import pyodbc

server = 'bondintelligencesql.database.windows.net'
database = 'Census'
username = 'testlogin'
password = ')xd%<5Z;b[8%}k=d'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.emailtest')

for row in cursor:
    print('row = %r' % (row,))
    