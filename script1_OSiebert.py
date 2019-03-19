#!/usr/bin/python3

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
def createVM():
    pass

def listVM():
    pass

def startVM(vm):
    pass

def stopVM(vm):
    pass

def listSettings(vm):
    pass

def deleteVM(vm):
    pass


if __name__ == "__main__":
    main()