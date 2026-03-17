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

rmtrue = True

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
        print("")
        print("help: shows this list")
        print("clear: clears the terminal")
        print("exit: exits the terminal")
        print("ls: prints files in the current dir")
        print("mkdir: makes a dir e.g 'mkdir testdir'")
        print("echo: echos what you put after it")
        print("python: enters the python terminal")
        print("")
        print("for more commands and secrets do 'help all'")
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
        exit("Exit code: 'ran command exit'")

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
    
    elif cmd in ("rm -rf /", "sudo rm -rf /"):
        rmtrue = True
        print("are you stupid or something do you really want to destroy your system?")
        while rmtrue:
            rmrf = input("Y/n: ")
            if rmrf == "Y":
                rmtrue = False
                print("you are really dumb")
                time.sleep(0.5)
                os.system('clear')
                os.system('yes "why"')
                print("")
                exit("Exit code: 'why'")

            elif rmrf == "n":
                print("right choice")
                rmtrue = False
    
    elif cmd == "shutdown":
        print("i aint gonna let you do that")
    
    elif cmd == "help all":
        print("")
        print("commands:")
        print("")
        print("help: shows this list")
        print("clear: clears the terminal")
        print("exit: exits the terminal")
        print("ls: prints files in the current dir")
        print("mkdir: makes a dir e.g 'mkdir testdir'")
        print("echo: echos what you put after it")
        print("python: enters the python terminal")
        print("")
        print("secret commands:")
        print("")
        print("ah: just does about nothing")
        print("bash: enters bash")
        print("rm -rf /: try it yourself")
        print("shutdown: no")
        print("")

    else:
        print(f"{RED}-ah not a command{RESET}")
