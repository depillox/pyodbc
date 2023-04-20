#Main.py
'''import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
cursor = conn.cursor()
cursor.execute("SELECT * FROM tAmericanAthleticConference")
total_enrollment = 0
# Step through all the rows in the results set
for row in cursor:
    print(row); # All columns in the row
    print (row[1]); # Second column
    print (row[2]); # Third column
    print (row[3]); # Third column
    total_enrollment = total_enrollment + int(row[2]) # running sum of enrollments
    
    
print ("Total enrollment = " + str(total_enrollment))'''
'''#I want just the schools that are private
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
#three ways to do that, one is cheating
cursor.execute('SELECT University, IsPrivate FROM tAmericanAthleticConference')
for row in cursor: #Lazy Evaluation
    if row.IsPrivate == 1:
        print(row.University)'''
        
'''import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')
#for row in cursor:
# print(row.University)

# The column names are case sensitive!
universities = [myRow.University.strip() for myRow in cursor.fetchall()] #Eager Evaluation (gives all the rows automatically

print (universities)

# Need to re-read the data
#I want the total enrollment of just the private schools
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference WHERE IsPrivate = 1') # Submit a query to the SQL Server instance and store the results in the cursor object
totalEnrollment = sum([int(myRow.Enrollment) for myRow in cursor.fetchall()])
print (totalEnrollment)'''

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')
#for row in cursor:
# print(row.University)

# The column names are case sensitive!
universities = [myRow.University.strip() for myRow in cursor.fetchall()]
print (universities)

# Need to re-read the data
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference') # Submit a query to the SQL Server instance and store the results in the cursor object
totalEnrollment = sum([int(myRow.Enrollment) for myRow in cursor.fetchall()])
print (totalEnrollment)

#Want enrollments under 50K in a set
cursor.execute('SELECT University, Enrollment, IsPrivate FROM tAmericanAthleticConference')
enrollments = [int(myRow.Enrollment)
                for myRow in cursor.fetchall()
                if myRow.Enrollment < 50000]
#print(enrollments)
print(set(enrollments))