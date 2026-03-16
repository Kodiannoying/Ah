import os
import random
import time
import socket
# colors
RED = "\033[31m"
RESET = "\033[0m"
# main script

hn = socket.gethostname()
osinfo = os.name

# ah handler
os.system('clear')
print("Booting Ah.OS")
time.sleep(1)
print("welcome to ah use 'help' for help 'info' for os info support")
if osinfo == "nt":
    print("WARNING OS IS WINDOWS SOME COMMANDS WONT WORK")
else:
    print("OS is linux or macos all commands should work")

while True:
    cmd = input(f"{hn}-$ ")

    if cmd == "help":
        print("help: shows this list")
        print("clear: clears the terminal")
        print("exit: exits the terminal")
        print("ls: prints files in the current dir")
        print("mkdir: makes a dir e.g 'mkdir testdir'")
        print("echo: echos what you put after it")
        print("python: enters the python terminal")
        print("")

    elif cmd == "info":
        print("")
        print("WARNING")
        print("for commands that use os.system may not work like ls mkdir clear and others may not work,")
        print("this script was made and used in linux mainly Debian,")
        print("so this script may not work right on windows or non debian based linux distros,")
        print("without a terminal that supports mkdir ls clear and others some or most commands will fail")
        print("")

    elif cmd == "clear":
        os.system('clear')

    elif cmd == "exit":
        exit()

    elif cmd.startswith("echo"):
        print(cmd[5:])
    
    elif cmd.startswith("mkdir"):
        os.system(f"mkdir {cmd[5:]}")

    elif cmd == "bash":
        print("now in bash")
        os.system('bash')
        os.system('clear')
        print("exited bash")
    
    elif cmd == "ah":
        os.system('clear')
        print("welcome to ah use 'help' for help 'info' for os info support")
    
    elif cmd == "python":
        os.system('python3')
    
    elif cmd.startswith("ls"):
        os.system(f"ls {cmd[2:]}")
    
    elif cmd.startswith("!"):
        os.system(f"{cmd[1:]}")
    
    elif cmd == "":
        pass

    elif cmd.startswith("nano"):
        os.system(f"nano {cmd[4:]}")

    else:
        print(f"{RED}-ah not a command{RESET}")

