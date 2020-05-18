import json
import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-i" , "--ipaddress", help="Enter IP Address To Recon")
args = parser.parse_args()
ip = args.ipaddress

print("")
print("IPRECON coded by : @whokilleddb ")
 
if (ip == None) :
   
    print("Type python3 iprecon.py -h for help ")
    print("")
    print("https://github.com/whokilleddb/iprecon ")
    sys.exit(0)
url = "http://ip-api.com/json/" + str(ip)
response = requests.get(url)
data = json.loads(response.content)

if data['status'] == 'success' :
    print("\t[+] IP \t\t\t : " , data['query'])
    print("\t[+] STATUS \t\t : " , str(data['status']).upper())
    print("\t[+] COUNTRY \t\t : " , data['country'])
    print("\t[+] COUNTRY CODE \t : " , data['countryCode'])
    print("\t[+] REGION \t\t : " , data['region'])
    print("\t[+] REGION NAME \t : " , data['regionName'])
    print("\t[+] CITY \t\t : " , data['city'])
    
    print("\t[+] ZIP CODE \t\t : " , data['zip'])
    print("\t[+] LATITUDE \t\t : " , data['lat'])
    print("\t[+] LONGITUDE \t\t : " , data['lon'])
    print("\t[+] TIMEZONE \t\t : " , data['timezone'])
    print("\t[+] ISP \t\t : " , data['isp'])
    print("\t[+] CITY \t\t : " , data['city'])    
    
    
if data['status'] == 'fail' :
    print("\t[+] IP \t\t\t : " , data['query'])
    print("\t[+] STATUS \t\t : " , str(data['status']).upper())
    print("\t[+] MESSAGE \t\t : " , data['message'])
    

print("")
