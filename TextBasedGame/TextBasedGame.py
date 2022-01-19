import random
import time
import termcolor
import playsound
from pygame import mixer
import os

validInput = False
validInput1 = False
validInput2 = False
validInput3 = False
validInput4 = False
validInput5 = False
validInput6 = False
validInput7 = False
validInput8 = False
validInput9 = False
validInput10 = False
validInput11 = False
validInput12 = False
validInput13 = False
validInput14 = False
validInput15 = False
validInput16 = False
validInput17 = False
validInput18 = False
validInput19 = False
validInput20 = False
validInput21 = False
validInput22 = False
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0 
v = 0
w = 0
x = 0
y = 0
z = 0

mixer.init()
mixer.music.load("upbeat.mp3")

def city():

    return('''
      __                   ___                       
 |""|  ___    _   __  |"""|  __                   
 |""| |"""|  |"| |""| |"""| |""|        _._ _
 |""| |"""|  |"| |""| |"""| |""|       (__((_(
 |""| |"""|  |"| |""| |"""| |""|      \'-:--:-.
 "'\''"''"'""'"""''"'\'''"""'""'""'~~~~~~'-----'~~~~
    ''')

def bookAscii():

    return('''
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                    `---`
    ''')

def sushi():

    return('''
                                                     ██▓▓██▓▓▓▓                                                                      
                                                    ▓▓▓▓▓▓░░░░░░░░░░▓▓▓▓                                                                  
                                                ██████  ████████████░░░░████                                                              
                                      ▓▓▓▓▓▓▓▓▓▓██████▓▓░░░░░░▒▒  ░░▓▓▓▓██▒▒▓▓██                                                          
                              ████████░░░░    ░░██░░  ░░            ░░░░  ██░░░░████                                                      
                            ██              ░░██                            ██  ░░░░████                                                  
                          ▒▒░░░░░░░░░░░░░░░░▓▓░░        ░░░░░░░░░░░░    ██▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒                                              
                      ▓▓▓▓░░      ░░▒▒░░░░░░██          ▒▒▒▒░░░░░░██████░░░░░░░░░░░░██████░░████                                          
                  ████  ██        ▒▒▒▒░░  ██        ▒▒▒▒░░░░░░░░██                        ██░░░░████                                      
              ░░░░░░░░  ████░░    ▒▒▒▒    ██      ▒▒░░░░░░▒▒▒▒▓▓░░                        ░░▓▓░░▒▒░░▓▓▒▒                                  
        ▓▓▓▓░░░░░░░░    ██▓▓▓▓      ▒▒▒▒▒▒██      ▒▒    ░░░░██░░        ▒▒▒▒░░░░  ░░  ▓▓▓▓▓▓██▓▓▓▓░░░░░░▓▓▓▓                              
    ████  ▒▒░░  ▒▒▒▒▒▒  ██▓▓▓▓██████      ████    ▒▒        ██      ▒▒▒▒░░░░░░░░░░████            ████  ░░░░████                          
  ██      ▒▒░░  ▒▒▒▒▒▒  ██▓▓▒▒▒▒▓▓▓▓██████████      ▒▒▒▒    ██    ▒▒  ░░  ▒▒▒▒░░██                    ██    ░░░░████                      
  ██▓▓▓▓    ▒▒▒▒▒▒▒▒      ██▓▓▒▒▒▒▓▓▓▓▓▓▓▓██▓▓██            ██    ▒▒      ░░  ██          ▒▒▒▒          ██      ░░░░████                  
  ██    ▓▓▓▓                ██▒▒▒▒▓▓▓▓▓▓▓▓██▓▓▓▓██          ██    ▒▒      ░░▒▒██      ▒▒▒▒░░░░░░░░      ██        ░░░░░░████              
  ██░░░░    ▓▓▓▓              ████████▓▓▓▓▓▓██▓▓▒▒██████    ████    ▒▒▒▒  ░░██      ▒▒  ░░░░▒▒▒▒░░░░      ██            ░░░░████          
  ██░░░░░░░░░░░░▓▓▒▒          ░░░░░░░░████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓████    ░░    ░░██      ▒▒  ░░  ░░░░░░░░      ██            ░░░░░░░░▓▓▓▓      
  ██░░░░░░░░░░░░    ▓▓▓▓          ░░░░░░░░░░░░██▒▒▒▒▒▒▓▓▓▓▓▓██▓▓██      ░░  ██      ▒▒      ░░░░░░░░      ██                ░░░░░░░░████  
  ██░░░░░░░░░░░░░░░░    ▓▓▓▓              ░░░░░░██▒▒▓▓▓▓▓▓▓▓██▓▓▓▓██        ██        ▒▒▒▒░░░░▒▒▒▒        ██                        ░░░░██
  ██░░░░░░░░░░░░░░░░░░░░    ▓▓▓▓            ░░░░░░██████▓▓▓▓▓▓██▓▓▒▒██████  ████          ░░░░░░        ████                ░░    ░░▓▓▓▓██
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░░░  ░░░░░░░░░░░░████████▓▓▒▒▓▓▓▓▓▓▓▓████          ░░  ░░        ████                    ▓▓▓▓░░░░██
    ████░░░░░░░░░░░░░░░░░░░░░░░░    ▓▓▓▓          ░░░░░░░░░░░░░░██▒▒▒▒▒▒▓▓▓▓██▓▓██                    ██▓▓██                ▓▓▓▓░░░░▒▒▒▒██
        ████░░░░░░░░░░░░░░░░░░░░░░░░    ▓▓▓▓                  ░░░░██▒▒▒▒▓▓▓▓██▓▓▓▓████            ████▓▓▓▓██            ▓▓▓▓░░░░▒▒▒▒▒▒▒▒██
        ░░░░██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░░░░░██████▓▓▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒██
            ██▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░    ▓▓▓▓░░            ░░░░░░░░██████▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  ░░  ▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ██▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░    ▓▓▓▓                ░░░░░░░░██▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██    ▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ██░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓            ░░░░░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓████░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ██░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░  ▓▓▓▓              ░░░░░░░░████████████░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ██░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░    ▓▓▓▓  ░░            ░░░░░░░░░░░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████  
            ██░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████  ░░  
            ██░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░  ▓▓▓▓    ░░░░░░░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██        
            ████░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░░░    ▓▓▓▓    ▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██        
            ░░░░██▓▓░░░░░░░░░░░░░░░░▓▓▒▒▒▒████░░▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██░░        
                    ████░░░░░░░░░░░░▓▓████          ████▓▓▓▓░░░░░░░░░░░░░░░░░░░░  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒████            
                        ████░░░░░░████              ██▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒████                
                            ██████                  ██▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓████                    
                                                    ██░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓████                        
                                                    ██░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████                            
                                                    ██░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓  ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒████                                
                                                    ██░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓████                                    
                                                    ████░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                                        
                                                    ░░░░▓▓▓▓░░░░░░░░░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░                                        
                                                        ░░  ▓▓▓▓░░░░░░░░░░░░▓▓▓▓▓▓▓▓▒▒████                                                
                                                                ████░░░░░░░░▓▓▓▓▒▒████                                                    
                                                                  ░░▓▓▓▓░░░░▓▓▓▓██░░░░                                                    
                                                                        ██████                                                            
    
    ''')

