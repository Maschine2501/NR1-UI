#!/bin/bash
set +e #
echo -e "\e[92m    _   ______ ___      __  ______\e[0m" #
echo -e "\e[92m   / | / / __ <  /     / / / /  _/\e[0m" #
echo -e "\e[92m  /  |/ / /_/ / /_____/ / / // /  \e[0m" #
echo -e "\e[92m / /|  / _, _/ /_____/ /_/ // /   \e[0m" #
echo -e "\e[92m/_/ |_/_/ |_/_/      \____/___/   \e[0m" #
echo "" #
echo -e "\e[92mSeting up...\e[0m" #
echo "" #
echo "_________________________________________________________ " #
sudo dpkg-reconfigure tzdata #
sudo apt-get update #
sudo apt-get install -y build-essential libffi-dev libc6-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev #
cd #
sudo chmod +x /home/volumio/NR1-UI/PreConfiguration.sh #
sudo chmod +x /home/volumio/NR1-UI/pcf-i2c-adress-config.sh #
sudo chmod +x /home/volumio/NR1-UI/ftp.sh #
sudo echo "dtparam=spi=on" >> /boot/userconfig.txt #
sudo echo "dtparam=i2c=on" >> /boot/userconfig.txt #
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo " " #
echo " " #
echo -e "\e[92m    _   ______ ___      __  ______\e[0m" #
echo -e "\e[92m   / | / / __ <  /     / / / /  _/\e[0m" #
echo -e "\e[92m  /  |/ / /_/ / /_____/ / / // /  \e[0m" #
echo -e "\e[92m / /|  / _, _/ /_____/ /_/ // /   \e[0m" #
echo -e "\e[92m/_/ |_/_/ |_/_/      \____/___/   \e[0m" #
echo "" #
echo -e "\e[92mConfiguration Part 1...\e[0m" #
echo " " #
echo -e "\e[4;92mDo you want to deactivate (onboard-)Bluetooth?\e[0;0m" #
echo " " #
echo "______________________ " #
echo -e "\e[93mValid selections are: \e[0m" #
echo -e "1 -> \e[92mYes\e[0m" #
echo -e "2 -> \e[91mNo\e[0m" #
echo -e "\e[93m--->\e[0m" #
getBluetooth() { #
  read -p "Enter your decision: " Bluetooth #
  case "$Bluetooth" in #
    1) #    
      echo "dtoverlay=pi3-disable-bt" >> /boot/userconfig.txt #
      echo " " #
      echo -e "\e[92m(onboard-) Bluetooth is disabled...\e[0m" #
      return 0 #
      ;; #
    2) #
      echo " " #
      echo -e "\e[92m(onboard-) Bluetooth stays active...\e[0m" #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getBluetooth; do : ; done #
echo "_______________________________________________ " #
echo " " #
echo -e "\e[4;92mDo you want to deactivate (onboard-) WiFi?\e[0m" #
echo " " #
echo "______________________ " #
echo " " #
echo -e "\e[93mValid selections are: \e[0m" #
echo -e "1 -> \e[92mYes\e[0m" #
echo -e "2 -> \e[91mNo\e[0m" #
echo -e "\e[93m--->\e[0m" #
getWiFi() { #
  read -p "Enter your decision: " WiFi #
  case "$WiFi" in #
    1) #    
      echo "dtoverlay=pi3-disable-wifi" >> /boot/userconfig.txt #
      echo " " #
      echo -e "\e[92m(onboard-) WiFi is disabled...\e[0m" #
      return 0 #
      ;; #
    2) #
      echo " " #
      echo -e "\e[92m(onboard-) WiFi stays active...\e[0m" #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getWiFi; do : ; done #
