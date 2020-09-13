#!/bin/bash
set +e #
sudo dpkg-reconfigure tzdata #                                                                               
cd #
echo "configuring Config.txt"
sudo cp /home/volumio/NR1-UI/config/config.txt /boot/ #
echo "Installing OpenSSL 1.1.1b"
mkdir /home/volumio/src #
cd /home/volumio/src && mkdir openssl && cd openssl #
wget https://www.openssl.org/source/openssl-1.1.1b.tar.gz #
tar xvf openssl-1.1.1b.tar.gz && cd openssl-1.1.1b #
./config --prefix=/home/volumio/src/openssl-1.1.1b --openssldir=/home/volumio/src/openssl-1.1.1b && make && sudo make install #
cd #
sudo cp /home/volumio/NR1-UI/config/ldconf/libc.conf /etc/ld.so.conf.d #
sudo ldconfig #
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/volumio/src/openssl-1.1.1b/lib #
echo "Installing 3.8.5 and related modules"
cd /home/volumio/src && mkdir python && cd python #
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz #
tar xf Python-3.8.5.tar.xz #
cd Python-3.8.5 #
sudo cp /home/volumio/NR1-UI/config/python/Setup /home/volumio/src/python/Python-3.8.5/Modules #
./configure --prefix=/home/volumio/src/Python-3.8.5 --with-openssl=/home/volumio/src/openssl-1.1.1b && make -j4 && sudo make altinstall #
export PATH=~/home/volumio/src/Python-3.8.5/bin:$PATH #
export LD_LIBRARY_PATh=/home/volumio/src/Python-3.8.5/bin #
sudo /home/volumio/src/Python-3.8.5/bin/pip3 install -U pip #
sudo /home/volumio/src/Python-3.8.5/bin/pip3 install -U setuptools #
sudo apt-get install -y python3-dev python3-setuptools python3-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio libffi-dev libcurl4-openssl-dev libssl-dev git-core autoconf make libtool libfftw3-dev libasound2-dev libncursesw5-dev libpulse-dev libtool #
sudo /home/volumio/Python-3.8.5/bin/pip3 install --upgrade setuptools pip wheel #
sudo /home/volumio/src/Python-3.8.5/bin/pip3 install --upgrade luma.oled #
sudo /home/volumio/src/Python-3.8.5/bin/pip3 install psutil socketIO-client pcf8574 pycurl gpiozero readchar numpy #
echo "all Python related modules arre installed..."
echo "Installing Cava..."
cdd #
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
echo "Installing NR1-UI..."
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
echo "Please have a look in the Installation instructions to finish setup."                                                                                                                         
echo " "
echo "https://github.com/Maschine2501/NR1-UI/wiki/Installation-Steps-(for-Python3.8.5-Version---Bash-Script)"
echo " "
exit 0
