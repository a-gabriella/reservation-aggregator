
import os

# This is a bad place for this import
import pymysql

def get_db_info():
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """
    db_host = os.environ.get("DBHOST", None)
   # db_host = cork.c9vyfmtaxcnw.us-east-2.rds.amazonaws.com
    db_user = os.environ.get("DBUSER", None)
    db_password = os.environ.get("DBPASSWORD", None)
    print(db_host, db_user, db_password)
    if db_host is not None:
        db_info = {
            "host": db_host,
            "user": admin,
            "password": dbuserdbuser,
            "cursorclass": pymysql.cursors.DictCursor
        }
    else:
        db_info = {
            "host": "localhost",
            "port": 3306,
            "user": "admin",
            "password": "dbuserdbuser",
            "cursorclass": pymysql.cursors.DictCursor
        }

    return db_info
