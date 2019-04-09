import mysql.connector as DbConnector
class DbOperations:
    def __init__(self,databaseName):
        self.__databaseName = databaseName

    def insert(self, query):
        try:
            conn = DbConnector.connect(host="localhost",
                                       user="root",
                                       database = self.__databaseName)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()
        except DbConnector.Error as e:
            print(e)
            
    def get(self, query):
        rows=None
        try:
            conn = DbConnector.connect(host="localhost",
                                       user="root",
                                       database = self.__databaseName)
            cur = conn.cursor()
            cur.execute(query)
            columns = [col[0] for col in cur.description]
            rows = [dict(zip(columns, row)) for row in cur.fetchall()] 
            conn.close()
        except DbConnector.Error as e:
            print(e)
        return rows
    
    def insertInTime(self,Id):
        query = "INSERT INTO usersattendance(userId) values({0})"
        query = query.format(Id)
        self.insert(query)
        
    def insertOutTime(self,Id):
        query = '''
                UPDATE usersattendance 
                SET    outtime = CURRENT_TIMESTAMP 
                WHERE  id = {0}
                AND InTime = (SELECT MAX(InTime) 
                               FROM   (SELECT * 
                                       FROM   usersattendance) AS vt
                               WHERE  id = {0}) 
                AND OutTime='0000-00-00 00:00:00'
                '''
        query = query.format(Id)
        self.insert(query)
        
    def insertLastTrainedAt(self):
        query = "update lasttrained set lasttrainedat=DEFAULT"
        self.insert(query)

    def getNewEmployeeImageDir(self):
        query = "SELECT ImageDirectory FROM users where CreatedOn >(SELECT lasttrainedat from lasttrained)"
        rows = self.get(query)
        return rows
