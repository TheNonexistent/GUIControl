import os
import subprocess

def checkactive():
   cmd = '/bin/systemctl status kerio-kvc.service'
   proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
   stdout_list = proc.communicate()[0].split('\n')
   for line in stdout_list:
      if 'Active:' in line:
         if '(running)' in line:
            return True
   return False

def start():
   os.system("gksudo --message 'Starting The Kerio Serivce Requires Administrator Access.\nPlease Enter Your Password' systemctl start kerio-kvc.service")

def stop():
   os.system("gksudo --message 'Stopping The Kerio Serivce Requires Administrator Access.\nPlease Enter Your Password' systemctl stop kerio-kvc.service")

def configure():
   os.system('gnome-terminal -e "sudo dpkg-reconfigure kerio-control-vpnclient"')
