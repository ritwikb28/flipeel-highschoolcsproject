import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

import pywhatkit as kit


client_product = input('product you want to shop today\n(section online\n##hard drive, service code = hd')

client_phno = int(input('phone number:\n'))

print('top product from the webpage will be sent to', client_phno)

print('tell us your preferred time to receive message from FLIPEEL')

print('hour,minute(s) format')

h = int(input("hour:\n"))

m = int(input("minute(s):\n"))



##snapdeal side
my_url = "https://www.snapdeal.com/products/computers-external-hard-drives?sort=plrty#bcrumbSearch:external%20hard%20disk|bcrumbLabelId:3032"





#requesting extraction of data
uClient = uReq(my_url)

#reading website's data
page_html = uClient.read()

#closing request
uClient.close()

#parsing the extracted data
page_soup = soup(page_html, "lxml")

#creating a container to store extracted data
containers = page_soup.findAll("div",{"class":"product-desc-rating"})




#looping through data to find our targetted section of the html-web page
for container in containers:
    #using findAll parsing for our section(json)
    title_container = container.findAll("p",{"class":"product-title"})
    #finding content via indexing the list created
    

    product_name = title_container[0].text
    
    kit.sendwhatmsg(client_phno,"hello from FLIPEEL\nThank you for choosing us\nDont forget to recommend us!!\nwe recommend the following product according to your requirements\n"+ product_name + "\nFLIPEEL@2020-21\ndeveloped by Jhanvi Agarwal and Ritwik Bhardwaj",h, m)
    
