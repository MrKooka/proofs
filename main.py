import sqlite3
from prettytable import from_db_cursor
from pprint import pprint
connection = sqlite3.connect("joind.db")
cursor = connection.cursor()
cursor.execute("")
# all_ = cursor.execute('DELETE FROM product_type WHERE id =5;')
# 
all_ = cursor.execute('SELECT * FROM Products ORDER BY price;')
mytable = from_db_cursor(all_)
print(mytable)
# connection.commit()