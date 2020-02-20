#!/bin/bash

#first commands enable touchscreen output - Touchscreen plugin needs to be enabled manualy by webinterface
sudo sh -c "echo 'hdmi_group=2' >> /boot/config.txt"
sudo sh -c "echo 'hdmi_mode=87' >> /boot/config.txt"
sudo sh -c "echo 'hdmi_cvt 1024 600 60 6 0 0 0' >> /boot/config.txt"
sudo sh -c "echo 'hdmi_drive=1' >> /boot/config.txt"
sudo sh -c "echo 'dtparam=spi=on' >> /boot/config.txt"

#2nd comans will install Braun-OledUI
apt-get update
apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio
pip install --upgrade setuptools pip wheel
pip install --upgrade socketIO-client-2 luma.oled
chmod +x BraunNR1-OledUI/oledui.py
cp BraunNR1-OledUI/oledui.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable oledui.service

echo " "
echo " "
echo " /$$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$          /$$$$$$  /$$                 /$$ /$$   /$$ /$$$$$$"
echo "| $$__  $$| $$__  $$ /$$__  $$| $$  | $$| $$$ | $$         /$$__  $$| $$                | $$| $$  | $$|_  $$_/"
echo "| $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$| $$$$| $$        | $$  \ $$| $$  /$$$$$$   /$$$$$$$| $$  | $$  | $$  "
echo "| $$$$$$$ | $$$$$$$/| $$$$$$$$| $$  | $$| $$ $$ $$ /$$$$$$| $$  | $$| $$ /$$__  $$ /$$__  $$| $$  | $$  | $$  "
echo "| $$__  $$| $$__  $$| $$__  $$| $$  | $$| $$  $$$$|______/| $$  | $$| $$| $$$$$$$$| $$  | $$| $$  | $$  | $$  "
echo "| $$  \ $$| $$  \ $$| $$  | $$| $$  | $$| $$\  $$$        | $$  | $$| $$| $$_____/| $$  | $$| $$  | $$  | $$  "
echo "| $$$$$$$/| $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$        |  $$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$/ /$$$$$$"
echo "|_______/ |__/  |__/|__/  |__/ \______/ |__/  \__/         \______/ |__/ \_______/ \_______/ \______/ |______/"
echo " "
echo " "
echo "Instalation Done!"
echo " "
echo " "
echo "To activate it, reboot the Raspberry."
echo " "
echo " "
echo " "
echo " "

exit