def pizza():

    return('''
                                                                                                                                                          
                                                                                                                                                          
                                                            ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░                                                              
                                                    ░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░  ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░                                                      
                                              ░░░░░░░░▒▒▒▒▒▒░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▒▒                                                  
                                          ░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒                                              
                                      ░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░                                          
                                    ░░▒▒▓▓▓▓▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                      
                                  ▒▒░░░░░░▒▒▒▒░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░▒▒                                    
                              ░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒▒▒▓▓▓▓██▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▓▓████▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒                                  
                            ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓████▓▓▓▓▓▓▓▓░░░░░░░░  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒░░░░░░░░░░░░▒▒░░                              
                            ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░  ░░░░░░░░░░░░░░░░░░▒▒▒▒                            
                          ░░░░░░  ░░░░░░▒▒░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓░░  ░░░░░░░░░░░░░░░░▒▒░░░░░░                          
                      ░░░░░░░░░░░░░░▒▒▓▓░░▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░                        
                      ░░░░░░░░░░░░▒▒▓▓▒▒▒▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓░░░░░░  ▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒░░                      
                    ░░░░░░░░░░░░▒▒▒▒░░▒▒▓▓██▓▓▓▓▒▒░░░░▓▓▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒░░░░    ░░▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒░░░░░░                      
                  ░░░░░░░░░░░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░  ░░    ░░▒▒▓▓▓▓▒▒▓▓▒▒▓▓▒▒░░░░░░░░▒▒██▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒░░░░░░                    
                  ▒▒░░░░░░░░▒▒░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░  ░░░░▓▓▒▒▓▓▒▒░░  ░░░░░░  ░░░░░░▒▒▓▓▓▓▓▓▒▒░░  ░░░░░░▓▓▓▓▒▒▓▓██▓▓▒▒░░░░▒▒▒▒░░░░░░                    
                ░░░░░░░░░░▒▒▒▒░░░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░    ░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒░░▒▒                  
                ░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░▒▒▒▒▓▓██▓▓▓▓▓▓░░░░░░  ░░░░░░░░    ▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░▓▓░░░░░░                  
              ░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░  ░░░░░░░░  ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░▓▓                
              ░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓██████▓▓▓▓░░░░    ░░░░░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒  ░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░▒▒░░░░▒▒▒▒              
              ░░░░░░░░▒▒░░░░░░  ░░░░██▓▓▓▓██▓▓▓▓▓▓░░░░    ░░░░░░░░░░▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░░░░░░░▒▒▒▒▒▒░░▓▓              
            ▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░▓▓▒▒▓▓██░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓░░    ░░░░░░░░░░░░░░▓▓▓▓▒▒▓▓▒▒▓▓░░░░░░░░░░░░░░░░▒▒░░▒▒              
            ██░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓░░░░  ░░░░░░░░░░░░  ░░▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░            
            ▒▒░░░░░░▒▒░░░░▒▒▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓▒▒░░  ░░▒▒░░░░  ░░░░  ░░░░░░░░░░░░▒▒░░▒▒            
          ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓░░░░░░░░▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒░░▒▒            
          ░░░░░░░░▒▒░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░▒▒▒▒▓▓░░░░░░░░░░▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒░░░░░░          
          ▒▒░░░░░░▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▒▒░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░  ░░░░░░▓▓▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓    ░░░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒░░░░░░          
          ▒▒░░░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓░░░░░░░░▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒  ░░░░░░░░░░░░      ░░░░░░▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒  ░░░░░░▓▓▓▓▒▒▓▓▓▓░░▒▒░░░░░░░░░░░░░░          
          ▒▒░░░░▒▒▒▒░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██░░░░  ░░░░▒▒▒▒▒▒▓▓▓▓▒▒    ░░░░▓▓░░░░▒▒▒▒░░░░░░░░░░▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░▒▒          
          ▒▒░░░░▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░▒▒          
          ▒▒░░░░▒▒▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░  ░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒░░▒▒          
          ░░░░░░▒▒░░░░▒▒▒▒▓▓██▓▓▒▒▒▒░░░░▒▒░░░░░░▓▓▓▓▓▓░░      ░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ░░░░░░▒▒▓▓▓▓▓▓░░░░░░  ░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▒▒░░▒▒          
          ▒▒░░▒▒▒▒░░░░▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░▓▓██▓▓▓▓▓▓░░░░  ░░▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░  ░░░░░░░░░░░░░░░░    ░░░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░▓▓░░░░▒▒          
          ░░░░░░▒▒░░░░░░▒▒░░░░░░░░░░░░░░░░▒▒▓▓██████▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░░░░░░░░░░░░░▒▒▓▓▒▒▓▓░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒          
          ░░░░░░▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓░░░░░░░░▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ░░▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓░░░░░░░░  ░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░          
          ▒▒░░░░▒▒▒▒▒▒▓▓██▓▓▓▓▓▓██▓▓░░░░░░██▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░▒▒░░▒▒▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░▒▒          
          ▒▒░░░░▓▓▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒░░░░░░░░▒▒▒▒░░░░▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓░░    ░░░░░░░░░░  ░░░░░░▒▒▒▒░░▓▓          
          ▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▓▓▒▒░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░  ░░░░░░░░░░░░░░  ░░▒▒▒▒▒▒░░▒▒          
          ▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░    ░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░  ░░░░▒▒▓▓▒▒░░░░          
          ░░▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▓▓██▓▓▓▓▓▓▒▒░░░░░░░░  ░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒░░░░          
          ░░▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░░░░░▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░▓▓▓▓▓▓▓▓▒▒░░▓▓██▓▓▓▓▒▒░░░░░░░░▒▒▓▓▓▓▓▓▒▒░░░░          
            ▒▒░░▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▒▒░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░░░▒▒▒▒▒▒░░            
            ░░░░▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓██▒▒░░░░░░░░░░░░░░▒▒░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▓▓▓▓▒▒░░░░░░░░            
              ▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒░░░░░░▒▒▒▒▓▓▒▒▓▓▓▓▒▒▓▓▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░▓▓▒▒▓▓▒▒▓▓▓▓▓▓██▓▓░░░░▒▒▒▒▒▒░░░░▒▒            
              ▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓░░░░░░▓▓██▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▓▓▒▒░░░░░░            
                ░░░░▒▒▒▒░░░░░░░░▒▒░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒░░░░▒▒▓▓██▓▓▒▒▓▓░░▒▒▒▒░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▓▓▒▒░░░░░░              
                ░░░░░░▒▒▓▓░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░              
                ░░░░░░░░░░▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓░░░░░░▓▓▓▓██▓▓▓▓▒▒░░░░░░▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒██████▓▓▒▒░░░░░░▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░                
                  ▒▒░░░░░░▒▒▒▒▒▒░░▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓██░░▒▒░░░░▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓██████▓▓▓▓██░░░░░░▒▒▓▓██████▓▓▒▒▒▒▒▒░░░░░░░░░░                
                  ░░▒▒░░░░░░▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░▒▒░░  ░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░                  
                    ▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒░░░░▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒░░░░░░░░  ░░░░                    
                      ▓▓▒▒░░▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓░░░░▒▒░░▒▒▒▒░░░░▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒██▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒░░░░░░░░░░░░  ░░░░░░                    
                        ▓▓▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░▒▒░░░░░░                      
                        ░░▓▓▒▒░░░░░░▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░  ░░░░░░░░▒▒                        
                          ░░▓▓▒▒░░▒▒░░▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░  ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒░░░░░░░░░░░░▒▒░░▒▒                          
                            ░░▓▓▒▒░░░░░░░░▒▒▒▒▒▒▒▒░░░░  ░░░░░░░░░░▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░▓▓▓▓▓▓▒▒                            
                              ░░▓▓▒▒░░▒▒░░░░░░▒▒▓▓░░▒▒░░░░░░░░░░░░░░▓▓██▓▓▓▓██▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▓▓▒▒░░░░░░░░▒▒▒▒▒▒                              
                                  ▒▒▓▓▓▓░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░    ░░▒▒▓▓▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░                                
                                    ▒▒██▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░                                  
                                      ░░██▓▓▒▒░░░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░                                      
                                          ░░▓▓░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒░░░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░                                        
                                              ░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░    ░░░░▒▒▒▒▒▒                                              
                                                  ░░▓▓▒▒░░░░▒▒░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░                                                
                                                        ▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░                                                      
                                                                ░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░                                                                                                                                                                                                                                                                                                     
    ''')


