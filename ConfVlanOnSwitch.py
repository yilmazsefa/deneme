"""
vlan1 üzerine ip verdik
enable password cisco
username sefa password cisco
line vty 0 4
login local
transport input all
işlemlerini switch üzerinde yaptık
wr ile kaydettik

"""


import getpass
import sys
import telnetlib

#Router default-gateway ipsi
Host ="192.168.122.72"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(Host)

tn.read_until("Username: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password+ "\n")

tn.write("enable\n")
tn.write("cisco\n")#username sefa password cisco telnet girişi için.
tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name Python_VLAN_2\n")
tn.write("exit\n")
tn.write("vlan 3\n")
tn.write("name Python_VLAN_3\n")
tn.write("exit\n")
tn.write("vlan 4\n")
tn.write("name Python_VLAN_4\n")
tn.write("exit\n")

tn.write("end\n")
tn.write("exit\n")

print(tn.read_all())
