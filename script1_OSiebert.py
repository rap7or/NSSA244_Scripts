#!/usr/bin/python3

#File: script1_OSiebert.py
#Author: Owen Siebert
#Description: Script for mananging Virtual Box written in python3.
#             Provides several options for VM managemet, including 
#             start, stop, create, delete, list settings, and list 
#             available VMs.


import os

#Function: main
#Parameters: None
#Description: Main method, which contains the menu with VM options.
#             Keeps taking in options untill user enters 'q'. Reads 
#             input and calles function based on menu item chosen.

def main():
    var = ''
    while(var != 'q'):
        print('\n|-----------------------|')
        print('|(a) : Create a VM      |')
        print('|(b) : List all VMs     |')
        print('|(c) : Start a VM       |')
        print('|(d) : Stop a VM        |')
        print('|(e) : List VM Settings |')
        print('|(f) : Delete a VM      |')
        print('|(q) : Quit             |')
        print('|-----------------------|\n')

        var = input('Choose and option: ')
        var = var.lower()

        if var not in 'abcdefq':
            print('\nPlease choose a valid option\n')

        elif var == 'a':
            createVM()

        elif var == 'b':
            listVM()

        elif var == 'c':
            vm = input('Enter a VM to start: ')
            startVM(vm)

        elif var == 'd':
            vm = input('Enter a VM to stop: ')
            stopVM(vm)

        elif var == 'e':
            vm = input('Enter a VM: ')
            listSettings(vm)

        elif var == 'f':
            vm = input('Enter a VM to delete: ')
            deleteVM(vm)


#Function: createVM
#Parameters: None
#Descripton: Prompts user for a vm name, os type, path to an ISO
#            and how much memory to allocate, and used that to 
#            create a vm.

def createVM():
    name = input('Enter a vm name: ') 
    OS = input('Enter an  OS type: ')
    iso = input('Enter an ISO path: ')
    mem = input("Enter memory size to allocate (bytes): ")
    os.system('vboxmanage createvm --name ' + name + ' --ostype ' + OS + ' --register')
    os.system('vboxmanage storagectl ' + name + ' --name IDE --add ide')
    os.system('vboxmanage modifyvm ' + name + ' --memory ' + mem)
    os.system('vboxmanage storageattach ' + name + ' --storagectl IDE --port 0 --device 0 --type dvddrive --medium ' + iso)



#Function: listVM
#Parameters: None
#Descripton: Lists All vm's in virtualbox

def listVM():
    var = input('Detailed list? [y/n]: ')
    while var not in 'yn':
        var = input("Please enter [y/n]: ")
    if var == 'y':
        os.system('vboxmanage list vms --long')
    if var == 'n':
        os.system('vboxmanage list vms')



#Function: startVm
#Parameters: vm - Virtual machine to start
#Descripton: Startes Virtual Machine based on vm parameter

def startVM(vm):
    os.system('vboxmanage startvm ' + vm)



#Function: stopVM
#Parameters: vm - Virtual machine to stop
#Descripton: Stops Virtual Machine based on vm parameter

def stopVM(vm):
    os.system('vboxmanage controlvm ' + vm + ' poweroff soft')



#Function: listSettings
#Parameters: vm - Virtual machine to list settings for
#Descripton: Shows vm info based on vm parameter 

def listSettings(vm):
    os.system('vboxmanage showvminfo ' + vm)



#Function: deleteVM
#Parameters: vm - Virtual machine to delete 
#Descripton: Delets VM based on vm parameter

def deleteVM(vm):
    os.system('vboxmanage unregistervm ' + vm + ' --delete')

if __name__ == "__main__":
    main()