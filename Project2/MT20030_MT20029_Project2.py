# Importing the required libraries
import tkinter as T
import sqlite3
from tkinter import messagebox 
import os
import pandas as pd
from tkinter import *
import numpy as np
import smtplib as email
import pickle as pk

# Creating the Register Class for SignUp
class Register():
    
    def SignUp(self):
        
        reg = T.Tk()
        reg.configure(bg='light cyan')
        Input_fields = ["User Name","Password"]
        variables = []
         
        for i in range(len(Input_fields)):
            variables.append(T.StringVar())
    
        reg.title("Sign Up Portal")
        
        T.Label(reg,
                height=3,
                width=31,
                anchor=CENTER,
                font=("Georgia", 20,'bold') , 
                bg="cyan", 
                fg="black" , 
                text="Sign Up Portal").grid(row=0,columnspan=2)
        
        Text_Box = [None for i in range(len(Input_fields))]
        for i in range(0,len(Input_fields)):
            T.Label(reg,
                    height=2,
                    width=20,
                    anchor=W , 
                    font=("Cubano", 16) , 
                    bg="light cyan", 
                    fg="black" ,
                    text=Input_fields[i]).grid(row=i+2)    
            T.Entry(reg,textvariable=variables[i]).grid(row=i+2, column=1)  

        def getvalues():
            for i in range(len(Input_fields)):
                Text_Box[i] = variables[i].get()
            messagebox.showinfo("","Sign Successfull")
            reg.destroy()
        
        Sumbit_Button = T.Button(reg,
                                 bg="light cyan",
                                 font=("Cubano", 11) ,
                                 width=10, 
                                 text ="Sumbit Data", command=getvalues)
        Sumbit_Button.grid(row=8, columnspan=2)

        reg.geometry('550x300')
        reg.resizable(0, 0) 
        reg.mainloop()
        
        file = r'Registered.pkl'

        if os.path.isfile(file):
            data = pk.load(open(file,'rb')) 
            s = len(data)
            data.loc[s] =Text_Box
            pk.dump(data, open(file, "wb"))
        else:
            data = pd.DataFrame([Text_Box],columns = ['User_Name','Password'])
            pk.dump(data, open(file, "wb"))

# Creating the SignIn Class for Login              
class SignIn():
    
    def __init__(self,cho):
        self.cho = cho
    
    def Login(self):
        
        
        login = T.Tk()
        login.configure(bg='light cyan')
        Input_fields = ["User Name","Password"]
        variables = []
         
        for i in range(len(Input_fields)):
            variables.append(T.StringVar())
    
        login.title("Login Portal")
        
        T.Label(login,
                height=3,
                width=31,
                anchor=CENTER,
                font=("Georgia", 20,'bold') , 
                bg="cyan", 
                fg="black" , 
                text="Login Portal").grid(row=0,columnspan=2)
        
        Text_Box = [None for i in range(len(Input_fields))]
        for i in range(0,len(Input_fields)):
            T.Label(login,
                    height=2,
                    width=20,
                    anchor=W , 
                    font=("Cubano", 16) , 
                    bg="light cyan", 
                    fg="black" ,
                    text=Input_fields[i]).grid(row=i+2)    
            T.Entry(login,textvariable=variables[i]).grid(row=i+2, column=1)  

        def getvalues():
            for i in range(len(Input_fields)):
                Text_Box[i] = variables[i].get()
            login.destroy()
        
        Sumbit_Button = T.Button(login,
                                 bg="light cyan",
                                 font=("Cubano", 11) ,
                                 width=10, 
                                 text ="Sumbit Data", command=getvalues)
        Sumbit_Button.grid(row=8, columnspan=2)
    
        login.geometry('550x300')
        login.resizable(0, 0) 
        login.mainloop()
        
        user = Text_Box[0]
        pas = Text_Box[1]
        
        file = r'Registered.pkl'
        data = pk.load(open(file,'rb'))
        
        x = data[(data.User_Name == user) & (data.Password == pas)]
        Text_Box = self.cho
        if(len(x)>0):
            
            if(int(Text_Box[0])==1):
                C = CompanyData()
                Te = C.GetCompanyInfo()
                DB = DBCompany(Te)
                DB.StoreCompanyInfo()
            
            elif(int(Text_Box[0])==2):
                S = StudentData()
                Te = S.GetStudentInfo()
                DB = DBStudent(Te)
                DB.StoreStudentInfo()
        
            elif(int(Text_Box[0])==3):
                D = DriveData()
                Te = D.GetDriveInfo()
                DB = DBDrive(Te)
                DB.StoreDriveInfo()
        
            elif(int(Text_Box[0])==4):
                 Sen = SendEligibleNotifications()
                 Sen.EligibleNotifications()
             
            elif(int(Text_Box[0])==5):
                Tr = TrackData()
                Te = Tr.GetTrackInfo()
                Sen = SendSelectedNotifications(Te)
                Sen.SelectedNotifications()
        else:
            level = T.Tk()
            messagebox.showinfo("","Login Failed")
            level.mainloop()