def competition():
  
  return ('''
______________________________________
|                                     |
|     Sustainability Competition      |
|                                     |
|   Welcome to the sustainability     |
|   competition. The competition      |
|   won't be held very soon,          |
|   because you will be required      |
|   to complete 4 tasks before        |
|   you can participate. You will     |
|   be notified about these 4         |
|   tasks and how to complete         |
|   these. Once you are done          |
|   completing these, you will        |
|   be given details about the        |
|   competition.                      |
|                                     |
|    Go to Sustainability Center      |
|            to Sign Up               |
|_____________________________________|
  ''')

def subway():

  return('''
  
___________   _______________________________________^__
 ___   ___ |||  ___   ___   ___    ___ ___  |   __  ,----\
|   | |   |||| |   | |   | |   |  |   |   | |  |  | |_____\
|___| |___|||| |___| |___| |___|  | O | O | |  |  |        \
           |||                    |___|___| |  |__|         )
___________|||______________________________|______________/
           |||                                        /--------
-----------\'''---------------------------------------'
  ''')

def skyscraper():

  return('''
                    ||
                       WW
                      WWWW
                     WWWWWW
                    WWWWWWWW
                   WWWWWWWWWW
                 \|/||||||||\| /
               \ /|/||||||||\|\ /
              \ / |/||||||||\| \ /               
_______________/__|/||||||||\|__\_/______________
                 _*/wwwwwwww\*_
                | / \_______/ \|
                | \ \  |||  / /|
                |    | |||  |  |
                |  | |      | ||
  ''')

