import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="123456",
    db="podcli"
)

cur = db.cursor()

cur.execute("SELECT * FROM usuario")

for row in cur.fetchall():
    print(row)

