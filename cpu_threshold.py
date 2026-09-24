import psutil


def cpu_threshold():
    cpu_thred=int(input("Enter the threshold you want to set"))
    cpu_current=int(psutil.cpu_percent(interval=1))
    print("current cpu usage is ",cpu_current)
    if cpu_current>cpu_thred:
        print("CPU usage is above the threshold, email sent to admin")
    else:        
        print("CPU usage is below the threshold")

cpu_threshold()
