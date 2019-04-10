import mysql.connector as DbConnector
from time import sleep

CreateUsersTable = '''
CREATE TABLE users(
Id INT PRIMARY KEY AUTO_INCREMENT,
UserName VARCHAR(15) NOT NULL,
Password VARCHAR(20) NOT NULL DEFAULT "e10adc3949ba59abbe56e057f20f883e",
IsAdmin varchar(1) NOT NULL,
ImageDirectory VARCHAR(50) NOT NULL,
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
users(UserName,IsAdmin,ImageDirectory,CreatedOn)
VALUES('admin','Y','Images/Admin',CURRENT_TIMESTAMP)
'''
conn = DbConnector.connect(host="localhost", user="root", password="mydatabase123!")
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
