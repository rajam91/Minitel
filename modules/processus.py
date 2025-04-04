import os

#information concernant le processus 
def identifierProcessus():

    process = os.popen('ps').read()
    cmd = os.popen('ip address show').read() #l'adress ip de toutes les interface
    link = os.popen('ip link show').read() #adress mac des interfaces(ethernet)

    print('Voici des infos sur le processus:')
    print('module name:', __name__)
    print('PID :', os.getpid())
    print('PPID :', os.getppid())
    print('\nProcessus :',process)
    print(cmd)
    print(link)


#shutdown immédiate sur mac avec la commande "sudo shutdown -h now"

#shutdown = os.popen('sudo shutdown -h now').read() # avec cette commande on peut définir le shutdown
#halt = os.popen('sudo halt').read() #shutdown de manière instantanée

