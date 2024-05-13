#Database Managment Banking
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="adeel121",
    database="bank"
)

cursor = mydb.cursor()
def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def create_customers_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        username VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL,
        name VARCHAR(50) NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL,
        city VARCHAR(50) NOT NULL,
        account_number INTEGER NOT NULL,
        status BOOLEAN NOT NULL
    )
    ''')

    mydb.commit()
    cursor.close()
    mydb.close()

if __name__ == "__main__":
    create_customers_table()
