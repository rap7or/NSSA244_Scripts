#!/usr/bin/python3


#!/usr/bin/python3

#File: script2_OSiebert.py
#Author: Owen Siebert
#Description: Script for mananging Docker containers written in python3.6.7.
#             Provides several options for container managemet, including 
#             Create, ping, view parameters, view network type, show running  
#             containers, start, stop and remove.



import os
import subprocess


#Function: main
#Parameters: None
#Description: Main method, which contains the menu with container options.
#             Keeps taking in options untill user enters 'q'. Reads 
#             input and calles function based on menu item chosen.

def main():
    
    var = ''
    while(var != 'q'):
        print('                    ##         .')
        print('              ## ## ##        ==   ')
        print('           ## ## ## ## ##    ===')
        print('       /"""""""""""""""""\___/ ===')
        print('  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~')
        print('       \______ o           __/')
        print('         \    \         __/')
        print('          \____\_______/')
        print('\n|--------------------------------------|')
        print('|(a) : Create two containers             |')
        print('|(b) : Get a shell                       |')
        print('|(c) : Install net-tools and ping test   |')
        print('|(d) : Ping between containers           |')
        print('|(e) : View container parameters         |')
        print('|(f) : View vetwork connection type      |')
        print('|(g) : Show running containers           |')
        print('|(h) : Start container                   |')
        print('|(i) : Stop container                    |')
        print('|(j) : Remove containers                 |')
        print('|(q) : Quit                              |')
        print('|----------------------------------------|\n')

        var = input('Choose and option: ')
        var = var.lower()

        if var not in 'abcdefghijq':
            print('\nPlease choose a valid option\n')

        elif var == 'a':
            createContainers()

        elif var == 'b':
            cont = input('Enter a container name: ')
            getShell(cont)

        elif var == 'c':
            netTools()

        elif var == 'd':
            pingBetween()

        elif var == 'e':
            cont = input('Enter a container name: ')
            viewParametrs(cont)

        elif var == 'f':
            viewNetworks()

        elif var == 'g':
            showRun()
        
        elif var == 'h':
            cont = input('Enter a container name: ')
            start(cont)

        elif var == 'i':
            cont = input('Enter a container name: ')
            stop(cont)
        
        elif var == 'j':
            cont = input('Enter a container name: ')
            deleteContainer(cont)

#Function: createContainers
#Parameters: None
#Description: Creates 2 containers and backgrounds them with
#             the names siebert1 and siebert2
def createContainers():
    os.system('docker pull ubuntu:latest')
    os.system('docker run -d -i --name=siebert1 ubuntu:latest')
    os.system('docker run -d -i --name=siebert2 ubuntu:latest')


#Function: getShell
#Parameters: cont - container to get a shell on
#Description: Uses docker exec to give user shell on container cont 

def getShell(cont):
    os.system('docker exec -it ' + cont + ' bash')


#Function: netTools
#Parameters: None
#Description: Runs apt update and installs net-tools and the ping command
#             on both containers. It then runs the icommand and pareses
#             the output to get the ip of each container. It then pings
#             each from the host machine.

def netTools():
    os.system('docker exec -it siebert1 apt update')
    os.system('docker exec -it siebert1 apt install net-tools -y')
    os.system('docker exec -it siebert1 apt install iputils-ping -y')
    os.system('docker exec -it siebert2 apt update')
    os.system('docker exec -it siebert2 apt install net-tools -y')
    os.system('docker exec -it siebert2 apt install iputils-ping -y')
    
    cmd = 'docker exec -it siebert1 ifconfig |  grep inet'
    result = subprocess.check_output(cmd, shell=True)
    ip1 = str(result.strip().split()[1]).split("'")[1]

    cmd = 'docker exec -it siebert2 ifconfig |  grep inet'
    result = subprocess.check_output(cmd, shell=True)
    ip2 = str(result.strip().split()[1]).split("'")[1]


    os.system('\n\nping ' + ip1 + ' -c 1')
    os.system('\n\nping ' + ip2 + ' -c 1\n\n')

#Function: pingBetween
#Parameters: None
#Description: pings between the siebert1 and siebert2 containers.
#             Gets the ip of each container ans pings it from the 
#             opposite one. Catches error if net-tools isnt installed
def pingBetween():
    cmd = 'docker exec -it siebert1 ifconfig |  grep inet'
    try:
        result = subprocess.check_output(cmd, shell=True)
        ip1 = str(result.strip().split()[1]).split("'")[1]
        print('\n\nPinging siebert1 from siebert2')
        os.system('docker exec -it siebert2 ping ' + ip1 + ' -c 1')
    except:
        print('net-tools not installed please run option c')
        return 1


    cmd = 'docker exec -it siebert2 ifconfig |  grep inet'
    result = subprocess.check_output(cmd, shell=True)
    ip1 = str(result.strip().split()[1]).split("'")[1]
    print('\n\nPinging siebert2 from siebert1')
    os.system('docker exec -it siebert1 ping ' + ip1 + ' -c 1')

#Function: viewParameters
#Parameters: cont - container to inspect
#Description: Runs docker inspect command on container cont
def viewParametrs(cont):
    os.system('docker inspect ' + cont)

#Function: viewNetworks
#Parameters: None
#Description: Runs docker inspect and greps out network type
def viewNetworks():
    print('siebert1 network: ')
    os.system('docker container inspect siebert1 | grep -A 1 NetworkSettings')
    print('siebert2 network: ')
    os.system('docker container inspect siebert1 | grep -A 1 NetworkSettings')

#Function: showRun
#Parameters: None
#Description: Runs docker stats to show running containers and their usage
def showRun():
    os.system('docker stats --no-stream')
    print('\n')

#Function: start
#Parameters: cont - container to start
#Description: starts container cont
def start(cont):
    os.system('docker start ' + cont)

#Function: stop
#Parameters: cont - container to stop
#Description: stops container cont
def stop(cont):
    os.system('docker stop ' + cont)

#Function: deleteContainer
#Parameters: cont - container to delete
#Description: deletes container cont
def deleteContainer(cont):
    os.system('docker rm ' + cont)

if __name__ == "__main__":
    main()



#references
#https://docs.docker.com/engine/reference/commandline/docker/