from CiscoCMsta import *
ipcm = 3
c = ComandoCMsta("ip", "usuarioTelnet", "passwordTelnet", "usuarioCMTS", "passwordCMTS", "IPcmts",ipcm)

print(c.commandCMTS())