def airplane2():

  return('''
           _
         -=\`\\
     |\ ____\_\__
   -=\c`""""""" "`)
      `~~~~~/ /~~`
        -==/ /
          '-'
  ''')

def airplane3():
  return('''
                                    |
                                    |
                                    |
                                  .-'-.
                                 ' ___ '
                       ---------'  .-.  '---------
       _________________________'  '-'  '_________________________
        ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
                      \    /  ||/   H   \||  \    /
                       '--'   OO   O|O   OO   '--'

  ''')

def firework():
  return('''
                                 .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ''')

def clear():
  os.system('clear')

#ASCII art sites

#https://www.asciiart.eu/
#https://textart.sh/topic/sushi
#https://textart.sh/topic/subway

#Sound Sites
#https://pixabay.com/music/search/genre/upbeat/
#https://sounds-mp3.com/

#clear
#https://replit.com/talk/ask/How-do-I-make-my-text-in-Python-disappear-when-the-user-presses-a-key/43147



sCity = "Sustainable City."
printString = termcolor.colored(sCity, 'green')



while validInput == False:
    mixer.music.play()
    print("Hi. Welcome to ",printString,"")
    start1 = "Type in (start) to begin"
    while a < len(start1):
      print(start1[a], end="", flush=True)
      time.sleep(0.01)
      a += 1
    start = input(" >> ")
    mixer.music.stop()
    if "start" in start.lower():
      clear()
      mixer.music.load("city.mp3")
      mixer.music.play()
      print(city())
      print("Welcome to ",printString,"")
      begin1 = "In this game, you will be required to find the mysteries of one of the most technological advanced cities in the world. In this game, you need to complete a certain amount of tasks. You will win once you collect 4 points from doing tasks. In this game you will have to type something up when you see two arrows which looks like this '>>'. Most of the time, you will need to type in word(s) that are included in brackets which look like this '()'. Sometimes, the question may not provide you with words to type in, so you may have to type in what you think the answers should be. Good luck and I hope you enjoy your adventure! If you are ready, type in the word (begin)"
      while b < len(begin1):
        print(begin1[b], end="", flush=True)
        time.sleep(0.1)
        b += 1
      validInput = True
    else:
      print("That command doesn't work.\n")

