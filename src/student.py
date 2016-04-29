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

first_name                       = form.getvalue('first_name')
last_name                        = form.getvalue('last_name')
select_title                     = form.getvalue('select_title')
ethnicity                        = form.getvalue('ethnicity')
disability                       = form.getvalue('disability')
select_citizenship               = form.getvalue('select_citizenship')
are_You_south_african            = form.getvalue('are_You_south_african')
if_not_please_state              = form.getvalue('if_not_please_state')
south_african_id                 = form.getvalue('south_african_id')
exact_city_of_residence          = form.getvalue('exact_city_of_residence')
phone_number                     = form.getvalue('phone_number')
email                            = form.getvalue('email')
languages                        = form.getvalue('languages')
what_am_i_looking_for            = form.getvalue('what_am_i_looking_for')
degree                           = form.getvalue('degree')
major                            = form.getvalue('major')
graduation_year                  = form.getvalue('graduation_year')
cv                               = form.getvalue('cv')
previous_projects                = form.getvalue('previous_projects')
degree_diploma                   = form.getvalue('degree_diploma')
photo                            = form.getvalue('photo')
job_category                     = form.getvalue('job_category')
experience                       = form.getvalue('experience')
preffered_work                   = form.getvalue('preffered_work')
city                             = form.getvalue('city')
about_me                         = form.getvalue('about_me')
work_experience                  = form.getvalue('work_experience')
type_Of_employment               = form.getvalue('type_Of_employment')
company_name                     = form.getvalue('company_name')
job_title                        = form.getvalue('job_title')
start_end_date                   = form.getvalue('start_end_date')
job_description                  = form.getvalue('job_description')
education                        = form.getvalue('education')
qualifications                   = form.getvalue('qualifications')
institution                      = form.getvalue('institution')
major_program                    = form.getvalue('major_program')
graduation_start_end_date        = form.getvalue('graduation_start_end_date')
skills                           = form.getvalue('skills')
recommendation                   = form.getvalue('recommendation')

#---
print('Debugging starts' + "<br>")

try:
  # Open database connection
  db = MySQLdb.connect("localhost","root","juvenile","braingiga" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor()

  # Execute the SQL command
  cursor.execute('insert into challenge values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % \
              (first_name,last_name,select_title,ethnicity,disability,select_citizenship,are_You_south_african,if_not_please_state,south_African_ID,exact_city_of_residence,phone_number,email,languages,what_am_i_looking_for,degree,major,graduation_year,cv,previous_projects,degree_diploma,photo,job_category,experience,preffered_work,city,about_me,work_experience,type_Of_employment,company_name,job_title,start_end_date,job_description,education,qualifications,institution,major_program,graduation_start_end_date,skills,recommendation))

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
sql = """insert into student values ('first_name','last_name','select_title','ethnicity','disability','select_citizenship','are_You_south_african','if_not_please_state','south_African_ID,'exact_city_of_residence','phone_number','email','languages','what_am_i_looking_for','degree','major','graduation_year','cv','previous_projects','degree_diploma','photo','job_category','experience,'preffered_work','city','about_me','work_experience','type_Of_employmnt','company_name','job_title','start_end_date','job_description','education','qualifications','institution','major_program','graduation_start_end_date','skills','recommendation')"""
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


print("first_name: ") + str(first_name)
print("last_name: " ) + str(last_name)
print("select_title: ") + str(select_title)
print("ethnicity: ") + str(ethnicity)
print("disability: ") + str(disability)
print("select_citizenship: ") + str(select_citizenship)
print("are_You_south_african: ") + str(are_You_south_african)
print("if_not_please_state: ") + str(if_not_please_state)
print("south_african_id: ") + str(south_african_id)
print("exact_city_of_residence: ") + str(exact_city_of_residence)
print("phone_number: ") + str(phone_number)
print("email: " )+ str(email)
print("languages: ") + str(languages)
print("what_am_i_looking_for: ") + str(what_am_i_looking_for)
print("degree: ") + str(degree)
print("major: ") + str(major)
print("graduation_year: ") + str(graduation_year)
print("cv: ") + str(file)
print("previous_projects: ") + str(file)
print("degree_diploma: ") + str(file)
print("photo: ") + str(file)
print("job_category: ") + str(job_category)
print("experience: ") + str(experience)
print("preffered_work: ") + str(preffered_work)
print("city: ") + str(city)
print("about_me: ") + str(about_me)
print("work_experience: ") + str(work_experience)
print("type_Of_employment: ") + str(type_Of_employment)
print("company_name: ") + str(company_name)
print("job_title: ") + str(job_title)
print("start_end_date: ") + str(start_end_date)
print("job_description: ") + str(job_description)
print("education: ") + str(education)
print("qualifications: ") + str(qualifications)
print("institution: ") + str(institution)
print("major_program: ") + str(major_program)
print("graduation_year: ") + str(graduation_start_end_date)
print("skills: ")+ str(skills)
print("recommendation: ") + str(recommendation)
print("</html>")
