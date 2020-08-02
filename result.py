#!/usr/bin/python3

import pymysql

def add_result(idval,imgName,username,tweet):
   # Open database connection
   db = pymysql.connect("localhost","testuser","test123","testdb" )

   # prepare a cursor object using cursor() method
   cursor = db.cursor()




   # Create table as per requirement
   sql = "INSERT INTO RESULT(ID , \
           IMAGENAME, USERNAME, 	TWEET) \
      VALUES ('%d', '%s', '%s', '%s')" % \
      (idval, imgName,username,tweet)

   try:
      # Execute the SQL command
      cursor.execute(sql)
      # Commit your changes in the database
      db.commit()
   except:
      # Rollback in case there is any error
      db.rollback()

   # disconnect from server
   db.close()
#add_result(2,'hi.jpg','THacksters','hello everyone')