while validInput1 == False:
    begin = input(" >> ")
    if "begin" in begin.lower():
        clear()
        print(city())
        print("Welcome to ",printString,"")
        welcome = "You are walking down the street, and you see a book store to your right. You enter the book store, and you notice that one of the best selling books is Happy Right Now. You read the book, and you understand that the three most important values being told are happiness, empathy, and gratitude. The store owner then tells you that these values are important values among people in the city. The owner also says that equity and inclusion are two important JEDI values you will also see around the city. You then decide to go explore the city more. Type (pizza shop) if you want to go get pizza, or type (sushi shop) if you want to get sushi\n"
        while c < len(welcome):
          print(welcome[c], end="", flush=True)
          time.sleep(0.01)
          c += 1
        print(bookAscii())
        validInput1 = True
        mixer.music.stop()
    else:
        print("That command doesn't work.")



while validInput2 == False:
    adventure = input(" >> ")
    if "sushi shop" in adventure.lower():
      clear()
      print(sushi())
      sShop = "\nWelcome to the sushi shop. Here, you try sushi for the first time and it ends up being the best\n thing you have ever tasted. While eating your sushi, you notice a piece of paper on the ground and\n you walk over to pick it up. The paper looks like this.\n"
      while d < len(sShop):
          print(sShop[d], end="", flush=True)
          time.sleep(0.01)
          d += 1
      print(competition())
      validInput2 = True
    elif "pizza shop" in adventure.lower():
      clear()
      print(pizza())
      pShop = "\nWelcome to the pizza shop. Here, you try pizza for the first time and it ends up being the best\n thing you have ever tasted. While eating your pizza, you notice a piece of paper on the ground and\n you walk over to pick it up. The paper looks like this.\n"
      while e < len(pShop):
          print(pShop[e], end="", flush=True)
          time.sleep(0.01)
          e += 1
      print(competition())
      validInput2 = True
    else: 
      print ("That command isn't valid.")

