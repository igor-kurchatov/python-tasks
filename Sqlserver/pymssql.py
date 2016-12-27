import sys
import pyodbc

connection = None
cursor = None
sqlCommand = None
dataset = None

try:
    connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=KIASAM\SQLEXPRESS2012;'
                                'Database=AdventureWorks2012;'
                                'uid=igor83;pwd=adventure'
                               )

except Exception as e:
    print(e.args)
    sys.exit()

cursor = connection.cursor()

sqlCommand = ("select a.FirstName, a.LastName, a.Title from"
              "("
                "select p.FirstName, p.LastName, p.Title,"
                "ROW_NUMBER() over(order by p.BusinessEntityID) rn" 
                " from Person.Person as p"
               ")a where a.rn <= 100"
               " order by a.LastName"
             )

cursor.execute(sqlCommand)
dataset = cursor.fetchone()

while dataset:

    print("Title:{} First name: {} Last Name: {}".format(dataset.Title, dataset.FirstName, str(dataset.LastName).encode(encoding="cp1251",errors="replace").decode()))
    dataset = cursor.fetchone()

connection.close()
