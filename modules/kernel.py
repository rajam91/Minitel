import os
import platform
import psutil #information about the CPU
import GPUtil #information about the GPU

def Kernel_info():
    # Sur macOS 
    print(platform.system()) #renvoie le nom du système d'exploitation 
    print(platform.release()) #renvoie la version du système d'exploitation
    print(os.name)

#on obtient la version du kernel avec la commande uname -a

    kernel_version = os.popen('uname -a').read() 
    print(f"Kernel: {kernel_version}")

    cpu_info = platform.processor()
    cpu_count = psutil.cpu_count(logical=False)
    logical_cpu_count = psutil.cpu_count(logical=True)

    print("\nCPU Information:")
    print(f"Processor: {cpu_info}")
    print(f"Physical Cores: {cpu_count}")
    print(f"Logical Cores: {logical_cpu_count}")

    memory_info = psutil.virtual_memory()

    print("\nMemory Information:")
    print(f"Total Memory: {memory_info.total} bytes")
    print(f"Available Memory: {memory_info.available} bytes")
    print(f"Used Memory: {memory_info.used} bytes")
    print(f"Memory Utilization: {memory_info.percent}%")

    disk_info = psutil.disk_usage('/')

    print("\nDisk Information:")
    print(f"Total Disk Space: {disk_info.total} bytes")
    print(f"Used Disk Space: {disk_info.used} bytes")
    print(f"Free Disk Space: {disk_info.free} bytes")
    print(f"Disk Space Utilization: {disk_info.percent}%")

#GPU ID, name, driver version, 
#total memory, free memory, used memory, GPU load, and temperature.

    gpus = GPUtil.getGPUs()

    if not gpus:
        print("No GPU detected.")
    else:
        for i, gpu in enumerate(gpus):
            print(f"\nGPU {i + 1} Information:")
            print(f"ID: {gpu.id}")
            print(f"Name: {gpu.name}")
            print(f"Driver: {gpu.driver}")
            print(f"GPU Memory Total: {gpu.memoryTotal} MB")
            print(f"GPU Memory Free: {gpu.memoryFree} MB")
            print(f"GPU Memory Used: {gpu.memoryUsed} MB")
            print(f"GPU Load: {gpu.load * 100}%")
            print(f"GPU Temperature: {gpu.temperature}°C")