while validInput3 == False:
  goToS = "Type in (start) to go to the Sustainability Center"
  while f < len(goToS):
          print(goToS[f], end="", flush=True)
          time.sleep(0.01)
          f += 1
  sCenter = input(" >> ")
  if "start" in sCenter.lower():
    clear()
    sub = "\nYou now take the subway over to where the Sustainability Center is.\n"
    while g < len(sub):
      print(sub[g], end="", flush=True)
      time.sleep(0.01)
      g += 1
    print(subway())
    print(skyscraper())
    fDesk = ("You walk into the large building, and walk up to the front desk to request to participate in the competition. The person at the front desk signs you up, and tells you what the first task is.\n She says that the first task revolves around the word 'sustainability.' You will have to explore the city and try to find the meaning of this word. Type in (begin) to start working on task 1 ")
    while h < len(fDesk):
      print(fDesk[h], end="", flush=True)
      time.sleep(0.01)
      h += 1
    validInput3 = True
  else:
    print("That command doesn't work.")

while validInput4 == False:
  task1 = input(" >> ")
  if "begin" in task1.lower():
    clear()
    walkAround = "\nYou walk around the city deciding on where to go to work on the first task. Type in (library) to visit the library to find information, or (book store) to go back to the book store you were at earlier to find information for task 1"
    while i < len(walkAround):
      print(walkAround[i], end="", flush=True)
      time.sleep(0.01)
      i += 1
    validInput4 = True
  else: 
    print ("That command isn't valid.")

while validInput5 == False:
  information = input(" >> ")
  if "library" in information.lower():
    clear()
    print(bookAscii())
    lib = "\nWelcome to the library. When you enter the library, you are amazed by the size of the building and the amount of books that you see. You browse the shelves in the building, and you find yourself searching the section that has books on developing a sustainable city.\n You find two books, one called 'The Word Sustainability' and the second one called 'The Idea Behind a Sustainable City.' To read 'The Word Sustainability', type in (book 1), and to read 'The Idea Behind a Sustainable City', type in (book 2)"
    while j < len(lib):
      print(lib[j], end="", flush=True)
      time.sleep(0.01)
      j += 1
    validInput5 = True
  elif "book store" in information.lower():
    clear()
    print(bookAscii())
    bStore = "\nWelcome to the book store. When you enter the book store, you are amazed by the size of the building and the amount of books that you see. You browse the shelves in the building, and you find yourself searching the section that has books on developing a sustainable city.\n You find two books, one called 'The Word Sustainability' and the second one called 'The Idea Behind a Sustainable City.' To read 'The Word Sustainability', type in (book 1), and to read 'The Idea Behind a Sustainable City', type in (book 2)"
    while k < len(bStore):
      print(bStore[k], end="", flush=True)
      time.sleep(0.01)
      k += 1
    validInput5 = True
  else:
    print ("That command doesn't work.")

while validInput7 == False:
  bookStore = input(" >> ")
  if "book 1" in bookStore.lower():
    clear()
    print(bookAscii())
    open = "\nYou slowly open up the book to page 1 and you start reading. On page 1, the book says sustainability is 'the ability to maintain something at a certain rate or level.'\n"
    while l < len(open):
      print(open[l], end="", flush=True)
      time.sleep(0.01)
      l += 1
    validInput7 = True
  elif "book 2" in bookStore.lower():
    clear()
    print(bookAscii())
    open2 = "\nYou slowly open up the book to page 1 and you start reading. On page 1, the book says that sustainable cities are 'are inclusive, safe, and resilient.'\n"
    while m < len(open2):
      print(open2[m], end="", flush=True)
      time.sleep(0.01)
      m += 1
    validInput7 = True
  else:
    print ("That command isn't valid")
# Google Dictionary

#https://sdgs.un.org/goals/goal11

