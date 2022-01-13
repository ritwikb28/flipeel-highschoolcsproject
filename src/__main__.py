#importing pyfiglet library for font art using ASCII
import pyfiglet
#creating the text and saving it in result
result = pyfiglet.figlet_format("FLIPEEL")
print(result)
#welcome text marking begining of the program
print("##WELCOME TO FLIPEEL 2.0, We are so excited for you to see our fresh features!##")
fname = input("your name:") #taking the client's name
print("hello",fname)
import signin #importing self created sign in module of the same folder
signin #calling the module
#signin module termination. implementation of the next line
client_proceed = input("how can we serve you today? (account access/ tech market)"'\n') #taking client's choice of service
#conditional block 1: tech market service
if client_proceed == "tech market":
    print("Hi, we are so excited to serve you",fname,"\nplease note that FLIPEEL is still in developement\nthank you!")
    #note to client + taking input from client about the site they want to use
    client_webpage = input('Where do you want to shop today, tell us!\n(flipkart -f , snapdeal - s):\n')
    #conditonal block 1A: directs to flipkart web scarpping application
    if client_webpage == "f":
        import flipkart_side #importing and calling
        flipkart_side
        print("thank you for shopping with us")
    #conditional block 1B: direct to snapdeal web scrapping application
    if client_webpage == "s":
        import snapdeal_side #importing and calling
        snapdeal_side
        print("thank you for shopping with us")
#conditional block 2: accessing their accound for deleting or updating details
elif client_proceed == "account access":
    import account_access
    account_access
else:
    print("wrong proceed code, try again") #program did not interact properly. error raised.






