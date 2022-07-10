# Imports
import mysql.connector

# Connect to SQL database
mydb = mysql.connector.connect(
    user='admin',
    password='password',
    host='capstone.cvyfjv7s3bb2.us-east-2.rds.amazonaws.com',
    database='capstoneDB')

cursor = mydb.cursor()


class DataBase:
    def select(self):
        cursor.execute("SELECT * FROM survay;")

        for i in cursor:
            print(i)
        return
    
    # Add row to SQL table
    def insert(self, id, num, col, ani):
        full_string = "INSERT INTO survay VALUES ({}, {}, '{}', '{}');".format(id, num, col, ani)
        cursor.execute(full_string)

        mydb.commit()
        return

    # Delete all rows in SQL table
    def clear(self):
        cursor.execute("DELETE FROM survay")

        mydb.commit()
        return
    
    # Get Quantity of each number in SQL table
    def getCountNum(self):
        cursor.execute("SELECT count(*) FROM survay GROUP BY number ORDER BY number;")
        x = []
        for i in cursor:
            x.append(i[0])
        return x

    # Get Quantity of each color in SQL table
    def getCountCol(self):
            cursor.execute("SELECT count(*), color FROM survay GROUP BY color ORDER BY color;")
            x = {
                'Red': 0, 
                'Orange': 0, 
                'Yellow': 0, 
                'Green': 0, 
                'Blue': 0, 
                'Purple': 0, 
                'Black': 0
            }
            for i in cursor:
                x[i[1]] = i[0]
            return x

    # Get Quantity of each animal in SQL table
    def getCountAni(self):
        cursor.execute("SELECT count(*), animal FROM survay GROUP BY animal ORDER BY animal;")
        x = {
            'Dogs': 0, 
            'Cats': 0
        }        
        for i in cursor:
            x[i[1]] = i[0]
        return x
