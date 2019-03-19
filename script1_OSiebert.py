#!/usr/bin/python3
"""
File: script1_OSiebert.py
Author: Owen Siebert
Description: Script for mananging Virtual Box written in python3.
             Provides several options for VM managemet, including 
             start, stop, create, delete,  list settings, and list 
             available VMs.
"""


"""
Funtion: main
Parameters: None
Description: Main method, which contains the menu with VM options.
             Keeps taking in options untill user enters 'q'. Reads 
             input and calles function based on menu item chosen.
"""
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

        var = raw_input('Choose and option: ')
        var = var.lower()

        if var not in 'abcdefq':
            print('\nPlease choose a valid option\n')

        elif var is 'a':
            createVM()

        elif var is 'b':
            listVM()

        elif var is 'c':
            vm = raw_input('Enter a VM to start: ')
            startVM(vm)

        elif var is 'd':
            vm = raw_input('Enter a VM to stop: ')
            stopVM(vm)

        elif var is 'e':
            vm = raw_input('Enter a VM: ')
            listSettings(vm)

        elif var is 'f':
            vm = raw_input('Enter a VM to delete: ')
            deleteVM(vm)

"""
Function: createVM
Parameters: None
Descripton:
"""
def createVM():
    pass

"""
Function: listVM
Parameters: None
Descripton:
"""
def listVM():
    pass

"""
Function: startVm
Parameters: vm - Virtual machine to start
Descripton:
"""
def startVM(vm):
    pass

"""
Function: stopVM
Parameters: vm - Virtual machine to stop
Descripton:
"""
def stopVM(vm):
    pass

"""
Function: listSettings
Parameters: vm - Virtual machine to list settings for
Descripton:
"""
def listSettings(vm):
    pass

"""
Function: deleteVM
Parameters: vm - Virtual machine to delete 
Descripton:
"""
def deleteVM(vm):
    pass


if __name__ == "__main__":
    main()