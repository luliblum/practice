#!/usr/bin/python3
import paramiko
import sys
from optparse import OptionParser

parser = OptionParser("usage: %prog [options] arg1 arg2")
#parser.add_option("-H", "--host", dest="hostname",
#        default="127.0.0.1", type="string",
#        help="specify hostname to run on")
parser.add_option("--host", "--hostname", dest="hostname",
        default="127.0.0.1", type="string",
        help="hostname for the ssh command")
parser.add_option("-u", "--username", dest="username",
        default="jonathan", type="string",
        help="username for SSH command")
parser.add_option("-p", "--password", dest="password",
        default="jonathan", type="string",
        help="Password for SSH")
parser.add_option("-c", "--command", dest="command",
        default="ls", type="string",
        help="Command to run")

(options, args) = parser.parse_args()
hostname = options.hostname
username = options.username
password = options.password
command = options.command

#user_name=username
#passwd=password
#ip=hostname
port=22
print ("Please wait creating ssh client...")
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("Please wait, connecting with remote server")
ssh_client.connect(hostname,port,username,password)
cmd="ls -lrt /home/jonathan/ssh_dir"
print ("Please wait, Executing command on remote server")
stdin,stdout,stderr=ssh_client.exec_command(command)
print ("Succesfully executed command on remote server.")
stdout=stdout.readlines()
print (stdout)

