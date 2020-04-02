#made by Aanchal S at CUSAT 
import time
import serial

def send_data(data):                                      #function to send data to nodeMCU
    nl='\n'                                               #because we check for \n to end buffer in nodeMCU
    data=data+nl                                          #append it, yay python
    new_data=data.encode('utf-8')
    ser.write(new_data)
               
ser = serial.Serial(                                #initialize serial comms     
     port='/dev/ttyS0',
     baudrate = 9600,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.EIGHTBITS,
     timeout=1
 )
exit=0            #they are all flags
helpFlag=1
while exit==0:
    
    if (helpFlag==1):
        print('press h for help \n w$$$ for fwd speed were $ is natural number \n')
        print('a$$ or d$$ for direction with rate \n x for stop \n s$$$ for reverse')
        print('\n e for exit\n')
        helpFlag=0
    order=input()
    
    if((order[0]=='w' or order[0]=='a' or order[0]=='s' or order[0]=='d') and len(order)==1):     # for example   dont send w, send w0
        order+='0'
    if (order=='h'): #h for help
        helpFlag=1
    elif ((order[0]=='w'  or order[0]=='s') and len(order)<5):  #ws for movement
        i=1
        buff='0'
        while (i<len(order)):
            buff+=order[i]
            i+=1
        if(buff.isdigit):
            send_data(order)
    
    elif ((order[0]=='a' or order[0]=='d') and len(order)<4):
        i=1
        buff='0'
        while (i<len(order)):
            buff+=order[i]
            i+=1
        if(buff.isdigit):
            send_data(order)
    elif (order[0]=='x' and len(order)==1):
        send_data(order)
    elif (order=='e'):
        send_data('x')
        exit=1
    else:
        print('\n***lol no***\n')
        #helpFlag=1