# Class to foward the user to either Register Class or SignIn class as per the choice
class Page():
    
    def __init__(self,cho):
        self.cho = cho
    
    def MainPage(self):
        
         if int(cho[0]) == 4 or int(cho[0])==5:
             V = SignIn(self.cho)       
             V.Login() 
         else:    
             main = T.Tk()
             main.configure(bg='light cyan')
             Input_fields = ["Input 1 : SignUp",
                        "Input 2 : SignIn"]
        
             variables = []
    
             for i in range(len(Input_fields)):
                 variables.append(T.StringVar())
    
             main.title("Main Page")
    
             T.Label(main,
                     height=3,
                     width=25,
                     anchor=CENTER,
                     font=("Georgia", 25,'bold') , 
                     bg="cyan", 
                     fg="black" , 
                     text="Main Page").grid(row=0,column=0)
    
    
             Text_Box = [None for i in range(len(Input_fields))]
             for i in range(0,len(Input_fields)):
                 T.Label(main,
                         height=2,
                         width=31,
                         anchor=W , 
                         font=("Cubano", 16) , 
                         bg="light cyan", 
                         fg="black" , 
                         text=Input_fields[i]).grid(row=i+1,column=0)
        
             T.Entry(main,
                     textvariable=variables[0],	
                     width=20,
                     bd = 3,
                     selectborderwidth = 2).grid(row=20,column=0)  

             def getvalues():
                 for i in range(len(Input_fields)):
                     Text_Box[i] = variables[i].get()
                 main.destroy()
        
             Sumbit_Button = T.Button(main,
                             height=1,
                             width=20,
                             bg="light cyan",
                             font=("Cubano", 12) ,
                             text ="Sumbit Data", command=getvalues)
        
       
             Sumbit_Button.grid(row=25, columnspan=2)
    
             main.geometry('500x350')
             main.resizable(0, 0) 
    
             main.mainloop()
         
             if int(Text_Box[0])==1:
                R = Register()
                R.SignUp()   
             elif int(Text_Box[0])==2:
                V = SignIn(self.cho)       
                V.Login()           


