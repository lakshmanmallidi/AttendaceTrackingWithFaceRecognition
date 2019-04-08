import mysql.connector as DbConnector
CreateUsersTable = '''
CREATE TABLE users(
Id INT PRIMARY KEY AUTO_INCREMENT,
FullName VARCHAR(50) NOT NULL,
Email VARCHAR(75) NOT NULL,
PhoneNumber VARCHAR(15),
Address VARCHAR(200),
UserName VARCHAR(25) NOT NULL,
Password VARCHAR(50) NOT NULL DEFAULT "Welcome2Automation",
Salary DOUBLE,
Role VARCHAR(30),
IsAdmin varchar(1) NOT NULL,
ImageDirectory VARCHAR(200) NOT NULL,
UserProfile VARCHAR(120) NOT NULL,
CreatedOn DATETIME NOT NULL
)
'''
CreateUsersAttendanceTable = '''
CREATE TABLE usersattendance(
Id INT NOT NULL,
DateCol DATE NOT NULL DEFAULT (CURRENT_DATE),
InTime TIME NOT NULL DEFAULT (CURRENT_TIME),
OutTime TIME,
FOREIGN KEY (Id) REFERENCES users(Id)
)
'''

CreateLastTrainedDateTimeTable = '''
CREATE TABLE lasttrained(
lasttrainedat DATETIME NOT NULL DEFAULT(CURRENT_TIMESTAMP)
)
'''
InsertDefaultLastTrainedDateTime = '''
INSERT INTO lasttrained() values()
'''
conn = DbConnector.connect(host="localhost", user="root",password="mydatabase123!")
try:
    cur = conn.cursor()
    cur.execute('DROP DATABASE IF EXISTS attendancemanagementsystem')
    cur.execute('CREATE DATABASE attendancemanagementsystem')
    cur.execute('USE attendancemanagementsystem')
    cur.execute(CreateUsersTable)
    cur.execute(CreateUsersAttendanceTable)
    cur.execute(CreateLastTrainedDateTimeTable)
    cur.execute(InsertDefaultLastTrainedDateTime)
except DbConnector.Error as e:
    print(e)
finally:
    conn.commit()
    conn.close()
