def seateconomy():
    print("\n\n\nKINDLY SELECT YOUR SEAT NUMBER for economy class")
    for x in range(1,4):
        print("\n\n")
        for y in range(1,8):
            print("[",x,"-",y,"]",end="   ")
    print("\n\n\n")
    for x in range(4,7):
        print("\n\n")
        for y in range(1,8):
            print("[",x,"-",y,"]",end="   ")
    print("\n\n\n")
    for x in range(7,10):
        print("\n\n")
        for y in range(1,8):
            print("[",x,"-",y,"]",end="   ")
def seatbusiness():
    print("\n\n\nKINDLY SELECT YOUR SEAT NUMBER for BUSINESS class")
    for x in range(1,2):
        print("\n\n")
        for y in range(1,8):
            print("[",x,"-",y,"]",end="   ")
    print("\n\n\n")
    for x in range(2,4):
        print("\n\n")
        for y in range(1,8):
            print("[",x,"-",y,"]",end="   ")
    print("\n\n\n")
    for x in range(4,5):
        print("\n\n")
        for y in range(1,8):
            print("[",x,"-",y,"]",end="   ")
def seatexecutive():
    print("\n\n\nKINDLY SELECT YOUR SEAT NUMBER for EXECUTIVE class")
    for x in range(1,2):
        print("\n\n")
        for y in range(1,8):
            print("[",x,"-",y,"]",end="   ")
    print("\n\n\n")
    for x in range(2,3):
        print("\n\n")
        for y in range(1,8):
            print("[",x,"-",y,"]",end="   ")
def newticketentry():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successfully connected")
    cursor=connector.cursor()
    a=str(input("Enter your name here:"))
    b=str(input("Enter the location you want to start the journey from:"))
    c=str(input("Enter the destination you want to visit:"))
    d=str(input("Enter the date of journey in YYYY/MM/DD format:"))
    f=str(input("Please enter the CLASS of which you want a seat of from the following:-\n\n1.ECONOMY CLASS\n2.BUSINESS CLASS\n3.EXECUTIVE CLASS\n\n\nPlease enter your choice here in capital letters only: "))
    seattype(f)
    e=str(input("Enter the seat number of the seat you like:"))
    abcd="insert into ticket values('{}','{}','{}','{}','{}','{}')".format(a,b,c,d,f,e)
    cursor.execute(abcd)
    connector.commit()
def newflightentry():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successfully connected")
    cursor=connector.cursor()
    a=str(input("Enter your name here:"))
    b=str(input("Enter the place of departure:"))
    c=str(input("Enter the place of arrival:"))
    d=str(input("Enter the date of flight in YYYY/MM/DD format:"))
    e=str(input("Enter Arrival time in HH/MM/SS format:"))
    f=str(input("Enter departure time in HH/MM/SS format:"))
    abcdef="insert into pilot values('{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f)
    cursor.execute(abcdef)
    connector.commit()
def welcome():
    x=" INDIGO AIRLINES ONLINE SERVICE PORTAL "
    y="*".join(x)
    z="         "
    print("\n\n\n",z,y,z)
def createtableticket():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successful connection")
    cursor=connector.cursor()
    a="create table ticket(name varchar(30) not null primary key,departure varchar(30) not null,arrival varchar(30) not null,TRAVELdate varchar(30) not null,seatclass varchar(30) not null,seatnumber varchar(10) not null);"
    cursor.execute(a)
    connector.commit()
def seattype(f):
    if f=="ECONOMY CLASS":
        seateconomy()
    elif f=="BUSINESS CLASS":
        seatbusiness()
    elif f=="EXECUTIVE CLASS":
        seatexecutive()
    else:
        print("Please enter a valid choice")
        seattype(f)
def droptableticket():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successfully connected")
    cursor=connector.cursor()
    abcdefg="drop table if exists ticket;"
    cursor.execute(abcdefg)
    connector.commit()
def createtablepilot():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successful connection")
    cursor=connector.cursor()
    a="create table pilot(name varchar(30) not null primary key,departure varchar(30) not null,arrival varchar(30) not null,Date varchar(30) not null,departuretime varchar(30) not null,arrivaltime varchar(30) not null);"
    cursor.execute(a)
    connector.commit()
def droptablepilot():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successfully connected")
    cursor=connector.cursor()
    abcdefg="drop table if exists pilot;"
    cursor.execute(abcdefg)
    connector.commit()
def createtablestaff():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successful connection")
    cursor=connector.cursor()
    a="create table staff(name varchar(30) not null primary key,designation varchar(30) not null,arrival varchar(30) not null,departure varchar(30) not null,traveldate varchar(30) not null,departuretime varchar(30) not null,arrivaltime varchar(30) not null);"
    cursor.execute(a)
    connector.commit()    
