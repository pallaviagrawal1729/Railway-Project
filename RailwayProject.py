#importing the modules
import mysql.connector as sqltor

#establishing connection and verifying if established properly or not
mycon=sqltor.connect(host='localhost',user='root', passwd='passnew',database='RAILWAY')
if(mycon.is_connected()):
    for i in range(0,190):
        print('*',end='')
    print("******************************************************************WELCOME TO OUR RAILWAY PROJECT. I HOPE YOU FIND IT USEFUL******************************************************************")
    for i in range(0,190):
        print('*',end='')
else:
    print("SORRY! The connection could not be established. Contact the host.")
    
#creating the cursor
cursor=mycon.cursor()

def loginOrRegister():
    login_or_register=True
    while(login_or_register):
        print("1. Are you an existing user?")
        print("2. Are you here for the first time?")
        enter=int(input())
        if(enter==1):
            username=input("Please enter your username: ")
            password=input("Please enter your password: ")
            cursor.execute("select * from customer_login")
            log=cursor.fetchall()
            for row in log:
                if(row[0]==username and row[1]==password):
                    login_or_register=False
                    break
            if(login_or_register==True):
                print("\n Sorry your username and password did not match! \n")
        elif(enter==2):
            print("Please provide your following details ")
            print("--------------------------------------")
            name=input("Name: ")
            gender=input("Gender(Male/ Female/ Other): ")
            dob=input("What is your date of birth(yyyy-mm-dd): ")
            phoneNo=input("Phone Number: ")
            country=input("Country: ")
            state=input("State: ")
            pinCode=input("Pin-Code: ")
            username=input("Please select a username: ")
            password=input("Please provide password for security (better to have a combination of letters, numbers, special characters with 7 char min): ")
            insertRegister="insert into register values ('{}','{}','{}','{}','{}',{},'{}','{}',{})".format(username,password,name,gender,dob,phoneNo,country,state,pinCode)
            insertLogin=("insert into customer_login values('{}','{}')".format(username,password))
            cursor.execute(insertRegister)
            cursor.execute(insertLogin)
            mycon.commit()
            login_or_register=False
        
def goFromStation():
    print("You have the following places to go from ")
    print("1.Haryana\n2.Madhya Pradesh\n3.Uttar Pradesh\n4.Delhi\n5.Uttrakhand\n6.Punjab\n7.Goa\n8.Jammu & Kashmir\n9.Rajasthan\n10.Gujarat\n11.Tamil Nadu\n12.Maharashtra")
    goFrom=int(input("Please choose One: "))
    print("You have the following famous stations to go from \n")
    if(goFrom==1):
        cursor.execute("select * from statecitystat where state='Haryana'")
    elif(goFrom==2):
        cursor.execute("select * from statecitystat where state='Madhya Pradesh'")
    elif(goFrom==3):
        cursor.execute("select * from statecitystat where state='Uttar Pradesh'")
    elif(goFrom==4):
        cursor.execute("select * from statecitystat where state='Delhi'")
    elif(goFrom==5):
        cursor.execute("select * from statecitystat where state='Uttrakhand'")
    elif(goFrom==6):
        cursor.execute("select * from statecitystat where state='Punjab'")
    elif(goFrom==7):
        cursor.execute("select * from statecitystat where state='Goa'")
    elif(goFrom==8):
        cursor.execute("select * from statecitystat where state='Jammu and Kashmir'")
    elif(goFrom==9):
        cursor.execute("select * from statecitystat where state='Rajasthan'")
    elif(goFrom==10):
        cursor.execute("select * from statecitystat where state='Gujarat'")
    elif(goFrom==11):
        cursor.execute("select * from statecitystat where state='Tamil Nadu'")
    elif(goFrom==12):
        cursor.execute("select * from statecitystat where state='Maharashtra'")
    else:
        print("\n------------------------------------------------------------You Entered invalid choice--------------------------------------------------------------\n")
        return (False,None)
    data=cursor.fetchall()
    index=1
    print("______________________________________\n")
    print("{} {:<20} {:^20}".format("Sno.","City","Station"))
    for row in data:
        print("{} {:<20} {:^20}".format(index,row[1],row[2]))
        index+=1
    print("______________________________________")
    try:
        goFrom=int(input("Choose one: "))
        goFromPlatform=data[goFrom-1][2]
        return (True,goFromPlatform)
    except IndexError:
        print("\n------------------------------------------------------------You Entered invalid choice--------------------------------------------------------------\n")
        return(False,None)

