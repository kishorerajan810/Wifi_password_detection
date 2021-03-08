#Import Subprocess Module
#Now we will store the profiles data in"data" variable by running the 1st cmd command using subprocess and check it out.

import subprocess

data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('/n')

#Now we will store the profile by coverting them to list.
profiles=[i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

#Using for loop in python we are checking and printing the wifi passwords if they are available using the 2nd cmd command.
for i in profiles:
    results=subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8').split('/n')
    results=[b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:30}| {:<}".format(i,results[0]))
    except IndexError:
        print("{:30}| {:<}".format(i,""))

#Printing the profiles[wifi names] with their passwords using try and except method.