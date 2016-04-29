#!/usr/bin/python

# http://www.tutorialspoint.com/python/python_database_access.htm

import MySQLdb

import cgi
# Turn on debug mode.
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

print("Content-type: text/html\r\n\r")
print ("<html>")

Login                      = form.getvalue('Login')
time                       = form.getvalue('time')
prizes                     = form.getvalue('prizes')
tips                       = form.getvalue('tips')
challenge_links            = form.getvalue('challenge_links')
main_question              = form.getvalue('main_question')
the_question               = form.getvalue('the_question')
background_about_company   = form.getvalue('background_about_company')
what_client_is_looking_for = form.getvalue('what_client_is_looking_for')
benefits_for_applicant     = form.getvalue('benefits_for_applicant')
uploads                    = form.getvalue('file')

#---
print('Debugging starts' + "<br>")

try:
  # Open database connection
  db = MySQLdb.connect("localhost","root","juvenile","braingiga" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor()

  # Execute the SQL command
  cursor.execute('insert into challenge values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % \
              (Login,time,prizes,tips,main_question,the_question,background_about_company,what_client_is_looking_for,benefits_for_applicant,file))

  # Commit your changes in the database
  db.commit()

except:
   print ('We are rollingback, there seems to have been a problem' + "<br>")
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

#---
print ('Debugging starts' + "<br>")
#
# Open database connection
print ('About to open DB connection' + "<br>")
db = MySQLdb.connect("localhost","root","juvenile","braingiga" )
print ('DB connection opened' + "<br>")
#
## prepare a cursor object using cursor() method
cursor = db.cursor()
#
## Prepare SQL query to INSERT a record into the database.
sql = """insert into challenge values ('Login','time','prizes','tips','main_question','the_question','background_about_company','what_client_is_looking_for','benefits_for_applicant','file')"""
#
#
#cursor.execute('insert into challenge values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % \
#         (Login,time,prizes,tips,main_question,the_question,background_about_company,what_client_is_looking_for,benefits_for_applicant,file))
#
#try:
#   print 'About to try writing to DB' + "<br>"
#   print "We are going to execute the following SQL statement : <br>" + sql + "<br>"
#   # Execute the SQL command
#   #cursor.execute(sql)
#   cursor.execute('insert into challenge values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % \
#             (Login,time,prizes,tips,main_question,the_question,background_about_company,what_client_is_looking_for,benefits_for_applicant,file))
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

#print("Debugging ends"+"<br><br>")


print("Login:") + str(Login)
print("time:") + str(time)
print("prizes:") + str(prizes)
print("tips:") + str(tips)
print("challenge links:") + str(challenge_links)
print("main question:") + str(main_question)
print("the question:") + str(the_question)
print("background about company:") + str(background_about_company)
print("what client is looking for:") + str(what_client_is_looking_for)
print("benefits for applicant:") + str(benefits_for_applicant)
print("file:") + str(file)
print("</html>")
