import sys
from modules.kernel import Kernel_info
from modules.network import Network_info
from modules.system import System_info
from modules.processus import identifierProcessus
import time

class bcolors:
    HEADER = '\033[95m'
    CRED    = '\33[31m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    CVIOLETBG = '\33[45m'
    CVIOLET = '\33[35m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CEND = '\033[44m'

def menu():
    ''' Main menu to choose an item '''
    
    chosen_element = 0

    #print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
    
    print (bcolors.OKCYAN +"#############################################################################"+ bcolors.ENDC)
    print (bcolors.OKCYAN +"########                                                             ########"+ bcolors.ENDC)
    print (bcolors.WARNING +"########                         Minitel                             ########"+ bcolors.ENDC)
    print (bcolors.OKCYAN +"######## ----------------------------------------------------------- ########"+ bcolors.ENDC)
    print (bcolors.WARNING +"########                 Welcome inside my Minitel                   ########"+ bcolors.ENDC)
    print (bcolors.OKCYAN +"######## ----------------------------------------------------------- ########"+ bcolors.ENDC)
    print (bcolors.OKCYAN + "########                                                             ########" + bcolors.ENDC)
    print (bcolors.WARNING + "########                    Choose an option:                        ########"+ bcolors.ENDC)
    print (bcolors.OKCYAN + "########                                                             ########"+ bcolors.ENDC)
    print (bcolors.WARNING +"########      1) General Information  |  2) Hardware Information     ########"+ bcolors.ENDC)
    print (bcolors.WARNING +"########      3) System limits        |  4) Installed packages       ########"+ bcolors.ENDC)
    print (bcolors.WARNING +"########                            5) Exit                          ########"+ bcolors.ENDC)
    print (bcolors.OKCYAN +"########                                                             ########"+ bcolors.ENDC)
    print (bcolors.OKCYAN +"#############################################################################"+ bcolors.ENDC)
    print(bcolors.OKCYAN +"Dédicasse à Ziad"+bcolors.ENDC)

    chosen_element = input(bcolors.CVIOLET + "Enter a number from 1 to 5: " + bcolors.CRED)
    
    if int(chosen_element) == 1:
        print(bcolors.CEND + 'General Information:'+bcolors.ENDC)
        Kernel_info()
        time.sleep(2)
        menu()
    elif int(chosen_element) == 2:
        print(bcolors.CEND +'Hardware Information:'+bcolors.ENDC)
        Network_info()
        time.sleep(2)
        menu()
    elif int(chosen_element) == 3:
        print(bcolors.CEND +'System limits:'+bcolors.ENDC)
        System_info()
        time.sleep(2)
        menu()
    elif int(chosen_element) == 4:
        print(bcolors.CEND +'Installed packages:'+bcolors.ENDC)
        identifierProcessus()
        time.sleep(2)
        menu()
    elif int(chosen_element) == 5:
        print(bcolors.CVIOLETBG + "Good Bye" + bcolors.CRED )
        sys.exit()
    else:
        print(bcolors.CRED + 'Sorry, the value entered must be a number from 1 to 5, then try again !' + bcolors.ENDC)

if __name__ == '__main__':
    ''' Python script main function '''
menu()


#https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal