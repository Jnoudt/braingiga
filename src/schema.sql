

-- for student registration page
drop table if exists student;
create table student
  ( first_name VARCHAR(100)
  , last_name varchar(100)
  , select_title text
  , ethnicity text
  , disability BOOLEAN
  , select_citizenship text
  , are_You_south_african BOOLEAN
  , if_not_please_state BOOLEAN
  , south_African_ID text
  , exact_city_of_residence text
  , phone_number text
  , email text
  , languages text
  , what_am_i_looking_for text
  , degree BOOLEAN
  , major text
  , graduation_year text
  , cv MEDIUMBLOB
  , previous_projects MEDIUMBLOB
  , degree_diploma MEDIUMBLOB
  , photo MEDIUMBLOB
  , job_category text
  , experience text
  , preffered_work text
  , city text
  , about_me text
  , work_experience text
  , type_Of_employment text
  , company_name text
  , job_title text
  , start_end_date char(100)
  , job_description text
  , education text
  , qualifications text
  , institution char(100)
  , major_program text
  , graduation_start_end_date text
  , skills text
  , recommendation text
  );

-- for Challenge page
drop table if exists challenge;
create table challenge
  ( Login text
  , time TIMESTAMP
  , prizes text
  , tips text
  , main_question text
  , the_question blob
  , background_about_company MEDIUMBLOB
  , what_client_is_looking_for text
  , benefits_for_applicant text
  , file MEDIUMBLOB
  );

  -- for solutions page
drop table if exists solutions;
create table solutions
  ( time TIMESTAMP
  , file MEDIUMBLOB
  );

  -- for contact page
drop table if exists contact;
create table contact
  (  Your_Name       char(30)
  ,  Contact_Number  int(14)
  ,  Your_Email      char(30)
  ,  Subject         char(30)
  ,  Your_Message    text
  );

  -- for login page
drop table if exists login;
create table login
  ( email char(30)
  , password char(20)
  );
