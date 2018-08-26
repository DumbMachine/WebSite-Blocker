import time
from datetime import datetime as dt

hosts_path="Your HOSTS file path here"# C:\Windows\System32\drivers\etc\hosts is the default location for HOSTS file.
redirect="127.0.0.1"
website_list =["www.facebook.com"]#Enter the URL of the sites to be blocked


print("Enter the site name you want to b(Only name will do):   ")
x = str(input())
if 'www.' and '.com' not in x:
    website_list.append("www."+str(input()+".com"))
elif 'www.' or '.com' not in x:
    print("The url provided doesnt include either 'www.' or '.com'")
else:
    website_list.append(x)

print("Now enter the time you want the Site to be BLOCKED from(24 hour format) : ")
x = int(input)
print("Now enter the time you want the Site to be BLOCKED to(24 hour format) : ")
y = int(input)
while 1:
    if dt(dt.now().year,dt.now().month,dt.now().day,x) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,y):#hour
        f = open("hosts_path", "r+")
        f.seek(0)
        for i in f.readlines():
            if website in i:
                pass
            else:
                file.write(redirect +' '+ website + "\n")
    else:
        f = open(hosts_path,"r+")
        content = f.readlines()
        file.seek(0)
        for i in f.readlines():
            if not any(website in i for website in website_list):
                file.write(line)    #writes everything except the '127.0.0.1 www.sitename.com' part
        file.truncate()       #deletes the reamaining items
time.sleep(60)

