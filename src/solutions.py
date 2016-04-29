#!/usr/bin/python

# http://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb

import cgi
# Turn on debug mode.
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

print ('Content-type: text/html\r\n\r')
print ('<html>')

time    = form.getvalue('time')
uploads = form.getvalue('file')

#---
print ('Debugging starts') + ("<br>")

try:
  # Open database connection
  db = MySQLdb.connect("localhost","root","juvenile","braingiga" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor()

  # Execute the SQL command
  cursor.execute('insert into solutions values("%s", "%s")' % \
            (time,file))

  # Commit your changes in the database
  db.commit()

except:
   print ('We are rollingback, there seems to have been a problem') + ("<br>")
   # Rollback in case there is any error
   db.rollback()

 #disconnect from server
db.close()

#---
#print 'Debugging starts' + "<br>"
#
## Open database connection
print ('About to open DB connection') + "<br>"
db = MySQLdb.connect("localhost","root","juvenile","braingiga" )
print ('DB connection opened') + "<br>"
#
## prepare a cursor object using cursor() method
cursor = db.cursor()
#
## Prepare SQL query to INSERT a record into the database.
sql = """insert into solutions values ('time','file')"""
#
#
#cursor.execute('insert into solutions values("%s", "%s")' % \
#         (time,file))
#
#try:
#   print 'About to try writing to DB' + "<br>"
#   print "We are going to execute the following SQL statement : <br>" + sql + "<br>"
#   # Execute the SQL command
#   #cursor.execute(sql)
#   cursor.execute('insert into solutions values("%s", "%s")' % \
#             (time,file))
#   print 'Wrote to DB' + "<br>"
#   # Commit your changes in the database
#   db.commit()
#   print 'Committed to DB' + "<br>"
#except:
#   print 'We are rollingback, there seems to have been a problem' + "<br>"
#   # Rollback in case there is any error
#   db.rollback()
#
## disconnect from server
#db.close()
#---

print("Debugging ends") + ("<br><br>")

print("time: ") + str(time) + '<br>'
print("file: ") + str(file) + '<br>'
print('</html>')