echo "_______________________________________________________ " #
echo " " #
echo -e "\e[4;92mDo you want to activate Touch-Display-Support?\e[0;0m" #
echo -e "\e[92mNeeded for "'"unofficial"'" displays...\e[0m" #
echo "" #
echo -e "\e[91m---> Touchdisplay Plugin in Volumio needed!!! \e[0m" #
echo -e "\e[91m------> Please install Plugin after Setup. \e[0m" #
echo " " #
echo "______________________ " #
echo -e "\e[93mValid selections are: \e[0m" #
echo -e "1 -> \e[92m5-Inch / 800x480 Pixel\e[0m" #
echo -e "2 -> \e[92m7-Inch / 1024x600 Pixel\e[0m" #
echo -e "3 -> \e[91mNo Touchscreen\e[0m" #
echo -e "\e[93m--->" #
getDisp() { #
  read -p "Enter your decision: " Disp #
  case "$Disp" in #
    1) #    
      echo "hdmi_force_hotplug=1" >> /boot/userconfig.txt #
      echo "hdmi_group=2" >> /boot/userconfig.txt #
      echo "hdmi_mode=87" >> /boot/userconfig.txt #
      echo "hdmi_cvt=800 480 60 6 0 0 0" >> /boot/userconfig.txt #
      echo "hdmi_drive=1" >> /boot/userconfig.txt #
      echo " " #
      echo -e "\e[92mTouch-Display-Support enabled...\e[0m" #
      return 0 #
      ;; #
    2) #    
      echo "hdmi_force_hotplug=1" >> /boot/userconfig.txt #
      echo "hdmi_group=2" >> /boot/userconfig.txt #
      echo "hdmi_mode=87" >> /boot/userconfig.txt #
      echo "hdmi_cvt=1024 600 60 6 0 0 0" >> /boot/userconfig.txt #
      echo "hdmi_drive=1" >> /boot/userconfig.txt #
      echo " " #
      echo -e "\e[92mTouch-Display-Support enabled...\e[0m" #
      return 0 #
      ;; #
    3) #
      echo " " #
      echo -e "\e[92mTouch-Display-Support disabled...\e[0m" #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1', '2' or '3'" #
      return 1 #
      ;; #
  esac #
} #
until getDisp; do : ; done #
echo "_________________________________________________________ " #
echo " " #
echo -e "\e[4;92mDo you want to use Spectrum/VU-Meter?\e[0;0m" #
echo -e "\e[92m(This enables two CAVA instances)\e[0m" #
echo "" #
echo -e "\e[91m---> This needs some resources!!! " #
echo -e "-> Better use Pi3 or above.\e[0m" #
echo " " #
echo "______________________ " #
echo " " #
echo -e "\e[93mValid selections are: \e[0m" #
echo -e "1 -> \e[92mYes\e[0m" #
echo -e "2 -> \e[91mNo\e[0m" #
echo -e "\e[93m--->\e[0m" #" #
getCAVATag() { #
  read -p "Enter your decision: " CAVATag #
  case "$CAVATag" in #
    1) #    
      sed -i 's/\(SpectrumActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -e "\e[92mCAVA/Spectrum will be installed...\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(SpectrumActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -e "\e[92mCAVA/Spectrum won't be installed...\e[0m" #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getCAVATag; do : ; done #
echo "________________________________________________________________________ " #
echo " " #
echo " " #
echo -e "\e[4;92mDo you want to activate Album-Art-Tool for NR1-UI-Remote?\e[0;0m" #
echo " " #
echo -e "More informations under: \e[93mhttps://github.com/Maschine2501/NR1-UI-Remote\e[0m" #
echo " " #
echo -e "\e[25;91mIf you select YES you'll get a promt, select: "'"Standalone"'" \e[0;0m" #
echo "______________________ " #
echo " " #
echo -e "\e[93mValid selections are: \e[0m" #
echo -e "1 -> \e[92mYes\e[0m" #
echo -e "2 -> \e[91mNo\e[0m" #
echo -e "\e[93m--->\e[0m" #
cd #
getRemote() { #
  read -p "Enter your decision: " Remote #
  case "$Remote" in #
    1) #    
      sed -i 's/\(NR1UIRemoteActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      sudo apt install -y proftpd-basic #
      sudo cp /home/volumio/NR1-UI/ConfigurationFiles/proftpd/proftpd.conf /etc/proftpd #
      sudo cp /home/volumio/NR1-UI/ConfigurationFiles/proftpd/proftp-custom.conf /etc/proftpd/conf.d #
      sudo mkdir /home/volumio/proftpd #
      sudo chmod 777 /home/volumio/proftpd #
      sudo cp /home/volumio/NR1-UI/ConfigurationFiles/proftpd/controls.log /home/volumio/proftpd  #
      sudo cp /home/volumio/NR1-UI/ConfigurationFiles/proftpd/proftpd.log /home/volumio/proftpd #
      sudo service proftpd restart #
      echo " " #
      echo -e "\e[92mAlbum-Art-Tool is activated...\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(NR1UIRemoteActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py
      echo " " #
      echo -e "\e[92mAlbum-Art-Tool is not active...\e[0m" #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getRemote; do : ; done #
echo -e "\e[92mInstalling OpenSSL 1.1.1b\e[0m" #
mkdir /home/volumio/src #
cd /home/volumio/src && mkdir openssl && cd openssl #
wget https://www.openssl.org/source/openssl-1.1.1b.tar.gz #
tar xvf openssl-1.1.1b.tar.gz && cd openssl-1.1.1b #
./config --prefix=/home/volumio/src/openssl-1.1.1b --openssldir=/home/volumio/src/openssl-1.1.1b && make && sudo make install #
cd #
sudo cp /home/volumio/NR1-UI/ConfigurationFiles/ldconf/libc.conf /etc/ld.so.conf.d #
sudo ldconfig #
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/volumio/src/openssl-1.1.1b/lib #
echo -e "\e[92mInstalling 3.8.5 and related modules\e[0m" #
cd /home/volumio/src && mkdir python && cd python #
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz #
tar xf Python-3.8.5.tar.xz #
cd Python-3.8.5 #
sudo cp /home/volumio/NR1-UI/ConfigurationFiles/python/Setup /home/volumio/src/python/Python-3.8.5/Modules #
./configure --prefix=/home/volumio/src/Python-3.8.5 --with-openssl=/home/volumio/src/openssl-1.1.1b && make -j4 && sudo make altinstall #
export PATH=/home/volumio/src/Python-3.8.5/bin:$PATH #
export LD_LIBRARY_PATh=/home/volumio/src/Python-3.8.5/bin #
sudo /home/volumio/src/Python-3.8.5/bin/pip3.8 install -U pip #
sudo /home/volumio/src/Python-3.8.5/bin/pip3.8 install -U setuptools #
sudo apt-get install -y python3-dev python3-setuptools python3-pip libfreetype6-dev libjpeg-dev python-rpi.gpio libcurl4-openssl-dev libssl-dev git-core autoconf make libtool libfftw3-dev libasound2-dev libncursesw5-dev libpulse-dev libtool #
sudo /home/volumio/src/Python-3.8.5/bin/pip3.8 install --upgrade setuptools pip wheel #
sudo /home/volumio/src/Python-3.8.5/bin/pip3.8 install --upgrade luma.oled #
sudo /home/volumio/src/Python-3.8.5/bin/pip3.8 install psutil socketIO-client pcf8574 pycurl gpiozero readchar numpy requests luma.lcd #
echo -e "\e[92mAll Python related modules are installed...\e[0m" #
cd #
if [[ $CAVATag -eq 1 ]];
then
    echo -e "\e[92mInstalling Cava...\e[0m"
    git clone https://github.com/Maschine2501/cava.git #
    cd cava #
    sudo bash autogen.sh #
    ./configure && make -j4 && sudo make install #
    cd #
    git clone https://github.com/Maschine2501/cava2.git /home/volumio/CAVAinstall #
    cd /home/volumio/CAVAinstall #
    sudo bash ./autogen.sh #
    ./configure --prefix=/home/volumio/CAVA2 && make -j4 && sudo make install #
    cd #
    sudo cp /home/volumio/NR1-UI/service-files/cava1.service /lib/systemd/system/ #
    sudo cp /home/volumio/NR1-UI/service-files/cava2.service /lib/systemd/system/ #
    sudo systemctl daemon-reload #
    sudo systemctl enable cava1.service #
    sudo systemctl enable cava2.service #
fi
echo -e "\e[92mInstalling NR1-UI...\e[0m"
chmod +x /home/volumio/NR1-UI/nr1ui.py #
sudo cp /home/volumio/NR1-UI/service-files/nr1ui.service /lib/systemd/system/ #
sudo systemctl daemon-reload #
sudo systemctl enable nr1ui.service #
if [[ $CAVATag -eq 1 ]];
then
    sudo sudo cp /home/volumio/NR1-UI/ConfigurationFiles/mpd.conf.tmpl /volumio/app/plugins/music_service/mpd #
    echo " " #
    echo " " #
    echo -e "\e[92mFifo-Audio-Outputs for Cava has been added to mpd.conf\e[0m"
    echo " " #
    echo " " #
    sudo service mpd restart #
fi
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo " " #
echo " " #
echo -e "\e[92m    _   ______ ___      __  ______\e[0m" #
echo -e "\e[92m   / | / / __ <  /     / / / /  _/\e[0m" #
echo -e "\e[92m  /  |/ / /_/ / /_____/ / / // /  \e[0m" #
echo -e "\e[92m / /|  / _, _/ /_____/ /_/ // /   \e[0m" #
echo -e "\e[92m/_/ |_/_/ |_/_/      \____/___/   \e[0m" #
echo "" #
echo -e "\e[92mConfiguration Part 2...\e[0m" #
echo "" #
echo "" #
echo "" #
echo -e "\e[4;92mPlease select your Display-Type.\e[0;0m" #
echo " " #
echo " " #
echo "_____________________ " #
echo -e "\e[93mValid selections are:\e[0m" #
echo -e "1 -> for \e[92mssd1306\e[0m" #
echo -e "2 -> for \e[92mssd1322\e[0m" #
echo -e "3 -> for \e[92mBraun-specific\e[0m" #
echo -e "4 -> for \e[92mssd1351\e[0m" #
echo -e "5 -> for \e[92mst7735\e[0m" #
echo -e "\e[93m---> \e[0m" #
getDisplayType() { #
  read -p "Enter your decision: " DisplayNumber #
  case "$DisplayNumber" in #
    1) #
      sed -i 's/\(DisplayTechnology = \)\(.*\)/\1"'"i2c1306"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo " " #
      echo -e "\e[92mSet Display-Type as ssd1306\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(DisplayTechnology = \)\(.*\)/\1"'"spi1322"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -e "\e[92mSet Display-Type as ssd1322\e[0m" #
      return 0 #
      ;; #         
    3) #
      sed -i 's/\(DisplayTechnology = \)\(.*\)/\1"'"Braun"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -e "\e[92mSet Display-Type as Braun-Specific\e[0m" #
      return 0 #
      ;; # 
    4) #
      sed -i 's/\(DisplayTechnology = \)\(.*\)/\1"'"spi1351"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      sed -i 's/\(NR1UIRemoteActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -e "\e[92mSet Display-Type as ssd1351\e[0m" #
      return 0 #
      ;; #         
    5) #
      sed -i 's/\(DisplayTechnology = \)\(.*\)/\1"'"st7735"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      sed -i 's/\(NR1UIRemoteActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -e "\e[92mSet Display-Type as st7735\e[0m" #
      return 0 #
      ;; #          
    *) #
      printf %s\\n "Please enter '1' or '2' or '3' or '4' or '5'" #
      return 1 #
      ;; #
  esac #
} #
until getDisplayType; do : ; done #
echo "_________________________________________________________________ " #
echo " " #
getScreenLayout1306() { #
  read -p "Enter your decision: " DisplayNumber #
  case "$DisplayNumber" in #
    1) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Spectrum-Screen"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "Spectrum-Screen" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Layout as Spectrum-Screen\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Progress-Bar"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "Progress-Bar" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Layout as Progress-Bar\e[0m" #
      return 0 #
      ;; #         
    *) #
      printf %s\\n "Please enter a number between '1' and '2'" #
      return 1 #
      ;; #
  esac #
} #
getScreenLayout1351() { #
  read -p "Enter your decision: " DisplayNumber #
  case "$DisplayNumber" in #
    1) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Spectrum-Center"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "Spectrum-Center" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Layout as Spectrum-Center\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "No-Spectrum" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Layout as No-Spectrum\e[0m" #
      return 0 #
      ;; #         
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
getScreenLayout7735() { #
  read -p "Enter your decision: " DisplayNumber #
  case "$DisplayNumber" in #
    1) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Spectrum-Center"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "Spectrum-Center" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Layout as Spectrum-Center\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "No-Spectrum" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Layout as No-Spectrum\e[0m" #
      return 0 #
      ;; #         
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
}
getScreenLayout1322() { #
  read -p "Enter your decision: " DisplayNumber #
  case "$DisplayNumber" in #
    1) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Spectrum-Center"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "Spectrum-Center" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Screen Layout as Spectrum-Center\e[0m" #
      return 0 #
      ;; #         
    2) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "No-Spectrum" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Screen Layout as No-Spectrum\e[0m" #
      return 0 #
      ;; #
    3) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Modern"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Screen Layout as Modern\e[0m" #
      return 0 #
      ;; #         
    4) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"VU-Meter-2"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "VU-Meter-2" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Screen Layout as VU-Meter-2\e[0m" #
      return 0 #
      ;; #
    5) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"VU-Meter-Bar"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "VU-Meter-Bar" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo -e "\e[92mSet Screen Layout as VU-Meter-Bar\e[0m" #
      return 0 #
      ;; #         
    *) #
      printf %s\\n "Please enter a number between '1' and '9'" #
      return 1 #
      ;; #
  esac #
} #
if [[ $CAVATag -eq 2 && $DisplayNumber -eq 1 ]];
then #
    sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Progress-Bar"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
    echo "Progress-Bar" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
