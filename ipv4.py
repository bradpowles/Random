import subprocess
import re
proc = str(subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE, shell=True).communicate())
print (re.findall("(?<=IPv4 Address. . . . . . . . . . . : )(\d+\.\d+\.\d+\.\d+)",proc))
print(str(re.findall("(?<=Default Gateway . . . . . . . . . : )(\d+\.\d+\.\d+\.\d+)",proc)))
