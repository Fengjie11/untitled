import pymysql

db = pymysql.connect("localhost", "root", "fengjie521", "person")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s" % data)

