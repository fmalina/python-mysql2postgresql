from mysql2postgresql import mysql2postgresql
from time import time
from math import floor
import tracemalloc
import os

time1 = time()
tracemalloc.start()

a = mysql2postgresql()
a.connect_mysql(
    host=os.getenv("MYSQL_HOST", "localhost"),
    port=3306,
    user=os.getenv("MYSQL_USER", "root"),
    passwd=os.getenv("MYSQL_PWD", ""),
    db=os.getenv("CONVERT_DATABASE", "db_name"),
    charset="utf8"
)

a.connect_postgresql(
    host=os.getenv("PGHOST", "localhost"),
    port=5432,
    user=os.getenv("PGUSER", "postgres"),
    password=os.getenv("PGPASSWORD", "postgres"),
    database=os.getenv("CONVERT_DATABASE", "database_name"),
)

a.tables = []  # Table list name

a.without = []  # Without table list

a.run()

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()

diff = time() - time1
hour = floor(diff / 3600)
mins = floor((diff / 60) - (hour * 60))
sec = diff - (mins * 60) - (hour * 3600)

print("\nAll done! ✨ 🍰 ✨")
print(f"Time spent: {hour} hours, {mins} minutes, {int(sec)} seconds")
