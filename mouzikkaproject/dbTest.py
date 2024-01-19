import cx_Oracle
import traceback
conn=None
try:
    conn=cx_Oracle.connect("mouzikka/music@127.0.0.1/xe")
    print("Connected successfully with the database")
except cx_Oracle.DatabaseError:
    print("Error in connecting with database")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("Disconnected successfully with the database")