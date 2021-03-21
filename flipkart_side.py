#importing web-scrapping tools via BS4
from os import name
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

import pywhatkit as kit

##flipkart side
client_product = input('product you want to shop today\n##section online\n##hard drive, service code = hd##:\n')

print('note:please include country code with your phonr number')

client_phno = input('phone number:\n')

print('top product from the webpage will be sent to', client_phno)

print('tell us your preferred time to receive message from FLIPEEL')

print('hour,minute(s) format')

h = int(input("hour:\n"))

m = int(input("minute(s):\n"))


#targetted URL
my_url = "https://www.flipkart.com/computers/storage/external-hard-disks/pr?sid=6bo,jdy,nl6&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_320f5d5b-e356-4399-b250-a20df85e8c47_1_372UD5BXDFYS_MC.YWIQ0U3Z3EPA&otracker=hp_rich_navigation_5_1.navigationCard.RICH_NAVIGATION_Electronics~Storage~ExternalHardDrive_YWIQ0U3Z3  "

#requesting extraction of data
uClient = uReq(my_url)

#reading website's data
page_html = uClient.read()

#closing request
uClient.close()

#parsing the extracted data
page_soup = soup(page_html, "html.parser")

#creating a container to store extracted data
containers = page_soup.findAll("div",{"class":"col col-7-12"})



#looping through data to find our targetted section of the html-web page
for container in containers:
    #using findAll parsing for our section(json)
    title_container = container.findAll("div",{"class":"_4rR01T"})
    #finding content via indexing the list created
    product_name = title_container[0].text
    #printing the titles extracted from the web page

    kit.sendwhatmsg(client_phno,"hello from FLIPEEL\nThank you for choosing us\nDont forget to recommend us!!\nwe recommend the following product according to your requirements:\n"+ product_name + "\nFLIPEEL@2020-21\ndeveloped by Jhanvi Agarwal and Ritwik Bhardwaj",h, m)








    


    

    
    



    

    
    