# Class to get the data about the Company
class CompanyData():
    
    def GetCompanyInfo(self):
    
        # Creating the Company From
        company = T.Tk()
        company.configure(bg='light cyan')
        Input_fields = ["Name","Address","Turnover","Core Business Area"]
        variables = []
         
        for i in range(len(Input_fields)):
            variables.append(T.StringVar())
    
        company.title("Company Data Portal")
        
        T.Label(company,
                height=3,
                width=31,
                anchor=CENTER,
                font=("Georgia", 20,'bold') , 
                bg="cyan", 
                fg="black" , 
                text="Company Data Portal").grid(row=0,columnspan=2)
        
        Text_Box = [None for i in range(len(Input_fields))]
        for i in range(0,len(Input_fields)):
            T.Label(company,
                    height=2,
                    width=20,
                    anchor=W , 
                    font=("Cubano", 16) , 
                    bg="light cyan", 
                    fg="black" ,
                    text=Input_fields[i]).grid(row=i+2)    
            T.Entry(company,textvariable=variables[i]).grid(row=i+2, column=1)  

        def getvalues():
            for i in range(len(Input_fields)):
                Text_Box[i] = variables[i].get()
            messagebox.showinfo("","Data Sumbitted")
            company.destroy()
        
        Sumbit_Button = T.Button(company,
                                 bg="light cyan",
                                 font=("Cubano", 11) ,
                                 width=10, 
                                 text ="Sumbit Data", command=getvalues)
        Sumbit_Button.grid(row=8, columnspan=2)
    
        company.geometry('550x400')
        company.resizable(0, 0) 
        company.mainloop()
        
        return Text_Box

# Class to store data of Company in Database
class DBCompany():
    
    def __init__(self,Text_Box):
        self.Text_Box = Text_Box
    
    def StoreCompanyInfo(self):
        
        # Create database and store the result
        file = r'Company.db'
    
        if os.path.isfile(file):
        
            comp = sqlite3.connect(file)
            comp_c = comp.cursor()
        
            insertq = """ INSERT INTO Company(Name,Address,Turn,Core)VALUES(?,?,?,?)"""
            comp_c.execute(insertq,tuple(self.Text_Box)) 
        
            s = comp.execute("""SELECT * FROM Company""")
        
            for i in s:
                print(i)
        
            comp.commit()
            comp.close()
    
        else:
        
            comp = sqlite3.connect(file)
            comp_c = comp.cursor()
        
            query = """
            CREATE TABLE Company (
                    Name TEXT , 
                    Address TEXT , 
                    Turn TEXT ,
                    Core TEXT );"""
            comp.execute(query)
                    
            insertq = """ INSERT INTO Company(Name,Address,Turn,Core)VALUES(?,?,?,?)"""
            comp_c.execute(insertq,tuple(self.Text_Box))
                    
            comp.commit()
            comp.close()
       

# Class to get the data about the Student       
class StudentData():
    
    def GetStudentInfo(self):
    
        student = T.Tk()
        student.configure(bg='light cyan')
        
        Input_fields = ["Name","Roll Number","Email Id","CGPA","Active backlogs","Stream"]
        variables = []
    
        for i in range(len(Input_fields)):
            variables.append(T.StringVar())
    
        student.title("Student Data Portal")
        
        T.Label(student,
                height=3,
                width=45,
                anchor=CENTER,
                relief=RAISED,
                font=("Georgia", 20,'bold') , 
                bg="cyan", 
                fg="black" , 
                text="Student Data Portal").grid(row=0,columnspan=2)
         
        Text_Box = [None for i in range(len(Input_fields))]
        for i in range(0,len(Input_fields)):
            T.Label(student,
                    height=2,
                    width=35,
                    anchor=W,
                    #relief=RAISED,
                    font=("Georgia", 16,'bold') , 
                    bg="light cyan", 
                    fg="black" , 
                    text=Input_fields[i]).grid(row=i+2,columnspan = 2)    
            T.Entry(student,textvariable=variables[i]).grid(row=i+2, column=1)  

        def getvalues():
            for i in range(len(Input_fields)):
                Text_Box[i] = variables[i].get()   
            messagebox.showinfo("","Data Sumbitted")    
            student.destroy()
        
        Sumbit_Button = T.Button(student,
                                 bg="light cyan",
                                 font=("Cubano", 11) ,
                                 width=10, 
                                 text ="Sumbit Data", command=getvalues)
        Sumbit_Button.grid(row=10, columnspan=2)
    
        student.geometry('800x550')
        student.resizable(0, 0)
        student.mainloop()
        
        return Text_Box

