#!/usr/bin/python
""" 
https://www.tutorialspoint.com/python/python_database_access.htm
"""
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","raspi","r4sp1","raspi" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM pulsador"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      instant = row[1]
      #age = row[2]
      #sex = row[3]
      #income = row[4]
      # Now print fetched result
      print "id=%s,instant=%s" % \
             (id, instant)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
