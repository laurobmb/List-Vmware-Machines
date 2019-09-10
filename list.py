#!/usr/bin/python3

import atexit
import ssl
from pyVim import connect
from pyVmomi import vim
from authentication import credencial 

servidor,usuario,senha = credencial()

def vconnect():
    s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    s.verify_mode = ssl.CERT_NONE
    service_instance = connect.SmartConnect(host=servidor, user=usuario, pwd=senha, sslContext=s)
    atexit.register(connect.Disconnect, service_instance)
    content = service_instance.RetrieveContent()
    return content

content = vconnect()
container = content.rootFolder
viewType = [vim.VirtualMachine]
recursive = True
containerView = content.viewManager.CreateContainerView(container, viewType, recursive)
children = containerView.view

for child in children:
    summary = child.summary
    if summary.runtime.powerState == 'poweredOn':        
        if 'Red Hat Enterprise Linux 7' in summary.config.guestFullName:
            print(summary.config.name+";"+summary.config.annotation)
        elif 'Red Hat Enterprise Linux 6' in summary.config.guestFullName:
            print(summary.config.name+";"+summary.config.annotation)
        elif 'CentOS 7' in summary.config.guestFullName:
            print(summary.config.name+";"+summary.config.annotation)
        elif 'CentOS' in summary.config.guestFullName and not 'CentOS 7' in summary.config.guestFullName:
            print(summary.config.name+";"+summary.config.annotation)