def newflightentry1():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successfully connected")
    cursor=connector.cursor()
    a=str(input("Enter your name here:"))
    b=str(input("Enter your designation:"))
    c=str(input("Enter the place of arrival:"))
    d=str(input("Enter the place of departure"))
    g=str(input("Enter the travel date in YYYY/MM/DD format:"))
    e=str(input("Enter Arrival time in HH/MM/SS format:"))
    f=str(input("Enter departure time in HH/MM/SS format:"))
    abcdef="insert into staff values('{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,g,e,f)
    cursor.execute(abcdef)
    connector.commit()    
      
def droptablestaff():
    import mysql.connector as mysqlconnector
    connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
    if connector.is_connected:
        print("successfully connected")
    cursor=connector.cursor()
    abcdefg="drop table if exists staff;"
    cursor.execute(abcdefg)
    connector.commit()       
        
        
















droptablestaff()
droptableticket()
droptablepilot()
m=100
ace=0
while m>0:


    
    if ace==0:
        import mysql.connector as mysqlconnector
        connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
        if connector.is_connected:
            print("successful connection")
        cursor=connector.cursor()
        createtablepilot()
        createtableticket()
        createtablestaff()

        
        
    ace=ace+1
    



    welcome()
    x=str(input("\n\n\nKindly mention you are here as a:\n\n1.PASSENGER\n2.PILOT\n3.AIRHOSTESS\n4.VISITOR\n5.ANY OTHER STAFF\n\n\nPlease type your choice here in capital letters only:"))
    if x=="PASSENGER":
        print("\n\n    THANKYOU FOR CHOOSING INDIGO AIRLINES    ")
        y=str(input("\nKindly mention the reason you are here for:\n\n1.NEW TICKET BOOKING\n2.OLD TICKET REVIEW\n\nPlease type your choice here in capital letters only:"))
        if y=="NEW TICKET BOOKING":
            print("      PLEASE WAIT      \n       REDIRECTING WINDOWS       \n\n")
            print("processing")
            
            newticketentry()
        elif y=="OLD TICKET REVIEW":
            import mysql.connector as mysqlconnector
            connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
            if connector.is_connected:
                print("successfully connected")
            cursor=connector.cursor()
            t=str(input("PLEASE MENTION YOUR FULL NAME AS PER YOUR TICKET:"))
            query="select * from ticket where name='{}'".format(t)
            cursor.execute(query)
            s=cursor.fetchall()
            print(s)
        else:
            print("\nPLEASE ENTER A VALID RESPONSE")
        print("\n\nTHANKYOU FOR CHOOSING INDIGO AIRLINES")
        a=str(input("\n\nDO YOU WANT TO CLOSE THE TAB?\n\n if YES type anything here:"))
        if a=="yes":
            print("THANK YOU")
        else:
            print("THANK YOU")
    elif x=="PILOT":
        print("\n\n   INDIGO AIRLINES WELCOMES YOU BACK   ")

        import mysql.connector as mysqlconnector
        connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
        if connector.is_connected:
            print("successfully connected")
        cursor=connector.cursor()
        
        a=str(input("Please mention what for you are here:\n\n1.NEW FLIGHT REGISTRATION\n2.OLD FLIGHT REVIEW\n\n\nPlease enter your chioce here:"))
        if a=="NEW FLIGHT REGISTRATION":
            newflightentry()
        elif a=="OLD FLIGHT REVIEW":
            import mysql.connector as mysqlconnector
            connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
            if connector.is_connected:
                print("successfully connected")
            cursor=connector.cursor()
            t=str(input("PLEASE MENTION YOUR FULL NAME AS PER YOUR ENTRY REGISTRATION:"))
            query="select * from pilot where name='{}'".format(t)
            cursor.execute(query)
            s=cursor.fetchall()
            print(s)
        else:
            print("\nPLEASE ENTER A VALID RESPONSE")
        print("\n\nTHANKYOU FOR CHOOSING INDIGO AIRLINES")
        a=str(input("\n\nDO YOU WANT TO CLOSE THE TAB?\n\n if YES type anything here:"))
        if a=="yes":
            print("THANK YOU")
        else:
            print("THANK YOU")
        
        
            
        
       
        
    elif x=="AIRHOSTESS":



        print("\n\n   INDIGO AIRLINES WELCOMES YOU BACK   ")

        import mysql.connector as mysqlconnector
        connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
        if connector.is_connected:
            print("successfully connected")
        cursor=connector.cursor()
       
        a=str(input("Please mention what for you are here:\n\n1.NEW FLIGHT REGISTRATION\n2.CHECK FLIGHT DETAILS\n\n\nPlease enter your chioce here:"))
        if a=="NEW FLIGHT REGISTRATION":
            newflightentry()
        elif a=="CHECK FLIGHT DETAILS":
            import mysql.connector as mysqlconnector
            connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
            if connector.is_connected:
                print("successfully connected")
            cursor=connector.cursor()
            t=str(input("PLEASE MENTION YOUR FULL NAME AS PER YOUR ENTRY REGISTRATION:"))
            query="select * from pilot where name='{}'".format(t)
            cursor.execute(query)
            s=cursor.fetchall()
            print(s)
        else:
            print("\nPLEASE ENTER A VALID RESPONSE")
        print("\n\nTHANKYOU FOR CHOOSING INDIGO AIRLINES")
        a=str(input("\n\nDO YOU WANT TO CLOSE THE TAB?\n\n if YES type anything here:"))
        if a=="yes":
            print("THANK YOU")
        else:
            print("THANK YOU")





        
        
        
       
        
        
    elif x=="VISITOR":
        print("                     DESCRIPTION                 \nIndiGo is an Indian low-cost airline headquartered in Gurugram,\n Haryana, India. It is the largest airline in India by \npassengers carried and fleet size, with a 60.4% domestic market \nshare as of July 2020.[6] It is also the largest individual \nAsian low-cost carrier in terms of jet fleet size and passengers\n carried, and the sixth largest carrier in Asia with over 6.4 crore (64 million)\n passengers carried in financial year 2018–19.\n The airline operates 1,500 flights everyday[7] to 87 destinations\n – 63 domestic and 24 international.[8] It has its primary hub at Indira Gandhi \nInternational Airport, Delhi.[9]\nThe airline was founded as a private company by Rahul Bhatia \nof InterGlobe Enterprises and Rakesh Gangwal in 2006.\n It took delivery \nof its first aircraft in July 2006 and commenced operations a month later. \nThe airline became the largest Indian carrier by passenger market share in 2012.\n The company went public in November 2015")
        print("\n\n\n                     HISTORY                     \n\n\nIndiGo was founded in 2006 as a private company by Rahul Bhatia\n of InterGlobe Enterprises and Rakesh Gangwal.[11] InterGlobe had\n a 51.12% stake in IndiGo and 47.88% was held by Gangwal's Virginia-based\n company Caelum Investments.[12][13] IndiGo placed a firm\n order for 100 Airbus A320-200 aircraft in June 2005 with\n plans to begin operations in mid-2006.[14] IndiGo took delivery of\n its first aircraft on 28 July 2006, nearly a year after placing\n the order.[15] It commenced operations on 4 August 2006\n with a service from New Delhi to Imphal via Guwahati.[16] By the end\n of 2006, the airline had six aircraft, and nine more were\n acquired in 2007.[16] In December 2010, IndiGo replaced state-run carrier\n Air India as the third largest airline in India, behind\n Kingfisher Airlines and Jet Airways with a passenger market share of 17.3%.[17]")
        print("\n\nTHANKYOU FOR CHOOSING INDIGO AIRLINES")
        a=str(input("\n\nDO YOU WANT TO CLOSE THE TAB?\n\n if YES type anything here:"))
        if a=="yes":
            print("THANK YOU")
        else:
            print("THANK YOU")
    elif x=="ANY OTHER STAFF":



        print("\n\n   INDIGO AIRLINES WELCOMES YOU BACK   ")

        import mysql.connector as mysqlconnector
        connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
        if connector.is_connected:
            print("successfully connected")
        cursor=connector.cursor()
        
        a=str(input("Please mention what for you are here:\n\n1.NEW FLIGHT REGISTRATION\n2.CHECK FLIGHT DETAILS\n\n\nPlease enter your chioce here:"))
        if a=="NEW FLIGHT REGISTRATION":
            newflightentry1()
        elif a=="CHECK FLIGHT DETAILS":
            import mysql.connector as mysqlconnector
            connector=mysqlconnector.connect(host="localhost",user="root",passwd="root",database="csproject")
            if connector.is_connected:
                print("successfully connected")
            cursor=connector.cursor()
            t=str(input("PLEASE MENTION YOUR FULL NAME AS PER YOUR ENTRY REGISTRATION:"))
            query="select * from staff where name='{}'".format(t)
            cursor.execute(query)
            s=cursor.fetchall()
            print(s)
        else:
            print("\nPLEASE ENTER A VALID RESPONSE")
        print("\n\nTHANKYOU FOR CHOOSING INDIGO AIRLINES")
        a=str(input("\n\nDO YOU WANT TO CLOSE THE TAB?\n\n if YES type anything here:"))
        if a=="yes":
            print("THANK YOU")
        else:
            print("THANK YOU")



        
        
    else:
        print("PLEASE ENTER A VALID RESPONSE")
        print("\n\nTHANKYOU FOR CHOOSING INDIGO AIRLINES")
        a=str(input("\n\nDO YOU WANT TO CLOSE THE TAB?\n\n if YES type anything here:"))
        if a=="yes":
            print("THANK YOU")
        else:
            print("THANK YOU")