fi #
if [[ $CAVATag -eq 2 && $DisplayNumber -eq 2 ]];
then
#else
    sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
    echo "No-Spectrum" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
fi #
if [[ $CAVATag -eq 2 && $DisplayNumber -eq 4 ]];
then
#else
    sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
    echo "No-Spectrum" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
fi #
if [[ $CAVATag -eq 2 && $DisplayNumber -eq 5 ]];
then
#else
    sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
    echo "No-Spectrum" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
fi #
if [[ $CAVATag -eq 1 ]];
then
    echo "" #
    echo -e "\e[4;92mPlease select your Screen Layout.\e[0;;0m" #
    echo ""#
    echo -e "\e[93mYou can find Previews/Screenshots here: \e[0m" #
    echo -e "\e[93mhttps://github.com/Maschine2501/NR1-UI \e[0m" #
    if [ $DisplayNumber -eq 1 ]; #
    then #
       echo "_____________________" #
       echo -e "\e[93mValid selections are:\e[0m" #
       echo -e "1 -> \e[92mSpectrum-Screen\e[0m" #
       echo -e "2 -> \e[92mProgress-Bar\e[0m" #
       echo -e "\e[93m---> \e[0m" #
       until getScreenLayout1306; do : ; done #
    fi #
    if [ $DisplayNumber -eq 2 ]; #
    then #
       echo "_____________________ " #   
       echo -e "\e[93mValid selections are:\e[0m" #
       echo -e "1 -> for \e[92mSpectrum-Center\e[0m" #
       echo -e "2 -> for \e[92mNo-Spectrum\e[0m" #
       echo -e "3 -> for \e[92mModern\e[0m" #
       echo -e "4 -> for \e[92mVU-Meter-2\e[0m" #
       echo -e "5 -> for \e[92mVU-Meter-Bar\e[0m" #
       echo -e "\e[93m---> \e[0m" #
       until getScreenLayout1322; do : ; done #
    fi #
    if [ $DisplayNumber -eq 3 ]; #
    then #
       echo "_____________________ " #   
       echo -e "\e[93mValid selections are:\e[0m" #
       echo -e "1 -> for \e[92mSpectrum-Center\e[0m" #
       echo -e "2 -> for \e[92mNo-Spectrum\e[0m" #
       echo -e "3 -> for \e[92mModern\e[0m" #
       echo -e "4 -> for \e[92mVU-Meter-2\e[0m" #
       echo -e "5 -> for \e[92mVU-Meter-Bar\e[0m" #
       echo -e "\e[93m---> \e[0m" #
       until getScreenLayout1322; do : ; done #
    fi #
    if [ $DisplayNumber -eq 4 ]; #
    then #
       echo "_____________________" #
       echo -e "\e[93mValid selections are:\e[0m" #
       echo -e "1 -> \e[92mSpectrum-Center\e[0m" #
       echo -e "2 -> \e[92mNo-Spectrum\e[0m" #
       echo -e "\e[93m---> \e[0m" #
       until getScreenLayout1351; do : ; done #
    fi #
    if [ $DisplayNumber -eq 5 ]; #
    then #
       echo "_____________________" #
       echo -e "\e[93mValid selections are:\e[0m" #
       echo -e "1 -> \e[92mSpectrum-Center\e[0m" #
       echo -e "2 -> \e[92mNo-Spectrum\e[0m" #
       echo -e "\e[93m---> \e[0m" #
       until getScreenLayout7735; do : ; done #
    fi
