import subprocess
import os
from globals import *

def create_usb(button,filename):
  parentwindow=button.get_parent_window()
  parentwindow.destroy()
  os.system('./unetbootin-linux-585 method=diskimage installtype=USB targetdrive=/dev/sdb isofile='+ISOPATH+filename)
