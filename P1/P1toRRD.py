#
# DSMR P1 uitlezer

import sys
import serial
import subprocess
import re
import os


################
#Error display #
################
def show_error():
    ft = sys.exc_info()[0]
    fv = sys.exc_info()[1]
    print("Fout type: %s" % ft )
    print("Fout waarde: %s" % fv )
    return


################################################################################################################################################
#Main program
################################################################################################################################################
print ("Control-C om te stoppen")

#Set COM port config
ser = serial.Serial()
ser.baudrate = 115200
ser.bytesize=serial.EIGHTBITS
ser.parity=serial.PARITY_NONE
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/ttyUSB0"




#Open COM port
try:
    ser.open()
except:
    sys.exit ("Fout bij het openen van %s. Programma afgebroken."  % ser.name)      


#Initialize
# stack is mijn list met de 26 regeltjes.
p1_teller=0
stack=[]

while p1_teller < 26:
    p1_line=''
#Read 1 line
    try:
        p1_raw = ser.readline()
    except:
        sys.exit ("Seriele poort %s kan niet gelezen worden. Programma afgebroken." % ser.name )      
    # p1_str=str(p1_raw)
    p1_str=str(p1_raw).replace ('b\'','')
    #p1_str=str(p1_raw, "utf-8")
    p1_line=p1_str.strip()
    stack.append(p1_line)
# als je alles wil zien moet je de volgende line uncommenten
#     print (p1_line)
    p1_teller = p1_teller +1

#Initialize
# stack_teller is mijn tellertje voor de 26 weer door te lopen. Waarschijnlijk mag ik die p1_teller ook gebruiken
stack_teller=0
meter=0

while stack_teller < 26:
    if stack[stack_teller][0:9] == "1-0:1.8.1":
        daldag=int(stack[stack_teller][10:16] )
    elif stack[stack_teller][0:9] == "1-0:1.8.2":
        hoogdag=int(stack[stack_teller][10:16])
    elif stack[stack_teller][0:9] == "1-0:1.7.0":
        afgenomen=int(float(stack[stack_teller][10:16])*1000)
# Gasmeter: 0-1:24.2.1
    elif stack[stack_teller][0:10] == "0-1:24.2.1":
    
# Helaas, 26-09-2016, ik krijg het gas niet aan de gang.
        print ("Gas                     ", int(float(stack[stack_teller][26:35])*1000)) 
    else:
        pass
    stack_teller = stack_teller +1

bashCommand="/usr/bin/rrdtool update /var/www/rrdpower/power.rrd " + ("N:%s:%s:%s" %(daldag,hoogdag,afgenomen)) 
os.system(bashCommand) 

#Debug
# print (bashCommand) 
#Close port and show status
try:
    ser.close()
except:
    sys.exit ("Oops %s. Programma afgebroken." % ser.name )      