fi #
#if [[ $CAVATag -eq 2 ]]; #
#then #
#    if [ $DisplayNumber -eq 1 ];
#    then #
#        sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Progress-Bar"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
#        echo "Progress-Bar" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
#    #fi
#    #if [ $DisplayNumber -eq 2 ]; #
#    else
#        sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
#        echo "No-Spectrum" > /home/volumio/NR1-UI/ConfigurationFiles/LayoutSet.txt #
#    fi
#fi #
echo "_________________________________________________________________ " #
echo " " #
echo -e "\e[4;92mShould the Display be rotated? \e[0;0m" #
echo " " #
echo "_____________________ " #
echo -e "\e[93mValid selections are:\e[0m" #
echo -e "1 -> \e[92mDisplay not rotated\e[0m" #
echo -e "2 -> \e[92mDisplay rotated 180 degrees \e[0m" #
echo -e "\e[93m---> \e[0m" #
getDisplayRotation() { #
  read -p "Enter your decision: " RotationNumber #
  case "$RotationNumber" in #
    1) #    
      sed -i 's/\(oledrotation = \)\(.*\)/\10/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo " " #
      echo -e "\e[92mSet Display-Rotation to zero Rotation.\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(oledrotation = \)\(.*\)/\12/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -e "\e[92mSet Display-Rotation to 180 degrees Rotation\e[0m" #
      return 0 #
      ;; #         
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getDisplayRotation; do : ; done #
echo "_________________________________________________________________ " #
echo " " #
echo -e "\e[4;92mDo you use LED's?\e[0m" #
echo " " #
echo -e "\e[93mMore informations here: \e[0m" #
echo -e "\e[93mhttps://github.com/Maschine2501/NR1-UI/wiki/LED-Wiring \e[0m" #
echo " " #
echo "_____________________ " #
echo -e "\e[93mValid selections are:\e[0m" #
echo -e "1 -> \e[92mYes\e[0m" #
echo -e "2 -> \e[91mNo\e[0m" #
echo -e "\e[93m---> \e[0m" #
getLEDUsage() { #
  read -p "Enter your decision: " LEDUsageNumber #
  case "$LEDUsageNumber" in #
    1) #    
      sed -i 's/\(ledActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo " " #
      echo -e "\e[92mActivated LED-Option\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(ledActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      sed -i 's/\(ledTechnology = \)\(.*\)/\1None/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo " " #
      echo -e "\e[92mDeactivated LED-Option\e[0m" #
      return 0 #
      ;; #         
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getLEDUsage; do : ; done #
getLEDType() { #
  read -p "Enter your decision: " LEDTypeNumber #
  case "$LEDTypeNumber" in #
    1) #    
      sed -i 's/\(ledTechnology = \)\(.*\)/\1"'"GPIOusage"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo -e "\e[92mActivated LED-Type: GPIO\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(ledTechnology = \)\(.*\)/\1"'"pcf8574usage"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo -e "\e[92mActivated LED-Type: PCF8574\e[0m" #
      echo " " #
      echo " " #
      /bin/bash /home/volumio/NR1-UI/pcf-i2c-adress-config.sh
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
if [ $LEDUsageNumber -eq 1 ]; then #
   echo "_________________________________________________________________ " #
   echo " " #
   echo -e "\e[4;92mPlease select your LED Technology:\e[0;0m" #
   echo " " #
   echo -e "\e[93mMore informations here: \e[0m" #
   echo -e "\e[93mhttps://github.com/Maschine2501/NR1-UI/wiki/LED-Wiring \e[0;0m" #
   echo " " #
   echo "_____________________" #
   echo -e "\e[93mValid selections are:\e[0m" #
   echo -e "1 -> \e[92mif you connect LED's directly to the GPIO's of the Raspberry\e[0m" #
   echo -e "2 -> \e[92mif you use an PCF8574 i2c device\e[0m" #
   echo -e "\e[93m---> \e[0m" #
   until getLEDType; do : ; done #
fi #
echo "_________________________________________________________________ " #
echo " " #
echo -e "\e[4;92mDo you use the Standby-Circuit?\e[0;0m" #
echo " " #
echo -e "\e[93mMore informations here: \e[0m" #
echo -e "\e[93mhttps://github.com/Maschine2501/NR1-UI/wiki/Standby-Module \e[0;0m" #
echo " " #
echo -e "\e[4;91mWARNING: Do not select YES if you do not have connected the circuit!!!\e[0;0m" #
echo " " #
echo "______________________ " #
echo -e "\e[93mValid selections are:\e[0m" #
echo -e "1 -> \e[92mYes\e[0m" #
echo -e "2 -> \e[91mNo\e[0m" #
echo -e "\e[93m----> \e[0m" #
StandbyUsage() { #
  read -p "Enter your decision: " StandbyNumber #
  case "$StandbyNumber" in #
    1) #   
      sed -i 's/\(StandbyActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "dtoverlay=gpio-shutdown" >> /boot/userconfig.txt #
      echo " " #
      echo -e "\e[92mActivated Standby-Function\e[0m" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(StandbyActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -e "\e[92mDeactivated Standby-Function\e[0m" #
      return 0 #
      ;; #         
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until StandbyUsage; do : ; done #
echo "_________________________________________________________________ " #
echo " " #
echo -e "\e[4;92mPlease select your Button- / Rotary- configuration\e[0;0m" #
echo " " #
echo -e "\e[93m*standard*-configuration means a conection like this: \e[0m" #
echo -e "\e[93mhttps://raw.githubusercontent.com/Maschine2501/NR1-UI/master/wiki/wiring/Wiring.jpg\e[0m" #
echo " " #
echo "_____________________" #
echo -e "\e[93mValid selections are:\e[0m" #
echo -e "\e[92m1 -> standard\e[0m" #
echo -e "\e[91m2 -> custom\e[0m" #
echo -e "\e[93m--->\e[0m" #
getGPIONumberA() { #
  read -p "Please enter the BCM Number for Button A :" ANumber #
  case "$ANumber" in #
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27) #    
      sed -i "s/\(oledBtnA = \)\(.*\)/\1$ANumber/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Number was out of range...(must be 0-27)" #
      return 1 #
      ;; #
  esac #
} #
getGPIONumberB() { #
  read -p "Please enter the BCM Number for Button B :" BNumber #
  case "$BNumber" in #
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27) #    
      sed -i "s/\(oledBtnB = \)\(.*\)/\1$BNumber/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Number was out of range...(must be 0-27)" #
      return 1 #
      ;; #
  esac #
} #
getGPIONumberC() { #
  read -p "Please enter the BCM Number for Button C :" CNumber #
  case "$CNumber" in #
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27) #    
      sed -i "s/\(oledBtnC = \)\(.*\)/\1$CNumber/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Number was out of range...(must be 0-27)" #
      return 1 #
      ;; #
  esac #
} #
getGPIONumberD() { #
  read -p "Please enter the BCM Number for Button D :" DNumber #
  case "$DNumber" in #
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27) #    
      sed -i "s/\(oledBtnD = \)\(.*\)/\1$DNumber/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Number was out of range...(must be 0-27)" #
      return 1 #
      ;; #
  esac #
} #
getGPIONumberL() { #
  read -p "Please enter the BCM Number for Rotary-Left :" LNumber #
  case "$LNumber" in #
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27) #    
      sed -i "s/\(oledRtrLeft = \)\(.*\)/\1$LNumber/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Number was out of range...(must be 0-27)" #
      return 1 #
      ;; #
  esac #
} #
getGPIONumberR() { #
  read -p "Please enter the BCM Number for Rotary-Right :" RNumber #
  case "$RNumber" in #
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27) #    
      sed -i "s/\(oledRtrRight = \)\(.*\)/\1$RNumber/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Number was out of range...(must be 0-27)" #
      return 1 #
      ;; #
  esac #
} #
getGPIONumberRB() { #
  read -p "Please enter the BCM Number for Rotary-Button :" RBNumber #
  case "$RBNumber" in #
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27) #    
      sed -i "s/\(oledRtrBtn = \)\(.*\)/\1$RBNumber/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Number was out of range...(must be 0-27)" #
      return 1 #
      ;; #
  esac #
}
getButtonLayout() { #
  read -p "Enter your decision: " ButonNumber #
  case "$ButonNumber" in #
    1) #    
      sed -i 's/\(oledBtn = \)\(.*\)/\14/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      sed -i 's/\(oledBtn = \)\(.*\)/\117/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      sed -i 's/\(oledBtn = \)\(.*\)/\15/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      sed -i 's/\(oledBtn = \)\(.*\)/\16/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      sed -i 's/\(oledRtrLeft = \)\(.*\)/\122/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      sed -i 's/\(oledRtrRight = \)\(.*\)/\123/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      sed -i 's/\(oledRtrBtn = \)\(.*\)/\127/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #  
      echo " " #
      echo -e "\e[92mSet standard-buttonlayout\e[0m" #
      return 0 #
      ;; #
    2) #
      echo -e "\e[4;92mPlease Enter the BCM-(GPIO) Number for each Button.\e[0;0m" #
      echo " " #
      echo -e "\e[93mFor BCM2 enter 2, for BCM17 enter 17...\e[0m" #
      echo -e "\e[93mBCM-list: https://de.pinout.xyz/#\e[0m" #
      echo " " #
      echo -e "\e[91mthe input is not filtered!!!\e[0m" #
      echo -e "\e[91m-> if you enter something wrong, something wrong will happen!\e[0m" #
      echo " " #
      until getGPIONumberA; do : ; done #
      until getGPIONumberB; do : ; done #
      until getGPIONumberC; do : ; done #
      until getGPIONumberD; do : ; done #     
      until getGPIONumberL; do : ; done #
      until getGPIONumberR; do : ; done #
      until getGPIONumberRB; do : ; done #      
      echo " " #
      echo -e "\e[92mSet custom-buttonlayout\e[0m" #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getButtonLayout; do : ; done #
