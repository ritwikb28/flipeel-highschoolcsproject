import pyfiglet
import pymysql as mysqltr
result = pyfiglet.figlet_format("YOUR ACCOUNT")
print(result)
#establishing connected with mysql on computer server to retrive the application's databse
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

hello = input("do you already have an account? (y/n)") #confiriming account status
#logical block 1: dashboard for pre existing account
if hello == "y" :
        acc = input('''proceed to dashboard? (d)''') #program requires confiramtion to move on for deleting and updating the account.
        #logical block 1A: retrieving all data from the table of the project data base
        if acc == "d": 
            name = input("account name:")
            cursor = con.cursor()
            sql = "select * from user_data where Name = %s " #creating a query for the required action of finding details related to client's name in the db
            cursor.execute(sql, [name]) #executing the same 
            #asking client to whether they want to update details or delete
            hi = input("do you intend to update acc details or delete? (u/d)")
            #logical block 1A (i): details to be updated
            if hi == "u":
                #giving client option of details to update
                change = input('''what do you want to change:
                Name (n)
                PhoneNumber (p)
                EmailId (e)''')
                #logical block 1A(i).1: name updation system
                if change == "n":
                    ph = int(input("confirm your phone number"))
                    updated_n = input("updated name:")
                    sql1 = "update user_data SET name = %s WHERE ph_no = %a" #creating query for the action.
                    y = cursor.execute(sql1, ([updated_n],ph)) #executing the query by replacing the placeholder with the pre saved variable.
                    con.commit()
                    if y == 1:
                        print("detail updated") #indicates that a row is effected and the required change has been reflected in the database's table
                        print("rerun for multiple edits")
                #logical block 1A(i).2: phone number updation system
                elif change == "p":
                    ph = int(input("confirm your phone number"))
                    updated_p = int(input("updated phone:"))
                    sql1 = "update user_data SET ph_no = %s WHERE ph_no = %a" #creating the query that updates phone number of the user 
                    y = cursor.execute(sql1, ([updated_p],ph)) #executing by replacing the placeholder
                    con.commit()
                    if y == 1:
                        print("detail updated") #database's table effected
                        print("rerun for multiple edits")
                #logical block 1A(i).3
                elif change == "e":
                    ph = int(input("confirm your phone number"))
                    updated_id = input("updated emailid:")
                    sql1 = "update user_data SET email = %s WHERE ph_no = %a" #creating the query that updates phone number of the user 
                    y = cursor.execute(sql1, ([updated_id],ph))
                    con.commit()
                    #implemting the query and observing database change.
                    if y == 1:
                        print("detail updated")
                        print("rerun for multiple edits")
            #logical block 1A(ii): deleting details as per user's command
            elif hi == "d":
                #program requesting user's input to implement conditional blocks accordingly
                #erasing all account data is also an option given to the client
                delete = input('''what do you want to change:
                Name (n)
                PhoneNumber (p)
                EmailId (e)
                delete account(da)''')
                #logical block 1A(ii).1: logical deletion of name 
                if delete == "n":
                    n = int(input("confirm your phone number")) #taking number to associate the client's name with it
                    sql1 = "update user_data SET name = NULL WHERE ph_no = %a"  #query for setting the associated name as NONE
                    y = cursor.execute(sql1, [n]) #implementing the query
                    con.commit() #commiting all changes to the db's table
                    #following demarcates that the program has made changes to the table
                    if y == 1:
                        print("detail deleted")
                        print("rerun for multiple edits or to update") #if the client want to delete a detail again, a rerun is required.
                #logical block 1A(ii).2: logical deletion of phone number
                elif delete == "p":
                    ph = int(input("confirm your phone number")) #taking number to associate the client's already saved phone number in the db with it
                    sql1 = "update user_data SET ph_no = NULL WHERE ph_no = %a" #query for setting the associated phone number as NONE
                    y = cursor.execute(sql1, [ph]) #implementing the query by replacing the placeholder with the variable
                    con.commit() #commiting all changes to the db's tables
                    #following demarcates that the program has made changes to the table
                    if y == 1:
                        print("detail deleted")
                        print("rerun for multiple edits or to update")
                #logical block 1A(ii).3: logical deletion of email
                elif delete == "e":
                    e = int(input("confirm your email id")) ##taking number to associate the client's email in the db with it
                    sql1 = "delete from user_data SET email = NULL WHERE email = %a" #query for setting the associated email as NONE
                    y = cursor.execute(sql1, [e])#implementing the query by replacing the placeholder with the variable
                    con.commit()#commiting all changes to the db's tables
                    #following demarcates that the program has made changes to the table
                    if y == 1:
                        print("detail updated")
                        print("rerun for multiple edits or to update")
                #logical block 1A(ii).4: logical deletion of all the details associated to the client's account
                elif delete == "da": #this is th feature that allows user to delete the whole account
                    ph = int(input("confirm your phone number")) #confirming here is also important because all data will be erased
                    sql1 = "DELETE from user_data WHERE ph_no = %a" #creating a query that deletes all details of client's account by associating their phone number with it
                    y = cursor.execute(sql1, [ph])#implementing the query by replacing the placeholder with the variable
                    con.commit()#commiting all changes to the db's tables
                    #following demarcates that the program has made changes to the table
                    if y == 1:
                        print("detail updated")
                        print("rerun for multiple edits or to update")
#account does not exist. directed to the main page for a rerun of the program.
else:
    print("create an account today!")
    import __main__
    __main__


            
            

