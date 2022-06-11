#! usr/bin/env python
import subprocess
from randmac import RandMac
from get_nic import getnic
import os

def generate_mac(): #random mac address generator
    example_mac = "00:00:00:00:00:00"
    generated_mac = RandMac(example_mac, True)
    return str(generated_mac)

def menu():
    interfaces = getnic.interfaces() # print available  interfaces
    while True:
        for i in range(len(interfaces)):  # print available interfaces
            print(str(i) + ")", interfaces[i], "\n")
        try:
            menu = int(input("choose network interface:\t"))
            if menu<0 or menu>len(interfaces)-1:
                print ("wrong entry")
            else:
                print("\t \t \t", interfaces[menu])
                nic = getnic.ipaddr(interfaces)  # generates dictionary with nics info
                nic = nic.get(interfaces[menu])  # exporting user choosed nic info to a dictionarie
                print(interfaces[menu], "Mac Address:" , nic.get('HWaddr'))
                for key, value in nic.items():  # printing nic info line by line
                    print(key, ' : ', value)
                change_mac_address=input("do you wish to change mac address? Y/N" )
                change_mac_address=change_mac_address.capitalize()
                if change_mac_address == "Y":
                    subprocess.call("ifconfig "+interfaces[menu]+" down", shell=True)
                    subprocess.call("ifconfig "+interfaces[menu]+" hw ether "+generate_mac(), shell=True)
                    subprocess.call("ifconfig "+interfaces[menu]+" up", shell=True)
                    nic = getnic.ipaddr(interfaces)  # generates dictionarie with nics info
                    nic = nic.get(interfaces[menu])  # exporting user choosed nic info to a dictionarie
                    print ("New Mac Address:",nic.get('HWaddr'))
                    print (subprocess.call("ifconfig", shell=True))
                    exit=input("do you wish to exit; Y/N\t").capitalize()
                    os.system('clear') # clear screen
                    if exit=="Y":
                        break
                    if exit!="N":
                        print("wrong option")
        except ValueError:
            print ("wrong option")

menu()

