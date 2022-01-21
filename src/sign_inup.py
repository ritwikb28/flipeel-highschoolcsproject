import sys 
import pymysql as mysqltr
import pyfiglet
#establishing connection from mysql server
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

#if con.is_connected() == False:
    #print("error")
result = pyfiglet.figlet_format("SIGN IN PAGE")
print(result)
#cursor for organised implementation of query
cursor = con.cursor()
#taking choice from client for logical blocks
forward = input("sign in (I)/ sign up(U)")
#logical block 1: sign in page for client. 
if forward == "I":
    name = input("name:") #recording client name to match + provided two ways to get into the login service: phone number or email id
    sinput = input('''sign in using
    phone number (ph)
    email_id (ei)''')
    #logical block 1A: log in service using phone number
    if sinput == "ph":
        ph = int(input("phone number:")) #takes phone number from the user and saves it in a variable.
        sql1 = "select name from user_data where ph_no = %a" #sql query for getting name of the user with whom the phone number taken as an input is associated 
        y = cursor.execute(sql1,ph) #replaces placeholder by the variable and execute
        con.commit() 
        #logical block 1A(i)
        if y == 1: # y indicates the number of rows effected so we need one line to be effected by the program
            print("welcome to flipeel", name)
            #sign in welcome

            print("---------reverting to main page---------")
        else: #if more or none rows are effected by our query which indiacted there is no number associated in the data base or logical error
            print("Invalid credentials. Log in failed.")
            sys.exit() #breaks the program as sign in is required in order to use the services of flipeel
    #logical block 1B: log in srvice using email id
    elif sinput == "ei":  
        ei = str(input("email id:"))
        sql1 = "select name from user_data where email = %a" #creating a query with a placeholder for the email id saved in the variable. 
        y = cursor.execute(sql1,ei) #executing the query
        con.commit() #commiting the changes made in the data base through the query
        #logical block 1B(i)
        if y == 1: 
            print("welcome to flipeel", name) #welcomes to services if one line is found to be associated to the given detail.
            import smtplib
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("sender email", "sender email password")
            message = '''SIGN IN COMFIRMATION FROM FLIPEEL.
            Hi! I am Ritwik Bhardwaj from FLIPEEL
            Thank you for signing in and using our application service.
            Have an amazing day:)
            Stay safe.
            PS: do not reply to this email.











            flipeel 2022 <3                        '''
            s.sendmail("sender email", ei, message)
            s.quit()
            
            print("----reverting to main page----")
        else:
            print("Invalid credentials. Log in failed.")
            sys.exit() #breaks program for the user as log in is a mandatory action

    else:
        print("unidentified error: sorry for inconvinience")
#logical block 2: directing to sign up services
elif forward == "U":
    import server_side #importing and calling the file created in this folder
    server_side
else:
    print("We are not able to log in you this moment:(") #general program failed error