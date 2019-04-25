#!/usr/bin/python3
import os

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
            pingBetweem()

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


def createContainers():
    os.system('docker pull ubuntu:latest')
    os.system('docker run -d -i --name=siebert1 ubuntu:latest')
    os.system('docker run -d -i --name=siebert2 ubuntu:latest')

def getShell(cont):
    os.system('docker exec -it ' + cont + ' bash')

def netTools():
    os.system('docker exec -it siebert1 apt update')
    os.system('docker exec -it siebert1 apt install net-tools -y')
    os.system('docker exec -it siebert1 apt install iputils-ping -y')
    os.system('docker exec -it siebert2 apt update')
    os.system('docker exec -it siebert2 apt install net-tools -y')
    os.system('docker exec -it siebert2 apt install iputils-ping -y')
    os.system('ping siebert1')
    os.system('ping siebert2')
def pingBetweem():
    pass

def viewParametrs(cont):
    pass

def viewNetworks():
    pass

def showRun():
    os.system('docker stats --no-stream')
    print('\n')

def start(cont):
    os.system('docker start ' + cont)

def stop(cont):
    os.system('docker stop ' + cont)

def deleteContainer(cont):
    os.system('docker rm ' + cont)

if __name__ == "__main__":
    main()