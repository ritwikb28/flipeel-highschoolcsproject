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
#dict_catalogue
flipkart_d = {"hd":"https://www.flipkart.com/computers/storage/external-hard-disks/pr?sid=6bo,jdy,nl6&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_320f5d5b-e356-4399-b250-a20df85e8c47_1_372UD5BXDFYS_MC.YWIQ0U3Z3EPA&otracker=hp_rich_navigation_5_1.navigationCard.RICH_NAVIGATION_Electronics~Storage~ExternalHardDrive_YWIQ0U3Z3",
"fafl" : "https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/fully-automatic-top-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Fully%20Automatic%20Top%20Load?",
"satl" : "https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/semi-automatic-top-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Semi%20Automatic%20Top%20Load",
"fatl" : "https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/semi-automatic-top-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Semi%20Automatic%20Top%20Load",
"iac"  : "https://www.flipkart.com/air-conditioners/pr?sid=j9e,abm,c54&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.technology%255B%255D%3DInverter&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Inverter%20AC",
"sac"  : "https://www.flipkart.com/home-kitchen/home-appliances/air-conditioners/split~type/pr?sid=j9e,abm,c54&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Split%20ACs",
"wac"  : "https://www.flipkart.com/home-kitchen/home-appliances/air-conditioners/window~type/pr?sid=j9e%2Cabm%2Cc54&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Window%20ACs",
"sd"   : "https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/single-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Single%20Door",
"dd"   : "https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/double-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Double%20Door",
"td"   : "https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/triple-door~type/pr?sid=j9e,abm,hzg&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Triple%20door",
"sbs"  : "https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/pr?otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DSide%2Bby%2BSide&sid=j9e%2Fabm%2Fhzg&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Side%20by%20Side",
"cnv"  : "https://www.flipkart.com/search?p%5B%5D%5B%5D=facets.features%255B%255D%3DConvertible&sid=j9e%2Fabm%2Fhzg&otracker=CLP_filters&p%5B%5D=facets.features%255B%255D%3DConvertible&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Convertible"
}

#targetted URL


if client_product == "hd":
    my_url == dict.get["hd"]
if client_product == "fafl":
    my_url == dict.get["fafl"]
if client_product == "satl":
    my_url == dict.get["satl"]
if client_product == "fatl":
    my_url == dict.get["fatl"]
if client_product == "iac":
    my_url == dict.get["iac"]
if client_product == "sac":
    my_url == dict.get["sac"]
if client_product == "wac":
    my_url == dict.get["wac"]
if client_product == "sd":
    my_url == dict.get["sd"]
if client_product == "dd":
    my_url == dict.get["dd"]
if client_product == "td":
    my_url == dict.get["td"]
if client_product == "sbs":
    my_url == dict.get["sbs"]
if client_product == "cnv":
    my_url == dict.get["cnv"]

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








    


    

    
    



    

    
    



