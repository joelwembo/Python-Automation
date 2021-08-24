import sys
from mysql.connector import connect, Error

if len(sys.argv) != 4:
        print ("please enter the Hostnames to connect followed by:")
        print ("mysql username;")
        print ("mysql db to connect;")
else:
        _host = sys.argv[1]
        _user = sys.argv[2]
#       _pass = sys.argv[3]
        _db   = sys.argv[3]
        cham = input("please enter the command to be executed:- ")
        _pass = input("please enter password:- ")

        if cham == "drop table":
            db = connect(host = _host, user = _user,db =  _db, passwd = _pass )
            cursor = db.cursor()
            cursor.execute("show tables")
            for i in cursor.fetchall():
                cursor.execute("drop table" + " " + (i[0]))
                print (cursor.fetchall())
                print ("all the tables has been deleted")
            db.close()
        else:
            db = connect(host = _host, user = _user,db =  _db, passwd = _pass )
            cursor = db.cursor()
            cursor.execute(cham)
            print (cursor.fetchall())
            db.close()