while validInput11 == False:
  task1complete = input("To complete task 1, type in one word that helps descirbe the meaning of the word 'sustainability' >> ")
  if "maintain" or "rate" or "level" or "inclusive" or "safe" or "resilient" in task1complete.lower():
    clear()
    comp1 = "Congrats! You have successfully completed task 1."
    comp1c = termcolor.colored(comp1, 'yellow')
    congrats1 = "\n You walk back to the Sustainability Center and tell the front desk that you have completed task 1. They tell you that the second task is to explore sustainable ways of transportation. To go to the train station for task 2, type in (train station). To go to the airport, type in (airport)\n"
    while n < len(congrats1):
      print(congrats1[n], end="", flush=True)
      time.sleep(0.01)
      n += 1
    validInput11 = True
  else:
    print ("Please try another word that better suits the defeniniton")

mixer.music.load("airplan.mp3")

while validInput12 == False:
  transportation = input(" >> ")
  if "airport" in transportation.lower():
    clear()
    mixer.music.play()
    air = "airport!"
    airp = termcolor.colored(air, 'blue')
    print(airplane2())
    print(airplane3())
    print("Welcome to the ",airp,"")
    airport1 = " At this airport, we have hundreds of flights that depart and land each day. At this airport, we use jet fuel called biofuel that doesn't have a bad impact on the environment like other jet fuels. This biofuel is better for our environment, and will help keep it sustainable. To complete task 2, type in a type of fuel that airplanes use that doesn't have a large negative impact on our environment"
    while o < len(airport1):
      print(airport1[o], end="", flush=True)
      time.sleep(0.01)
      o += 1
    validInput12 = True
    mixer.music.stop()
  elif "train station" in transportation.lower():
    clear()
    mixer.music.load("train.mp3")
    mixer.music.play()
    tStation = "Welcome to the train station! At this train station, we have many trains that come and go. At this train station, all trains are electrically powered and do not rely on substances that harm our environment. Electrically powered trains have a minimal impact on the environment compared to others. To complete task 2, type in a power source that has a minimal impact on the environment"
    while p < len(tStation):
      print(tStation[p], end="", flush=True)
      time.sleep(0.01)
      p += 1
    validInput12 = True
    mixer.music.stop()
  else:
    print("That command doesn't work.")

while validInput14 == False:
  task2complete = input(" >> ")
  if "biofuel" or "electric" in task2complete.lower():
    clear()
    T2com = "\nCongrats! You have successfully completed task 2. You typed in the correct answer. You walk back to the Sustainability Center to inform them that you have completed task 2. They tell that for task 3, you will have to explore sustainable food sources that help supply everyone in the city with food. To go tour around the city for sustainable food sources, type in the word (explore)\n"
    while q < len(T2com):
      print(T2com[q], end="", flush=True)
      time.sleep(0.01)
      q += 1
    validInput14 = True
  else:
    print ("Please try another word that better suits the defeniniton")

while validInput15 == False:
  task3 = input(" >> ")
  if "explore" in task3.lower():
    clear()
    exp = "\nWhile you walk out of the sustainability center, you notice that many people have gardens in the frontyard or backyard of their house, or the balcony of their apartment. You learn that this is effective as it is cheaper for people, and lessens the amount of fertilizer and pesticides being used. \nOne effective method used in the city for growing produce, is to create indoor farms. These indoor farms are effective for growing foods as the environment can be controlled, and it doesn't take up too much land as the building can be built vertically. Now since you have learned a lot about sustainable food sources, type in one or more words that describe sustainable food sources\n"
    while r < len(exp):
      print(exp[r], end="", flush=True)
      time.sleep(0.01)
      r += 1
    validInput15 = True
  else:
    print("That command doesn't work.")

while validInput16 == False:
  completeTask3 = input(" >> ")
  if "garden" or "fertilizer" or "pesticide" or "indoor" or "farms" or "control" in completeTask3.lower():
    clear()
    T3com = "Congrats on completing task 3. You are almost ready for the competition, just one more to go. For task 4, you job is to find ways you can protect and help your city. To explore the city to find ways to protect it, type in (park) if you want to go visit the park, or type in (city caves) to go visit the city's famous caves"
    while s < len(T3com):
      print(T3com[s], end="", flush=True)
      time.sleep(0.01)
      s += 1
    validInput16 = True
  else:
    print("Try another answer that better suits the question.")

