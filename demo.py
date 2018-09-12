# this is to demo execute command line  ping , and log the result 
# [operation system : Linux]
#  command-line interface technique 
#  execution tactic
import os
import subprocess
cmd_ping = "ping -c 5  www.td.com"
p = subprocess.Popen(cmd_ping, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
    	# keep the ping log to output.txt
    	f = open("output.txt", "w")
    	f.write(out)
    	# restore environment: remove the file created 
    	os.remove("output.txt")

        