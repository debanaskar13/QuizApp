import mysql.connector


class DBhelper:

    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='quizapp')
            self.mycursor=self.conn.cursor()
        except Exception as e :
            print(e)

    def insert_question(self,question,option1,option2,option3,option4,answer):
        try :
            self.mycursor.execute(f"INSERT INTO questions(question_no,question,option1,option2,option3,option4,answer) VALUES(NULL,'{question}','{option1}','{option2}','{option3}','{option4}','{answer}')")
            self.conn.commit()
            return 1
        except Exception as e:
            print(e)

    def fetch_question(self):
        try:
            self.mycursor.execute("SELECT * FROM questions")
            data=self.mycursor.fetchall()
            return data
        except:
            return 0

    def fetch_historyquestion(self):
        try:
            self.mycursor.execute("SELECT * FROM historyquestions")
            data=self.mycursor.fetchall()
            return data
        except:
            return 0

    def check_login(self,email,password=None):
        if password!=None:
            self.mycursor.execute(f"SELECT * FROM users WHERE email LIKE '{email}' AND password LIKE '{password}'")
            data = self.mycursor.fetchall()
        else:
            self.mycursor.execute(f"SELECT * FROM users WHERE email LIKE '{email}'")
            data = self.mycursor.fetchall()

        return data

    def insert_user(self,name,email,password,filename=None):

        try :
            self.mycursor.execute(f"INSERT INTO users (user_id,name,email,password,dp) VALUES (NULL,'{name}','{email}','{password}','{filename}')")
            self.conn.commit()
            return 1
        except :
            return 0

    def update_score(self,user_id,score):
        try :
            self.mycursor.execute(f"UPDATE users SET score={score} WHERE user_id={user_id}")
            self.conn.commit()
            return 1
        except :
            return 0
    
    def check_leaderboard(self):
        self.mycursor.execute(f"SELECT * FROM users ORDER BY score DESC LIMIT 5")
        data = self.mycursor.fetchall()

        return data