# Class to store data of Student in Database
class DBStudent():
    
    def __init__(self,Text_Box):
        self.Text_Box = Text_Box
    
    def StoreStudentInfo(self):
        
        file = r'Student.db'
    
        # Create database and store the result
        if os.path.isfile(file):
        
            stud = sqlite3.connect(file)
            stud_c = stud.cursor()
        
            insertq = """ INSERT INTO Student(Name,Roll,Email,Cgpa,Back,Stre) VALUES(?,?,?,?,?,?)"""
            stud_c.execute(insertq,tuple(self.Text_Box)) 
        
            s = stud.execute("""SELECT * FROM Student """)
        
            for i in s:
                print(i)
        
            stud.commit()
            stud.close()
    
        else:
        
            stud = sqlite3.connect(file)
            stud_c = stud.cursor()
            
            query = """
            CREATE TABLE Student (
                    Name TEXT , 
                    Roll TEXT , 
                    Email TEXT ,
                    Cgpa TEXT ,
                    Back TEXT ,
                    Stre TEXT );"""
            stud.execute(query)
        
            insertq = """ INSERT INTO Student(Name,Roll,Email,Cgpa,Back,Stre) VALUES(?,?,?,?,?,?)"""
            stud_c.execute(insertq,tuple(self.Text_Box))

            stud.commit()
            stud.close()

# Class to get the data about the Drive            
class DriveData():
    
    def GetDriveInfo(self):
    
        drive = T.Tk()
        drive.configure(bg='light cyan')
        Input_fields = ['Job Id','Company','Salary','Venue','Drive Date','Eligibilty',
                    'Job Title','Quality','No of Rounds','Backlogs','Test Time',
                    'Cutoff Score']
        variables = []
    
        for i in range(len(Input_fields)):
            variables.append(T.StringVar())
        
        drive.title("Drive Information Portal")
        
        T.Label(drive,
                height=3,
                width=31,
                anchor=CENTER,
                font=("Georgia", 20,'bold') , 
                bg="cyan", 
                fg="black" , 
                text="Drive Information Portal").grid(row=0,columnspan=2)
        
        Text_Box = [None for i in range(len(Input_fields))]
        for i in range(0,len(Input_fields)):
            T.Label(drive,
                    height=1,
                    width=20,
                    anchor=W , 
                    #relief=RAISED,
                    font=("Cubano", 16) , 
                    bg="light cyan", 
                    fg="black" ,
                    text=Input_fields[i]).grid(row=i+2)    
            T.Entry(drive,textvariable=variables[i]).grid(row=i+2, column=1)  

        def getvalues():
            for i in range(len(Input_fields)):
                Text_Box[i] = variables[i].get()   
            messagebox.showinfo("","Data Sumbmitted")    
            drive.destroy()
        
        Sumbit_Button = T.Button(drive,
                                 bg="light cyan",
                                 font=("Cubano", 11) ,
                                 width=10, 
                                 text ="Sumbit Data", command=getvalues)
        Sumbit_Button.grid(row=15, columnspan=2)
    
        drive.geometry('550x600')
        drive.resizable(0,0)
        drive.mainloop()
        
        return Text_Box