echo "_________________________________________________________________" #
echo " " #
echo -e "\e[4;92mPlease enter a Value for Pause -> to -> Stop -Time.\e[0;0m" #
echo " " #
echo -e "\e[93mValue is in Seconds = 15 = 15 Seconds.\e[0m" #
echo -e "\e[93mAfter this time, while playback is paused, player will Stop and return to Standby-Screen.\e[0;0m" #
echo " " #
echo "____________________________________________ " #
echo -e "\e[93mValid values are numbers between 1 and 86400\e[0m" #
echo -e "\e[93m86400 seconds are 24 hours...\e[0m" #
echo " " #
getPlay2PauseTime() { #
  read -p "Enter a Time (in seconds): " Play2PauseT #
  case "$Play2PauseT" in #
    [1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-8][0-6][0-3][0-9][0-9]|86400) #     
      sed -i "s/\(oledPause2StopTime = \)\(.*\)/\1$Play2PauseT.0/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo -n "Set Play-to-Pause timer to "; echo -n "${Play2PauseT} "; echo -n "seconds" #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Please enter a number between '1' and '86400'" #
      return 1 #
      ;; #
  esac #
} #
until getPlay2PauseTime; do : ; done #
echo " " #
echo " " #
echo " " #
echo " " #
echo -e "\e[4;92mConfiguration has finished, congratulations!\e[0;0m" #
echo " " #
echo " " #
echo -e "\e[93mPlease have a look in the Installation instructions to finish setup.\e[0m" #                                                                                                                      
echo " " #
echo -e "\e[93mhttps://github.com/Maschine2501/NR1-UI/wiki/Installation-Steps-(for-Python3.8.5-Version---Bash-Script)\e[0m" #
echo " " #
echo " " #
echo -e "\e[25;91mIf you use CAVA/Spectrum: \e[0;0m" #
echo " " #
echo -e "\e[91mPlease set Audio-Output to HDMI or Headphones and save setting.\e[0m" #
echo -e "\e[91mNow Select your DAC/Playback device and save aggain.\e[0m" #
exit 0 #
