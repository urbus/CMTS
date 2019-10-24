import getpass
import sys
import telnetlib
import sys
import re

class ComandoCM:
	#El parametro Comando es: flap, phy y CableModems controla la lista command
	def __init__(self, host, usertelnet, passtelnet, usercisco, passcisco, ipcm):
		self.host = host
		self.usertelnet = usertelnet
		self.passtelnet = passtelnet
		self.usercisco = usercisco
		self.passcisco = passcisco
		self.ipcm = ipcm

	def command(self):
		HOST = self.host

		tn = telnetlib.Telnet(HOST)
		user = str(self.usertelnet) + "\n"

		if user:
			tn.write(user)

		password=str(self.passtelnet)+"\n"
		if password:
			tn.write(password)

		ena = str(self.usercisco)+"\n"
		tn.write(ena)
		passw =  (self.passcisco)+"\n"
		tn.write(passw)

		command = []
		cmd = 'show cable modem '+self.ipcm+" verbose\n"
		command.append(cmd)

		phy = False
		tn.write(command[0])

		lines_to_read = 42
		line = []
		ShowStatusOK = []
		ShowStatus = []
		ShowStatusPhy = []

		for i in range(lines_to_read):
		        line.append( tn.read_until(b"\n"))
			#print(line[i].partition(":")[0])
		        tn.write(b'\r\n')

		tn.write("exit\n")

		del line[0:16]
		#del line[0:9]
		
		dataCM = []
	

		for j in range(len(line)):
			d = line[j].partition(":")[2].replace('\n','').replace('\r','')
			dataCM.append(d.strip())
		
		#print(dataCM)
		return dataCM
