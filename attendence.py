import sqlite3 as sql

# Attendence class has all the operations related to the attendence system
class AttendenceSystem:
    def __init__(self,attendence_date:str,database) -> None:
        self.attendence_date = attendence_date
        self.database = database
        self.createTable()
        
    def createTable(self) -> None:
        # chech or the table is already existe in the database
        table_name = self.attendence_date
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cur.fetchone()
        
        #if the table is existe in database the the user can mark their attendence
        if result:
            print("the table has already existe you can mark your attendence")
        # if the table is not exist in dtabase the we create the table in the database
        else:
            cur.execute(f"CREATE TABLE {self.attendence_date}(name,roll_no)")
            
    # this function used the insert the values into the table i.e mark attendences   
    def markAttendence(self):
        
        try:
            name = input("enter your name")
            roll_no = int(input("enter your roll no"))
        
            cur.execute(F"INSERT INTO {self.attendence_date} VALUES(?,?)",(name,roll_no))
            print("your attendence is marked successfully")
            
        except Exception as e:
            print(f"an error occured {e}")
        
        
    # this function used to view the attendences
    def attendenceStatus(self) -> None:
        cur.execute(f"SELECT * FROM {self.attendence_date}")
        attendence = cur.fetchall()
        print(f"attendence of date {self.attendence_date}")
        
        if len(attendence) == 0:
            print(f"there is no attendeees on date {self.attendence_date}")
        else:
            print("index  name     roll _no")
            for i,attendees in enumerate(attendence):
                print(f"{i} {attendees[0]} {attendees[1]}")
        
print("############### PLEASE MARK YOUR ATTENDENCE #######################")       
db = sql.connect("attendence_database")
cur = db.cursor()
date = input("enter the today's date (monthday)")
attendence = AttendenceSystem(date,cur)
while True:
    option = int(input("which operation do you want to perform ( 1.mark attendence,2.view attendence,3.exit)"))
    if option == 1:
        attendence.markAttendence()
    elif option == 2:
        attendence.attendenceStatus()
    elif option == 3:
        break
    else:
        print("please enter valid option")
        
db.close()
