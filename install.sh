#!/bin/bash
set +e

echo -e "\e[92m    _   ______ ___      __  ______\e[0m"
echo -e "\e[92m   / | / / __ <  /     / / / /  _/\e[0m"
echo -e "\e[92m  /  |/ / /_/ / /_____/ / / // /  \e[0m"
echo -e "\e[92m / /|  / _, _/ /_____/ /_/ // /   \e[0m"
echo -e "\e[92m/_/ |_/_/ |_/_/      \____/___/   \e[0m"
echo ""
echo -e "\e[92mSetting up...\e[0m"
echo -e "\e[92mInstalling all needed Modules and Libraries\e[0m"
echo ""
echo "_________________________________________________________"

sudo dpkg-reconfigure tzdata
sudo apt-get update
sudo apt-get install -y python3-setuptools python3-pip python-rpi.gpi
sudo pip3 install pycurl rpi.gpio psutil socketIO-client pcf8574 pycurl gpiozero readchar numpy requests luma.lcd readchar pillow
sudo apt-get install -y libfftw3-dev libasound2-dev libncursesw5-dev libpulse-dev libtool libiniparser-dev libsdl2-2.0-0 libsdl2-dev libffi-dev libbz2-dev libexpat1-dev liblzma-dev libncurses5-dev libncursesw5-dev libreadline-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libfreetype6-dev libatlas-base-dev libjpeg-dev libfftw3-dev libasound2-dev libncursesw5-dev libtool libcurl4 libssl-dev git autoconf automake make m4

git clone https://github.com/Maschine2501/cava.git
git clone https://github.com/Maschine2501/cava2.git /home/volumio/CAVAinstall

sudo chmod +x /home/volumio/NR1-UI/PreConfiguration.sh
sudo chmod +x /home/volumio/NR1-UI/pcf-i2c-adress-config.sh
sudo chmod +x /home/volumio/NR1-UI/ftp.sh

sudo echo "dtparam=spi=on" >> /boot/userconfig.txt
sudo echo "dtparam=i2c=on" >> /boot/userconfig.txt

sudo pip3 install -U pip
sudo pip3 install -U setuptools
sudo pip3 install --upgrade setuptools pip wheel
sudo pip3 install --upgrade luma.oled

cd

sed -i 's/\(SpectrumActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py
sed -i 's/\(NR1UIRemoteActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py

mkdir /home/volumio/src
cd

echo -e "\e[92mInstalling Cava...\e[0m"
cd /home/volumio/src
wget http://www.fftw.org/fftw-3.3.10.tar.gz
tar zxvf fftw-3.3.10.tar.gz
sudo mkdir /usr/local/fftw
cd fftw-3.3.10
./configure --prefix=/usr/local/fftw --disable-fortran
make
sudo make install
make clean
./configure --enable-float --prefix=/usr/local/fftw --disable-fortran
make
sudo make install
cd

cd /home/volumio/cava
sudo bash autogen.sh
./configure && make -j4 && sudo make install
cd

git clone https://github.com/Maschine2501/cava2.git /home/volumio/CAVAinstall
cd /home/volumio/CAVAinstall
sudo bash ./autogen.sh
./configure --prefix=/home/volumio/CAVA2 && make -j4 && sudo make install
cd

sudo cp /home/volumio/NR1-UI/service-files/cava1.service /lib/systemd/system/
sudo cp /home/volumio/NR1-UI/service-files/cava2.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable cava1.service
sudo systemctl enable cava2.service

echo -e "\e[92mInstalling NR1-UI and Service File...\e[0m"
chmod +x /home/volumio/NR1-UI/nr1ui.py
sudo cp /home/volumio/NR1-UI/service-files/nr1uibuster.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable nr1uibuster.service
sudo sudo cp /home/volumio/NR1-UI/ConfigurationFiles/mpd.conf.tmpl /volumio/app/plugins/music_service/mpd
echo -e "\e[92mFifo-Audio-Outputs for Cava have been added to mpd.conf\e[0m"
sudo service mpd restart

exit 0
