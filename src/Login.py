#!/usr/bin/python

import MySQLdb

import cgi
# Turn on debug mode.
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

print ('Content-type: text/html\r\n\r')
print ('<html>')

Login = form.getvalue('login')
Password = form.getvalue('password')

#---
print ('Debugging starts') + ("<br>")

try:
  # Open database connection
  db = MySQLdb.connect("localhost","root","juvenile","braingiga" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor()

  # Execute the SQL command
  cursor.execute('insert into login values("%s", "%s")' % \
            (login,password))

  # Commit your changes in the database
  db.commit()

except:
   print ('We are rollingback, there seems to have been a problem') + ("<br>")
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

#---
#print 'Debugging starts' + "<br>"

# Open database connection
print 'About to open DB connection' + "<br>"

db = MySQLdb.connect("localhost","root","juvenile","braingiga" )
print ('DB connection opened') + ("<br>")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """insert into login values ('login','password')"""

#cursor.execute('insert into login values("%s", "%s")' % \
#         (login,password))



print ('Debugging ends') + ("<br><br>")

print ('Login: ') + str(Login) + ('<br>')
print ('Password: ') + str(Password) + ('<br>')
print ('</html>')