while validInput17 == False:
    task4 = input(" >> ")
    if "park" in task4.lower():
      parc = "\nWelcome to the park. Sustainable city has many parks in the city as they are very helpful towards the environment. Parks provide a home for many plants and animals in the city and they are important to have in a city. They are nice places that people can go to during the day. You walk back to the Sustainability Center to go complete the final task. You then get asked your final question.\n Type in one or more words that helps describe ways to protect your city\n"
      while t < len(parc):
        print(parc[t], end="", flush=True)
        time.sleep(0.01)
        t += 1
      validInput17 = True
    elif "city caves" in task4.lower():
      caves = "\nWelcome to the city caves. These caves have been here for a very long time, but they have been protected during the building of this city. Preserving ancient sites like this is important as they have a ton of value in our world today. One important value is teaching us about our past. You walk back to the Sustainability Center to go complete the final task. You then get asked your final question.\n Type in one or more words that helps describe ways to protect your city"
      while u < len(caves):
        print(caves[u], end="", flush=True)
        time.sleep(0.01)
        u += 1
      validInput17 = True
    else:
      print("This command doesn't work")

while validInput18 == False:
  task4Complete = input(" >> ")
  if "park" or "preserve" or "protect" or "plants" or "animals" or "ancient" in task4Complete.lower():
    comFour = ("Congratulations! You have completed all 4 tasks. You are now ready for the big competition.\n They tell you that competition begins soon and that all you should no be ready.")
    while v < len(comFour):
        print(comFour[v], end="", flush=True)
        time.sleep(0.01)
        v += 1
    validInput18 = True
  else:
    print ("Sorry. That answer is not correct")

while validInput19 == False:
  weeks = "A few weeks later."
  while w < len(weeks):
        print(weeks[w], end="", flush=True)
        time.sleep(0.01)
        w += 1
  comp = "To compete in the competition using all the skills that you have just acquired, type in the word (competition) to compete in the Sustainability Competition"
  while x < len(comp):
    print(comp[x], end="", flush=True)
    time.sleep(0.01)
    x += 1
  compete = input(" >> ")
  if "competition" in compete.lower():
    competition1 = "To complete the Sustainability Competition, remind yourself of the book you read, Happy Right Now. One of the main things being taught in the book Happy Right Now is making good choices. Explain good choices that could impact your city positively. Explain using around 2 sentences. Also, feel free to write about your own design for a city."
    while y < len(competition1):
        print(competition1[y], end="", flush=True)
        time.sleep(0.01)
        y += 1
    validInput19 = True
  else:
    print("That isn't the correct answer.")    

mixer.music.load("fireworks.mp3")

while validInput20 == False:
  competitionReal = input(" >> ")
  if "maintain" or "preserve" or "environment" or "protect" or "plants" or "animals" or "transportation" or "park" or "garden" or "fertilizer" or "pesticide" or "indoor" or "farms" or "biofuel" or "electric" or "rate" or "level" or "inclusive" or "safe" or "resilient" in competitionReal.lower():
    mixer.music.play()
    print(firework())
    amaz = "Amazing work. You have won the competition. Good job a I hope you enjoyed playing this game."
    while z < len(amaz):
        print(amaz[z], end="", flush=True)
        time.sleep(0.01)
        z += 1
    validInput20 = True
    mixer.music.stop()
  else:
    print("Sorry, you didn't win the competition. Amazing work in everything else, and I hope you enjoyed playing this game. Feel free to try playing again.")
    validInput20 = True


#https://www.google.com/search?q=importance+of+world+heritage+sites&source=lmns&bih=660&biw=1420&rlz=1C5GCEM_enCA976CA976&hl=en&sa=X&ved=2ahUKEwi-8pOb36X1AhXBqnIEHSvuDDwQ_AUoAHoECAEQAA

#https://www.google.com/search?q=why+is+having+parks+in+cities+good&rlz=1C5GCEM_enCA976CA976&oq=why+is+having+parks+in+cities+good&aqs=chrome..69i57.6373j0j7&sourceid=chrome&ie=UTF-8

#https://sdgs.un.org/goals/goal11

#http://www.asciiworld.com/-Buildings,202-.html

#https://www.lifewire.com/how-to-connect-macbook-air-to-tv-4581209


