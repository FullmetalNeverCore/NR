import random, string
import webbrowser
import time
import requests


print(""" 
 __   _ _______ _______  ______ _     _ __   _ __   _ _____ __   _  ______     
 | \  | |______    |    |_____/ |     | | \  | | \  |   |   | \  | |  ____     
 |  \_| |______    |    |    \_ |_____| |  \_| |  \_| __|__ |  \_| |_____|     
                                                                               
""")
print("ver 1.0")
time.sleep(0.1)
print("Created by NeverCore")

num = input("Enter amount of keys")

f=open("ncodes.txt","w+", encoding='utf-8')

for n in range(int(num)):
   ch = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   lnk = "https://discord.gift/" + ch
   f.write("{}\n".format(lnk))

f.close()

with open("ncodes.txt") as f:
    for line in f:
        api = line.strip("\n")
        print(api)
        link = "https://discordapp.com/api/v6/entitlements/gift-codes/" + api + "?with_application=false&with_subscription_plan=true"
        r = requests.get(link)
        if r.status_code == 200:
            print("This one is Valid:".format(line.strip("\n")))
            r = open("Valid ones.txt", "a", encoding='utf-8')
            r.write("{}\n".format(api))
            r.close()
            break
        else:
            print("Invalid:".format(line.strip("\n")))
        