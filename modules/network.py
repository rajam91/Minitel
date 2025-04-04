import os


def Network_info():
    # information réseau   
    #la commande pour récupérer une adress IP dans le terminal : ipconfig getifaddr en0
    ip_adress = os.popen('ipconfig getifaddr en0').read() 
    print(f"\nIP: {ip_adress}")

    interface = os.popen('ifconfig').read() 
    print(f"interface: {interface}")

    routes = os.popen('netstat -rn').read()
    print(f"routes: {routes}")

