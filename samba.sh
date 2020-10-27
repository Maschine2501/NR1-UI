#!/bin/bash
sudo apt-get update #
sudo apt-get install -y samba samba-common smbclient #
echo "[global]" > /etc/samba/smb.conf
echo "workgroup = WORKGROUP" >> /etc/samba/smb.conf
echo "security = user" >> /etc/samba/smb.conf
echo "encrypt passwords = yes" >> /etc/samba/smb.conf
echo "client min protocol = SMB2" >> /etc/samba/smb.conf
echo "client max protocol = SMB3" >> /etc/samba/smb.conf
echo "[NR1-Samba]" >> /etc/samba/smb.conf
echo "comment = NR1-Sambashare" >> /etc/samba/smb.conf
echo "path = /home/volumio" >> /etc/samba/smb.conf
echo "read only = no" >> /etc/samba/smb.conf
sudo smbpasswd -a volumio
sudo service smbd restart
sudo service nmbd restart