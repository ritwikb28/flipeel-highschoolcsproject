import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

#if con.is_connected() == False:
    #print("error")

cursor = con.cursor() #establishing a connection with the localhost of mysql db to acces project tables
print("please note that you are now creating an account") 
proceed = input("N/Y\n") #making sure that user knows that proceeding this level of the program will lead them to account creation with the application
if proceed == "N": 
    print("thank you")
    signin = input('do you want to sign in instead?') #tackling situation in order to help the client proceed otherwise and keep them in the application loop
    import sign_inup
    sign_inup         #importing and calling the main signin page in this folder to help user manage their account
elif proceed == "Y": #proceeding to access databse in order to create the account
    #follwowing is creation of a query that inserts details of the client accordingly
    sql = "insert into `user_data` (`name`, `ph_no`,`email`, `prod`, `city`, `date`) Values(%s, %s, %s, %s, %s, %s)"
    name = input("name:")
    ph_no = int(input("phone number:"))
    email = input("email id:")             #taking various details and saving them in variables
    prod = input("product of intrest:")
    city = input("city of residence:")
    print("date format: yyyy-mm-dd") #specifying date format
    date = input("date:")
    cursor.execute(sql, (name, ph_no, email, prod, city, date )) #executing the query and replacing all placeholders with variables

con.commit() #commiting all changes to database
import smtplib #email communication
s = smtplib.SMTP('smtp.gmail.com', 587) #connecting to server and establish port connection (TLS)
s.starttls() #starting tls connection
s.login("sender email", "sender email password") ##MESSEGE TO BE SENT VIA THE SYSTEM## // following is a sign up confirmation email
message = '''SIGN UP CONFIRMATION FROM FLIPEEL  
Hi! I am Ritwik Bhardwaj from FLIPEEL
Thank you for signing up with us.
We look forward to serving you.
Have an amazing day:)
Stay safe.



PS: It is not you? Reply this email with a 'DELETE_NOT_ME' and we will erase all data associated with this account:) 






flipeel 2022 <3                        '''
s.sendmail("sender email", email, message) #sending out the email
s.quit() #exiting the server connection




