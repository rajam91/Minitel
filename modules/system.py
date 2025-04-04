import os 

def System_info():
    current_files = os.popen('ulimit -a').read() 
    print(f"\n: {current_files}")


    system_limit = os.popen('ulimit -sn').read() 
    print(f"\n: {system_limit}")


    strict_limit = os.popen('ulimit -Hn').read() 
    print(f"\n: {strict_limit}")