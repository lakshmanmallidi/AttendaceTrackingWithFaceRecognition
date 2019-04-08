import mysql.connector as DbConnector
class DbOperations:
    def __init__(self,databaseName):
        self.__databaseName = databaseName

    def insert(self, query):
        try:
            conn = DbConnector.connect(host="localhost",
                                       user="root",
                                       password="mydatabase123!",
                                       database = self.__databaseName)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            conn.close()
        except DbConnector.Error as e:
            print(e)
            
    def insert(self, query):
        rows=None
        try:
            conn = DbConnector.connect(host="localhost",
                                       user="root",
                                       password="mydatabase123!",
                                       database = self.__databaseName)
            cur = conn.cursor()
            cur.execute(query)
            columns = [col[0] for col in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()] 
            conn.close()
        except DbConnector.Error as e:
            print(e)
        return rows

    def insertOutTime(self,Id):
        query = '''
                UPDATE usersattendance 
                SET    outtime = ( CURRENT_TIME ) 
                WHERE  id = {0}
                       AND datecol = (SELECT Max(datecol) 
                                      FROM   (SELECT * 
                                              FROM   usersattendance) AS vt1 
                                      WHERE  id = {0}) 
                       AND intime = (SELECT Max(intime) 
                                     FROM   (SELECT * 
                                             FROM   usersattendance) AS vt2 
                                     WHERE  id = {0} 
                                            AND datecol = (SELECT Max(datecol) 
                                                           FROM   (SELECT * 
                                                                   FROM   usersattendance) AS 
                                                                  vt3 
                                                           WHERE  id = {0})) 
                       AND outtime IS NULL 
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
