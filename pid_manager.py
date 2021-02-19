MIN_PID = 300
MAX_PID = 5000

def allocate_map():
    global pid_list
    pid_list = [0 for i in range(4700)]
    if (pid_list):
        return 1
    else:
        return -1

def allocate_pid():
    try:
        index = pid_list.index(0)
        pid_list[index] = 1
        return index + 300
    except ValueError:
        return -1

def release_pid(pid):
    try:
        int(pid)
        if (pid < MIN_PID):
            print("Cannot release a PID value less than 300")
        elif (pid > MAX_PID):
            print("Cannot release a PID value greater than 300")
        else:
            pid_list[pid - 300] = 0
            print("PID %d has been released" %pid)
    except ValueError:
        print("Please enter an integer value between 300 and 5000")