# Class to store data of Drive in Database
class DBDrive(): 
    
    def __init__(self,Text_Box):
        self.Text_Box = Text_Box
    
    def StoreDriveInfo(self):
        
        file = r'Drive.db'
        
        # Create the database and store the values
        if os.path.isfile(file):
        
            dri = sqlite3.connect(file)
            dri_c = dri.cursor()
        
            insertq = """ INSERT INTO Drive(jobid,company,salary,venue,drive_date,eligibilty,
                    job_title,quality,no_rounds,backlogs,test_time,
                    cutoff_score) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"""
            dri_c.execute(insertq,tuple(self.Text_Box)) 
        
            d = dri.execute("""SELECT * FROM Drive""")
        
            for i in d:
                print(i)
            
            dri.commit()
            dri.close()
    
        else:
        
            dri = sqlite3.connect(file)
            dri_c = dri.cursor()
        
            query = """
                    CREATE TABLE Drive(
                    jobid TEXT , 
                    company TEXT , 
                    salary TEXT ,
                    venue TEXT ,
                    drive_date TEXT,    
                    eligibilty TEXT ,         
                    job_title TEXT ,
                    quality TEXT , 
                    no_rounds TEXT ,
                    backlogs TEXT ,
                    test_time TEXT ,
                    cutoff_score TEXT);"""
            dri.execute(query)
        
            insertq = """ INSERT INTO Drive(jobid,company,salary,venue,drive_date,eligibilty,
                          job_title,quality,no_rounds,backlogs,test_time,cutoff_score) 
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"""
            dri_c.execute(insertq,tuple(self.Text_Box))

            dri.commit()
            dri.close()

# Class to generate the list of eligible students        
class Eligibility():
    
    def GetEligibility(self):
        file1 = r'Drive.db'
        file2 = r'Student.db'
        Input_fields1 = ['Job Id','Company','Salary','Venue','Drive Date','Eligibilty',
                         'Job Title','Quality','No of Rounds','Backlogs','Test Time',
                         'Cutoff Score']
        Input_fields2 = ["Name","Roll Number","Email Id","CGPA","Active backlogs","Stream"]
    
        if os.path.isfile(file1):
        
            dri = sqlite3.connect(file1)
            d = dri.execute("""SELECT * FROM Drive """)
            d = list(d)
            Drive =  pd.DataFrame(d , columns=Input_fields1)
            Drive = Drive.replace(to_replace='None', value=np.nan)
            Drive = Drive.dropna()
            Drive['K'] = 1
    
        if os.path.isfile(file2):
        
            stu = sqlite3.connect(file2)
            s = stu.execute("""SELECT * FROM Student""")
            s = list(s)
            Student = pd.DataFrame(s , columns=Input_fields2)
            Student = Student.replace(to_replace='None', value=np.nan)
            Student = Student.dropna()
            Student['K'] = 1
        
        Eligibility = pd.merge(Student,Drive,on ='K')
        Eligibility = Eligibility.drop('K',axis=1)

        Eligibility['Active backlogs'] = Eligibility['Active backlogs'].astype(float).astype('int64')
        Eligibility['Backlogs'] = Eligibility['Backlogs'].astype(float).astype('int64')
        Eligibility['CGPA'] = Eligibility['CGPA'].astype(float).astype('int64')
        Eligibility['Eligibilty'] = Eligibility['Eligibilty'].astype(float).astype('int64')
    
        Eli = Eligibility[(Eligibility['Active backlogs']<=Eligibility['Backlogs']) & 
                      (Eligibility['CGPA'] >= Eligibility['Eligibilty'])]  
        
        # Store the data of eligible students
        Eli.to_csv('Eligibility.csv')
        
        return Eli

# Class to send notification to eligible students        
class SendEligibleNotifications(Eligibility):
    
    def EligibleNotifications(self):
        
        Eli = Eligibility.GetEligibility(self)
        for i in range(Eli.shape[0]):
                P
                l = list(Eli.iloc[i])
                server = "smtp.gmail.com"
                port = 587
                
                message = """Hi %s,\n\n You are eligible for the Company named %s.\n
            Find the details for the campus drive :
                Job ID : %s
                Job Title : %s
                Salary : %s
                Venue : %s
                Drive Date : %s
                Test Time : %s
                No. of Rounds : %s\n
    Regards,
    XYZ
    Placement Cell\n"""%(l[0],l[7],l[6],l[12],l[8],l[9],l[10],l[16],l[14])
                
                
                conn = email.SMTP(server,port)
                conn.ehlo()
                sender_mail =  "mtaniketakhand@gmail.com" 
                password = "OOPDProject123@"
                conn.starttls()
                conn.login(sender_mail, password)
                receiver_mail = [l[2]]
                conn.sendmail(sender_mail,receiver_mail,message)
                conn.close() 
                print(message) 
            
            
        print('Mail Send To Eligible Students')

