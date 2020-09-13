#!/bin/bash
set +e #
sudo dpkg-reconfigure tzdata #                                                                               
cd #
echo "configuring Config.txt"
sudo cp /home/volumio/NR1-UI/config/config.txt /boot/ #
echo "Installing OpenSSL 1.1.1b Python 3.8.5 and dependencies"
mkdir src #
cd ~/src && mkdir openssl && cd openssl #
wget https://www.openssl.org/source/openssl-1.1.1b.tar.gz #
tar xvf openssl-1.1.1b.tar.gz && cd openssl-1.1.1b #
./configure --prefix=/home/volumio/src/openssl-1.1.1b --openssldir=/home/volumio/src/openssl-1.1.1b && make && sudo make install #
cd #
sudo cp /home/volumio/NR1-UI/config/ldconf/libc.conf /etc/ld.so.conf.d #
sudo ldconfig #
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/volumio/src/openssl-1.1.1b/lib #
cd ~/src && mkdir python && cd python #
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz #
tar xf Python-3.8.5.tar.xz #
cd Python-3.8.5 #
sudo cp /home/volumio/NR1-UI/config/python/Setup /home/volumio/src/python/Python-3.8.5/Modules #
./configure --prefix=/home/volumio/src/Python-3.8.5 --with-openssl=/home/volumio/src/openssl-1.1.1b && make -j4 && sudo make altinstall #
export PATH=~/home/volumio/src/Python-3.8.5/bin:$PATH #
export LD_LIBRARY_PATh=/home/volumio/src/Python-3.8.5/bin #
sudo ~/src/Python-3.8.5/bin/pip3 install -U pip #
sudo ~/src/Python-3.8.5/bin/pip3 install -U setuptools #
sudo apt-get install -y python3-dev python3-setuptools python3-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio libffi-dev libcurl4-openssl-dev libssl-dev git-core autoconf make libtool libfftw3-dev libasound2-dev libncursesw5-dev libpulse-dev libtool #
sudo ~/src/Python-3.8.5/bin/pip3 install --upgrade setuptools pip wheel #
sudo ~/src/Python-3.8.5/bin/pip3 install --upgrade luma.oled #
sudo ~/src/Python-3.8.5/bin/pip3 install psutil socketIO-client pcf8574 pycurl gpiozero readchar numpy #
git clone https://github.com/Maschine2501/cava.git #
cd cava #
sudo bash autogen.sh #
./configure && make -j4 && sudo make install #
cd #
#sudo cp /home/volumio/NR1-UI/config/mpd.conf /etc/ #
#sudo chmod 777 /etc/mpd.conf #
git clone https://github.com/Maschine2501/cava.git /home/volumio/CAVAinstall #
cd /home/volumio/CAVAinstall #
sudo bash ./autogen.sh #
./configure --prefix=/home/volumio/CAVA2 && make -j4 && sudo make install #
cd #
chmod +x /home/volumio/NR1-UI/nr1ui38.py #
sudo cp /home/volumio/NR1-UI/service-files/nr1ui38.service /lib/systemd/system/ #
sudo cp /home/volumio/NR1-UI/service-files/cava1.service /lib/systemd/system/ #
sudo cp /home/volumio/NR1-UI/service-files/cava2.service /lib/systemd/system/ #
sudo systemctl daemon-reload #
sudo systemctl enable nr1ui38.service #
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