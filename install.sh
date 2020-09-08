#!/bin/bash
set +e #
sudo dpkg-reconfigure tzdata #                                                                               
cd #
echo "configuring Config.txt"
sudo cp /home/volumio/NR1-UI/config/config.txt /boot/ #
echo "Installing Python 3.5.2 and dependencies"
sudo apt-get update #
sudo apt-get install -y build-essential libc6-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev #
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz #
tar -zxvf Python-3.5.2.tgz #
cd Python-3.5.2 #
./configure && make -j4 && sudo make install #
cd #
alias python3=python3.5 #
echo "Updating default pip installation"
sudo pip3 install -U pip #
sudo pip3 install -U setuptools #
echo "installing all other dependencies" #
sudo apt-get install -y python3-dev python3-setuptools python3-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio libffi-dev libcurl4-openssl-dev libssl-dev git-core autoconf make libtool libfftw3-dev libasound2-dev libncursesw5-dev libpulse-dev libtool #
sudo pip3 install --upgrade setuptools pip wheel #
sudo pip3 install --upgrade luma.oled #
sudo pip3 install psutil socketIO-client pcf8574 pycurl gpiozero readchar numpy #
echo "Installing Cava(1)"
git clone https://github.com/Maschine2501/cava.git #
cd cava #
sudo bash autogen.sh #
./configure && make -j4 && sudo make install #
cd #
echo "Copying mpd.conf"
sudo cp /home/volumio/NR1-UI/config/mpd.conf /etc/ #
sudo chmod 777 /etc/mpd.conf #
cd #
echo "Installing Cava 2 (used for loudness-graph)"
git clone https://github.com/Maschine2501/cava.git /home/volumio/CAVAinstall #
cd /home/volumio/CAVAinstall #
sudo bash ./autogen.sh #
./configure --prefix=/home/volumio/CAVA2 && make -j4 && sudo make install #
cd #
echo "installing NR1-UI..."
chmod +x /home/volumio/NR1-UI/nr1ui.py #
sudo cp /home/volumio/NR1-UI/service-files/nr1ui.service /lib/systemd/system/ #
sudo cp /home/volumio/NR1-UI/service-files/cava1.service /lib/systemd/system/ #
sudo cp /home/volumio/NR1-UI/service-files/cava2.service /lib/systemd/system/ #
sudo systemctl daemon-reload #
sudo systemctl enable nr1ui.service #
sudo systemctl enable cava1.service #
sudo systemctl enable cava2.service #
echo " "
echo " "
echo "Installation has finished, congratulations!"
echo " "
echo " "
echo "Please reboot to finish setup."                                                                                                                         
echo " "
exit 0