def goToStation(trip_from,goFromPlatform):
    while(not(trip_from)):
        (trip_from,goFromPlatform)=goFromStation()
    print("You have the following places to go To ")
    print("1.Haryana\n2.Madhya Pradesh\n3.Uttar Pradesh\n4.Delhi\n5.Uttrakhand\n6.Punjab\n7.Goa\n8.Jammu & Kashmir\n9.Rajasthan\n10.Gujarat\n11.Tamil Nadu\n12.Maharashtra")
    goTo=int(input("Please choose One: "))
    print("You have the following famous stations to go To \n")
    if(goTo==1):
        cursor.execute("select * from statecitystat where state='Haryana'")
    elif(goTo==2):
        cursor.execute("select * from statecitystat where state='Madhya Pradesh'")
    elif(goTo==3):
        cursor.execute("select * from statecitystat where state='Uttar Pradesh'")
    elif(goTo==4):
        cursor.execute("select * from statecitystat where state='Delhi'")
    elif(goTo==5):
        cursor.execute("select * from statecitystat where state='Uttrakhand'")
    elif(goTo==6):
        cursor.execute("select * from statecitystat where state='Punjab'")
    elif(goTo==7):
        cursor.execute("select * from statecitystat where state='Goa'")
    elif(goTo==8):
        cursor.execute("select * from statecitystat where state='Jammu and Kashmir'")
    elif(goTo==9):
        cursor.execute("select * from statecitystat where state='Rajasthan'")
    elif(goTo==10):
        cursor.execute("select * from statecitystat where state='Gujarat'")
    elif(goTo==11):
        cursor.execute("select * from statecitystat where state='Tamil Nadu'")
    elif(goTo==12):
        cursor.execute("select * from statecitystat where state='Maharashtra'")
    else:
        print("\n------------------------------------------------------------You Entered invalid choice--------------------------------------------------------------\n")
        return (trip_from,goFromPlatform,False,None)
    data=cursor.fetchall()
    index=1
    print("______________________________________\n")
    print("{} {:<20} {:^20}".format("Sno.","City","Station"))
    for row in data:
        print("{} {:<20} {:^20}".format(index,row[1],row[2]))
        index+=1
    print("______________________________________")
    try:
        goTo=int(input("Choose one: "))
        goToPlatform=data[goTo-1][2]
        return (trip_from,goFromPlatform,True,goToPlatform)
    except IndexError:
        print("\n------------------------------------------------------------You Entered invalid choice--------------------------------------------------------------\n")
        return (trip_from,goFromPlatform,False,None)

def Journey():
    loginOrRegister()
    (trip_from,goFromPlatform,trip_to,goToPlatform)=goToStation(False,None)
    while(not(trip_to)):
        (trip_from,goFromPlatform,trip_to,goToPlatform)=goToStation(True,goFromPlatform)
    print("\n\t\t\t\t\t\t\tFROM STATION: {}".format(goFromPlatform))
    for i in range(1,190):
        print('*',end='')
    print("\n")
    for i in range(0,4):
        for j in range(0,12):
            print(" * *\t\t",end='')
        print("\n")
    for i in range(1,190):
        print('*',end='')
    print("\n")
    print("\t\t\t\t\t\t\tTO STATION: {}\n".format(goToPlatform))
    cursor.execute("select * from train")
    trains=cursor.fetchall()
    trainFound=False
    for trainInfo in trains:
        cursor.execute("select * from `{}`".format(trainInfo[1]))
        checkStationsOfTrain=cursor.fetchall()
        fromStationMatch=False
        toStationMatch=False
        for station in checkStationsOfTrain:
            if(not(fromStationMatch and toStationMatch)):
                if(station[1]==goFromPlatform):
                    fromStationMatch=True
                if(station[1]==goToPlatform):
                    toStationMatch=True
        if(fromStationMatch and toStationMatch):
            trainFound=True
            for i in range(0,190):
                print("*",end='')
            print("\n")
            print("TRAIN NAME: {}".format(trainInfo[1]))
            print("TRAIN NUMBER: {}".format(trainInfo[0]))
            print("ITS ROUTE IS: ")
            cursor.execute("select * from `{}`".format(trainInfo[1]))
            stations=cursor.fetchall()
            for station in stations:
                print("{:<20} {:^20}".format(station[0],station[1]))
            for i in range(0,190):
                print("*",end='')
            print("\n")
    if(trainFound==False):
        print("\nPlease try with some other stations\n")
        
Journey()