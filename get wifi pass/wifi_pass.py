import subprocess
import socket
import requests



wifi_list=subprocess.getoutput("netsh wlan show profile").replace("All User Profile","").replace(":","").replace("-","").replace("Profiles on interface WiFi","").replace("Group policy profiles (read only)","").replace("<None>","").replace("User profiles"
,"")

lists=wifi_list.split()

f= open("passwords.txt","w+")



for i in lists:
    if "DLink" in i:
        i="D-Link"
    passwd=subprocess.getoutput("wifipassword "+i)
    
    if " is not found on the system." not in passwd:
        
        print(passwd)
        
        f.write(passwd + "\n")