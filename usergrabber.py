import ctypes
import PySimpleGUI as sg
sg.theme('DarkAmber')
import os
import time
ctypes.windll.kernel32.SetConsoleTitleW("Roblox Account Grabber")
layout = [  [sg.Text('***Warning***')],
            [sg.Text('Please change the directories in the codes (bottom line)')],
            [sg.Button('Continue')] ]
window = sg.Window('Warning', layout)
event, values = window.read()
if event == 'Continue' or event == sg.WIN_CLOSED:
    window.close()
    sg.popup('Roblox account grabber\nMad by cetinofflegend (github.com/cetinofflegend)')
#print("***Warning!***\nChange the directories (bottom codes)")
time.sleep(0.5)
#print("Roblox User:Pass grabber (2010 spam acc)")
#print("***Author***\n@cetinofflegend")
#print("Visit github: https://github.com/cetinofflegend")
#print("I will release a documentation on how to get the program working for your device")
layout = [  [sg.Text('Please enter how many account you want to generate')],
            [sg.Text('Amount:'), sg.InputText(key="amount")],
            [sg.Text('Start ID:'), sg.InputText(key="id")],
            [sg.Text('Filename to save:'), sg.InputText(key="save")],
            [sg.Text('Include password? (y or n)'), sg.InputText(key="ips")],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('Roblox Account Grabber', layout)
while True:
    event, values = window.read()
    if event == 'Ok':
        window.close()
        text_input = values["amount"]
        idss = values["id"]
        filename = values["save"]
        ip = values["ips"]
        #layout = [  [sg.Text('Config:')],
         #   [sg.Text('Amount:'), text_input],
          #  [sg.Text('Start ID:'), idss],
           # [sg.Text('Filename to save:'), filename],
            #[sg.Button('Ok'), sg.Button('Cancel')] ]
        #window = sg.Window("Config", layout)
        sg.popup("Amount :"+text_input+"\nID :"+idss+"\nFilename: "+filename+"\nInclude Password: "+values["ips"]+"\nMade by @cetinofflegend       _",title="Config")
        gen = int(text_input)
        gen2 = int(idss)
    elif event == sg.WIN_CLOSED or event == 'Cancel':
        break
        gen = 100
        gen2 = 12786543
        filename ="roblox"
        
#layout = [  [sg.Text('Please enter start ID')],
  #          [sg.Text('ID:'), sg.InputText()],
   #         [sg.Button('Ok'), sg.Button('Cancel')] ]
#window = sg.Window('Roblox Account Grabber', layout)
#event, values = window.read()
#if event == 'Ok':
  #  text_input = values[0]
 #   sg.popup('Start ID is set to:', text_input)
 #   gen2 = text_input
#    window.close()
#elif event == sg.WIN_CLOSED or event == 'Cancel':
 #   sg.popup('ID is set to 12700001 by default')
 ##   gen2 = 12700001
   # window.close()
    
    
time.sleep(0.3)
import asyncio
from roblox import Client
from roblox.utilities.exceptions import UserNotFound
from roblox.utilities.exceptions import TooManyRequests
client = Client()
acc = []

    #gen = int(input("How many accounts do you want to pull: "))
    #print("Amount of accounts that will be generated: "+str(gen))

    #print("Amount of account that will be generated is set to 100 as default. Please eneter a valid integer value next time!")
    #gen = 100

    #gen2 = int(input("Start ID (12100000 - 12800000): "))
    #print("ID is set to: "+str(gen2))

    #print("ID is set to 12745632 as dedault. Please enter a valid integer value next time!")
    #gen2 = 12745632
#layout = [  [sg.Text('Include password?')],
      #      [sg.Button('Yes'), sg.Button('No')] ]
#window = sg.Window('Pass Config', layout)
#event, values = window.read()
#if event == 'Yes':
#    window.close()
#    sg.popup('Include password is set to true',title="false")
#    ip = "y"
    
#elif event == sg.WIN_CLOSED or event == 'No':
 #   window.close()
 #   sg.popup('Include password is set to false',title="false")
  #  ip = "n"
#sg.popup("Now starting to generate accounts!",title="Start")
    
#ip = input("Include pass?(y or n): ")
#if ip == "y" or ip == "Y":
 #   print("Include password set to: true")
#if ip == "n" or ip == "N":
 #   print("Include password set to: false")
#else:
 #   ip = "y"
##layout = [  [sg.Text('Please enter filename to save accs')],
            #[sg.Text('Filename:'), sg.InputText()],
         #   [sg.Button('Ok'), sg.Button('Cancel')] ]
#window = sg.Window('Roblox Account Grabber', layout)
#event, values = window.read()
#if event == 'Ok':
   # text_input = values[0]
    #sg.popup('Filename is set to:', savefile1)
    #window.close()
#elif event == sg.WIN_CLOSED or event == 'Cancel':

    #sg.popup('Filename is set to roblox.txt by default')
    #filename = "roblox"
    #window.close()
#filename = #str(input("File Name to save accounts: "))
async def main():
    a=0
    i=0
    idid = int(gen2)
    while i!= int(gen):
        i += 1
        
        try:
            user = await client.get_user(idid)
            if ip == "y" or ip == "Y":
                print(user.name+":l0l0l0l")
                acc.append(user.name +":l0l0l0l")
            elif ip == "n" or ip == "N":
                print(user.name)
                acc.append(user.name)
        except UserNotFound:
            print("Invalid ID")
        except TooManyRequests:
            print("Too many requests, Trying again in 1.5 seconds")
            time.sleep(1.5)
        idid += 1
        a+= 1
    sg.popup(str(gen) +" accounts generated!")
    sg.popup("Writing all accounts to a file...")
    try:
        with open("C:/Users/adalw/Desktop/usergrabber-main/accounts/" +filename+".txt", 'w') as f:
            for line in acc:
                f.write(line)
                f.write('\n')
    except FileNotFoundError:
        sg.popup('Creating account folder')
        time.sleep(0.2)
        sg.popup('Writing all accounts to a file')
        time.sleep(0.3)
        with open("C:/Users/adalw/Desktop/usergrabber-main/accounts/" +filename+".txt", 'w') as f:
            for line in acc:
                f.write(line)
                f.write('\n')
        os.mkdir("C:/Users/adalw/Desktop/usergrabber-main/accounts")
    sg.popup('Writing done')
    sg.popup('Writing last id to a file (lastid.txt)')
    with open("lastid.txt", 'w') as f:
        f.write(str(idid))
    sg.popup('Writing done (lastid.txt)')
    sg.popup('Closing in 3 seconds')
    time.sleep(3)
    
        


asyncio.get_event_loop().run_until_complete(main())
