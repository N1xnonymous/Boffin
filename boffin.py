import time
import sys
from find import find

green="\u001b[32m"
Magenta="\033[95m"
yellow="\033[33m"
red="\033[31m"
cyan = '\033[36m' 

print(Magenta+"""

                    ██████╗░░█████╗░███████╗███████╗██╗███╗░░██╗
                    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║████╗░██║
                    ██████╦╝██║░░██║█████╗░░█████╗░░██║██╔██╗██║
                    ██╔══██╗██║░░██║██╔══╝░░██╔══╝░░██║██║╚████║
                    ██████╦╝╚█████╔╝██║░░░░░██║░░░░░██║██║░╚███║
                    ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝
    
    """)

print(cyan+"                                                        By : Team Shunux Space")
print(yellow+"  Input help to see all the options")

def boffin():
    inp=(input("Option-> "))
    elif(inp=='exit'):
        exit()
    elif(inp=='help'):
        print(green+"""Tools available
            In making, will update soon
            usage : type exit to stop
            """)
    else:
        print(red+"Hello Moto, Have a look at options by inputting "help".)
    while True:
        boffin()    
        
if __name__=="__main__":
   boffin()
