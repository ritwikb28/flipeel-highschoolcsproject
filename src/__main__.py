import server_side
import flipkart_side
import snapdeal_side
import account_access
print("##WELCOME TO FLIPEEL 2.0, We are so excited for you to see our fresh features!##")
client_proceed = input("how can we serve you today? (account access/ tech market/ about us ")
if client_proceed == "tech market":
    print('please fill in the required details so that we are able to serve you better')
    stdinp = input("Do you accept our terms and confitions? (Y/N")
    if stdinp == "Y":
        server_side()
        print("Hi, we are so excited to serve you",server_side.name,"\n please note that FLIPEEL is still in developement\nthank you!")
        client_webpage = input('Where do you want to shop today, tell us!\n(flipkart -f , snapdeal - s):\n')

        if client_webpage == "f":
            flipkart_side()

        if client_webpage == "s":
            snapdeal_side()
    else:
        print("To access our services, accepting conditions and policy is mandatory:/")
elif client_proceed == "account access":
    account_access()
elif client_proceed == "about us":
    print("in dev")