# Class to get the data about the Score of candidate in different rounds    
class TrackData():
    
    def GetTrackInfo(self):  
        track = T.Tk()
        track.configure(bg='light cyan')
        Input_fields = ["JobID","Name","Email","Number of Rounds",
                        "Score 1","Score 2","Score 3"]
        variables = []
        
        for i in range(len(Input_fields)):
            variables.append(T.StringVar())
    
        track.title("Track Score Portal")
        T.Label(track,
                height=3,
                width=31,
                anchor=CENTER,
                #relief=RAISED,
                font=("Georgia", 20,'bold') , 
                bg="cyan", 
                fg="black" , 
                text="Track Score Portal").grid(row=0,columnspan=2)
        
        Text_Box = [None for i in range(len(Input_fields))]
        for i in range(0,len(Input_fields)):
            T.Label(track,
                    height=2,
                    width=20,
                    anchor=W , 
                    font=("Cubano", 16) , 
                    bg="light cyan", 
                    fg="black" ,
                    text=Input_fields[i]).grid(row=i+2)
            T.Entry(track,textvariable=variables[i]).grid(row=i+2, column=1)    

        def getvalues():
            for i in range(len(Input_fields)):
                Text_Box[i] = variables[i].get()
            messagebox.showinfo("","Data Sumbitted")
            track.destroy()
        
        Sumbit_Button = T.Button(track,
                                 bg="light cyan",
                                 font=("Cubano", 11) ,
                                 width=10, 
                                 text ="Sumbit Data", command=getvalues)
        Sumbit_Button.grid(row=9, columnspan=2)
    
        track.geometry('550x600')
        track.resizable(0,0)
        track.mainloop()
        
        return Text_Box
    
# Class to store data of Track in Database
class DBTrack():
    
    def __init__(self,Text_Box):
        self.Text_Box = Text_Box
    
    def StoreTrackInfo(self):
        file = r'Track.db'
    
        if os.path.isfile(file):
            
            tra = sqlite3.connect(file)
            tra_c = tra.cursor()
            
            insertq = """INSERT INTO Track(JobID,Name,Email,NumberofRounds,Score1,Score2,Score3)VALUES(?,?,?,?,?,?,?)"""
            tra_c.execute(insertq,tuple(self.Text_Box)) 
        
            t = tra.execute("""SELECT * FROM Track""")
        
            for x in t:
                print(x)
        
            tra.commit()
            tra.close()
    
        else:
        
            tra = sqlite3.connect(file)
            tra_c = tra.cursor()
        
            query = """
            CREATE TABLE Track (
                    JobID TEXT , 
                    Name TEXT , 
                    Email TEXT ,
                    NumberofRounds TEXT ,
                    Score1 TEXT , 
                    Score2 TEXT ,
                    Score3 TEXT );"""
            tra.execute(query)
        
            insertq = """INSERT INTO Track(JobID,Name,Email,NumberofRounds,Score1,Score2,Score3)VALUES(?,?,?,?,?,?,?)"""
            tra_c.execute(insertq,tuple(self.Text_Box))

            tra.commit()
            tra.close()
            
        return self.Text_Box     
            
