from globals import *
import subprocess

def eject():
    command = 'eject', DEVICE
    subprocess.Popen(command)

def tray_close():
    command = 'eject', '-t', DEVICE
    subprocess.Popen(command, 0, "eject", subprocess.PIPE, subprocess.PIPE, subprocess.STDOUT)
