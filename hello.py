import platform
import psutil

def sys_info():
    print(f"操作系统: {platform.system()}")
    print(f"内存总量: {round(psutil.virtual_memory().total / (1024.0 **3), 2)} GB")
    print(f"内存使用率: {psutil.virtual_memory().percent}%")
    print("Hello from OpenClaw AI Assistant!")

if __name__ == "__main__":
    sys_info()
    print('AI internal access active')