# Class to send notification to selected/unselected students   
class SendSelectedNotifications(DBTrack):
    
    def __init__(self, Text_Box):
        self.Text_Box = Text_Box
        
    
    def SelectedNotifications(self):
        
        Text_Box = DBTrack.StoreTrackInfo(self)
        c = 60
        total = 0
        
        if int(Text_Box[3])==1 :
            total = int(Text_Box[4])
        elif int(Text_Box[3])==2 :
            total = int(Text_Box[4]) + int(Text_Box[5])
        elif int(Text_Box[3])==3 :
            total = int(Text_Box[4]) + int(Text_Box[5]) + int(Text_Box[6])
        else :
            total = 0        
        if total > c:
            server = "smtp.gmail.com"
            port = 587
            mess = """Hi %s,\n\n You are selected for Job ID : %s\n\nXYZ\nGeneral Manager"""%(Text_Box[1],Text_Box[0])
            t = T.Tk()
            messagebox.showinfo("",mess)
            t.destroy()
            
            conn = email.SMTP(server,port)
            conn.ehlo()
            sender_mail =  "mtaniketakhand@gmail.com" 
            password = "OOPDProject123@"
            conn.starttls()
            conn.login(sender_mail, password)
            receiver_mail = [Text_Box[2]]
            conn.sendmail(sender_mail,receiver_mail,mess)
            conn.close() 
            print('Mail Send')
            
        else:
            server = "smtp.gmail.com"
            port = 587
            mess = """Hi %s,\n\n We are sorry to inform you that you are not selected for Job ID : %s\n\nXYZ\nGeneral Manager"""%(Text_Box[1],Text_Box[0])
            t = T.Tk()
            messagebox.showinfo("",mess)
            t.destroy()
            
            conn = email.SMTP(server,port)
            conn.ehlo()
            sender_mail =  "mtaniketakhand@gmail.com" 
            password = "OOPDProject123@"
            conn.starttls()
            conn.login(sender_mail, password)
            receiver_mail = [Text_Box[2]]
            conn.sendmail(sender_mail,receiver_mail,mess)
            conn.close() 
            print('Mail Send')

# Class to get choices based on the inputs
class CampusPlacementDrive():

    
    def GetChoice(self):
        
        main = T.Tk()
        main.configure(bg='light cyan')
        Input_fields = ["Input 1 : Company Data Portal",
                        "Input 2 : Student Data Portal",
                        "Input 3 : Drive Data Portal",
                        "Input 4 : Send Drive Information to the Eligible Students",
                        "Input 5 : Track Score Portal"]
        variables = []
    
        for i in range(len(Input_fields)):
            variables.append(T.StringVar())
    
        main.title("Campus Recruitment System ")
    
        T.Label(main,
            height=5,
            width=65,
            anchor=CENTER,
            font=("Georgia", 25,'bold') , 
            bg="cyan", 
            fg="black" , 
            text="Campus Recruitment System").grid(row=0,column=0)
    
    
        Text_Box = [None for i in range(len(Input_fields))]
        for i in range(0,len(Input_fields)):
            T.Label(main,
                height=2,
                width=65,
                anchor=W , 
                font=("Cubano", 16) , 
                bg="light cyan", 
                fg="black" , 
                text=Input_fields[i]).grid(row=i+1,column=0)
        
        T.Entry(main,
            textvariable=variables[0],	
            width=50,
            bd = 3,
            selectborderwidth = 2).grid(row=20,column=0)  

        def getvalues():
            for i in range(len(Input_fields)):
                Text_Box[i] = variables[i].get()
            main.destroy()
        
        Sumbit_Button = T.Button(main,
                             height=1,
                             width=20,
                             bg="light cyan",
                             font=("Cubano", 12) ,
                             text ="Sumbit Data", command=getvalues)
        
       
        Sumbit_Button.grid(row=25, columnspan=2)
    
        main.geometry('1430x800')
        main.resizable(0, 0) 
    
        main.mainloop()
        
        if(int(Text_Box[0]) in [1,2,3,4,5]):
            return Text_Box
        else:
            return [0]
        
    
P = CampusPlacementDrive()
cho = P.GetChoice() 

if cho[0] !=0:
    Pa = Page(cho)
    Pa.MainPage()

            
            
            
        
        
    
