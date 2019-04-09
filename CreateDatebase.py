import mysql.connector as DbConnector
from time import sleep

CreateUsersTable = '''
CREATE TABLE users(
Id INT PRIMARY KEY AUTO_INCREMENT,
FullName VARCHAR(50) NOT NULL,
Email VARCHAR(75) NOT NULL,
PhoneNumber VARCHAR(15),
Address VARCHAR(200),
UserName VARCHAR(25) NOT NULL,
Password VARCHAR(50) NOT NULL DEFAULT "e10adc3949ba59abbe56e057f20f883e",
Salary DOUBLE,
Role VARCHAR(30),
IsAdmin varchar(1) NOT NULL,
ImageDirectory VARCHAR(200) NOT NULL,
UserProfile VARCHAR(120) NOT NULL,
CreatedOn TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
'''

CreateUsersAttendanceTable = '''
CREATE TABLE usersattendance(
Id INT PRIMARY KEY AUTO_INCREMENT,
userId INT NOT NULL,
InTime TIMESTAMP NOT NULL DEFAULT  CURRENT_TIMESTAMP,
OutTime TIMESTAMP,
FOREIGN KEY (userId) REFERENCES users(Id)
)
'''

CreateLastTrainedDateTimeTable = '''
CREATE TABLE lasttrained(
lasttrainedat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
'''
InsertDefaultLastTrainedDateTime = '''
INSERT INTO lasttrained() values()
'''
InsertAdminUsers = '''
INSERT INTO
users(FullName,Email,PhoneNumber,Address,
      Salary,Role,IsAdmin,ImageDirectory,UserProfile,
      CreatedOn)
VALUES('Sai krishna','saisiddu365@gmail.com','9493476964',
'OYO ROOMS Hyderabad-533234',80000,'AssistantSoftware',
'Y','Images/Admin','images/admin.jpg',CURRENT_TIMESTAMP)
'''
conn = DbConnector.connect(host="localhost", user="root")
try:
    cur = conn.cursor()
    cur.execute('DROP DATABASE IF EXISTS attendancemanagementsystem')
    cur.execute('CREATE DATABASE attendancemanagementsystem')
    cur.execute('USE attendancemanagementsystem')
    cur.execute(CreateUsersTable)
    cur.execute(CreateUsersAttendanceTable)
    cur.execute(CreateLastTrainedDateTimeTable)
    cur.execute(InsertDefaultLastTrainedDateTime)
    sleep(2)
    cur.execute(InsertAdminUsers)
   
except DbConnector.Error as e:
    print(e)
finally:
    conn.commit()
    conn.close()
