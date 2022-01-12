from re import search
import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

if con.is_connected() == False:
    print("error")

cursor = con.cursor()
forward = input("sign in (I)/ sign up(U)")
if forward == "I":
    name = input("name:")
    sinput = input('''sign in using
    phone number (ph)
    email_id (ei)''')
    if sinput == "ph":
        ph = int(input("phone number:"))
        sql1 = "select name from user_data where ph_no = %a"
        y = cursor.execute(sql1,ph)
        con.commit()
        if y == name:
            print("welcome to flipeel", y)
            print("reverting to main page")
        else:
            print("Invalid credentials. Log in failed.")

    elif sinput == "ei":
        ei = int(input("email id:"))
        sql1 = "select name from user_data where email = %a"
        y = cursor.execute(sql1,ei)
        con.commit()
        if y == name:
            print("welcome to flipeel", y)
            print("reverting to main page")
        else:
            print("Inalid credentials. Log in failed.")

    else:
        print("unidentified error: sorry for inconvinience")
elif forward == "U":
    import server_side
    server_side
else:
    print("We are not able to log in you this moment:(")