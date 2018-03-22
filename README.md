# MSF-Undetector
Metasploit python-payload obfuscation, to allow penetration testers bypass Antivirus solutions. Use PyInstaller to create the final, single-file binary.

# Important notice
For PyInstaller issues when creating a single executable, please take a look at [this link](https://github.com/kkar/MSF-Undetector/issues/2). This is **NOT** MSF-Undetector's issue. You just have to follow some extra steps with PyInstaller.

# Requirements
Metasploit framework. May work as expected on Windows, but not tested for now.

# Payload support
Currently, only python payloads are supported.

# Windows targets supported?
Use PyInstaller, py2exe or any tool of your choice to create a single executable.

# Help
```
=============================================
[ MSF-Undetector - http://github.com/kkar ]
=============================================
usage: msf-undetector.py [-h] [-p PAYLOAD] -a ADDRESS -l LPORT [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -p PAYLOAD, --payload PAYLOAD
                        chose your payload (Default:
                        python/meterpreter_reverse_https)
  -a ADDRESS, --address ADDRESS
                        IP/Hostname of metasploit console
  -l LPORT, --lport LPORT
                        msf console listening port
  -o OUTPUT, --output OUTPUT
                        obfuscated filename (Default: output.py)
```
