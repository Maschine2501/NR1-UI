#!/bin/bash
set +e #
sudo dpkg-reconfigure tzdata #
sudo apt-get update #
sudo apt-get install -y build-essential libffi-dev libc6-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev #
cd #
sudo chmod +x /home/volumio/NR1-UI/mpd-buffertime.sh #
sudo chmod +x /home/volumio/NR1-UI/mpd.sh #
sudo chmod +x /home/volumio/NR1-UI/PreConfiguration.sh #
sudo chmod +x /home/volumio/NR1-UI/pcf-i2c-adress-config.sh #
sudo chmod +x /home/volumio/NR1-UI/ftp.sh #
#sudo cp /home/volumio/NR1-UI/ConfigurationFiles/config.txt /boot/ #
echo "dtparam=spi=on" >> /boot/userconfig.txt #
echo "dtparam=i2c=on" >> /boot/userconfig.txt #
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo " " #
echo " " #
echo "________________________________________ " #
echo "This is the Configuration for config.txt" #
echo "________________________________________ " #
echo " " #
echo " " #
echo " " #
echo " " #
echo "______________________________________________" #
echo "Do you want to deactivate (onboard-)Bluetooth?" #
echo "______________________________________________" #
echo " " #
echo " " #
echo "______________________ " #
echo " " #
echo "Valid selections are: " #
echo "1 -> Yes" #
echo "2 -> No" #
echo "--->" #
getBluetooth() { #
  read -p "Enter your decision: " Bluetooth #
  case "$Bluetooth" in #
    1) #    
      echo "dtoverlay=pi3-disable-bt" >> /boot/userconfig.txt #
      echo " " #
      echo "(onboard-) Bluetooth is disabled..." #
      return 0 #
      ;; #
    2) #
      echo " " #
      echo "(onboard-) Bluetooth stays active..." #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getBluetooth; do : ; done #
echo " " #
echo " " #
echo " " #
echo " " #
echo "______________________________________________" #
echo "Do you want to deactivate (onboard-) WiFi?" #
echo "______________________________________________" #
echo " " #
echo " " #
echo "______________________ " #
echo " " #
echo "Valid selections are: " #
echo "1 -> Yes" #
echo "2 -> No" #
echo "--->" #
getWiFi() { #
  read -p "Enter your decision: " WiFi #
  case "$WiFi" in #
    1) #    
      echo "dtoverlay=pi3-disable-wifi" >> /boot/userconfig.txt #
      echo " " #
      echo "(onboard-) WiFi is disabled..." #
      return 0 #
      ;; #
    2) #
      echo " " #
      echo "(onboard-) WiFi stays active..." #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getWiFi; do : ; done #
echo " " #
echo " " #
echo " " #
echo " " #
echo "______________________________________________" #
echo "Do you want to use Spectrum/VU-Meter?" #
echo "(This enables two CAVA instances)" #
echo "______________________________________________" #
echo "---> This needs some resources!!! " #
echo "-> Better use Pi3 or above." #
echo " " #
echo "______________________ " #
echo " " #
echo "Valid selections are: " #
echo "1 -> Yes" #
echo "2 -> No" #
echo "--->" #
getCAVATag() { #
  read -p "Enter your decision: " CAVATag #
  case "$CAVATag" in #
    1) #    
      #sed -i 's/\(SpectrumActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo "CAVA/Spectrum will be installed..." #
      return 0 #
      ;; #
    2) #
      #sed -i 's/\(SpectrumActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo "CAVA/Spectrum won't be installed..." #
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
echo " " #
echo "______________________________________________" #
echo "Do you want to activate Album-Art-Tool for NR1-UI-Remote?" #
echo "______________________________________________" #
echo " " #
echo "More informations under: https://github.com/Maschine2501/NR1-UI-Remote " #
echo " " #
echo " " #
echo "______________________ " #
echo " " #
echo "Valid selections are: " #
echo "1 -> Yes" #
echo "2 -> No" #
echo "--->" #
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
      echo "Album-Art-Tool is activated..." #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(NR1UIRemoteActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py
      echo " " #
      echo "Album-Art-Tool is not active..." #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getRemote; do : ; done #
echo "Installing OpenSSL 1.1.1b" #
mkdir /home/volumio/src #
cd /home/volumio/src && mkdir openssl && cd openssl #
wget https://www.openssl.org/source/openssl-1.1.1b.tar.gz #
tar xvf openssl-1.1.1b.tar.gz && cd openssl-1.1.1b #
./config --prefix=/home/volumio/src/openssl-1.1.1b --openssldir=/home/volumio/src/openssl-1.1.1b && make && sudo make install #
cd #
sudo cp /home/volumio/NR1-UI/ConfigurationFiles/ldconf/libc.conf /etc/ld.so.conf.d #
sudo ldconfig #
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/volumio/src/openssl-1.1.1b/lib #
echo "Installing 3.8.5 and related modules" #
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
sudo /home/volumio/src/Python-3.8.5/bin/pip3.8 install psutil socketIO-client pcf8574 pycurl gpiozero readchar numpy requests #
echo "all Python related modules arre installed..." #
cd #
if [[ $CAVATag -eq 1 ]];
then
    echo "Installing Cava..." #
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
echo "Installing NR1-UI..."  #
chmod +x /home/volumio/NR1-UI/nr1ui.py #
sudo cp /home/volumio/NR1-UI/service-files/nr1ui.service /lib/systemd/system/ #
sudo systemctl daemon-reload #
sudo systemctl enable nr1ui.service #
if [[ $CAVATag -eq 1 ]];
then
    echo "audio_output {" >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo '    type     "fifo"' >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo '    name     "my_fifo"' >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo '    path     "/tmp/mpd.fifo"' >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo '    format   "44100:16:2"' >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo "}" >> /etc/mpd.conf #
    echo "audio_output {" >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo '    type     "fifo"' >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo '    name     "my_fifo2"' >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo '    path     "/tmp/mpd2.fifo"' >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo '    format   "44100:16:2"' >> /etc/mpd.conf #
    echo " " >> /etc/mpd.conf #
    echo "}" >> /etc/mpd.conf #
    echo " " #
    echo " " #
    echo "Fifo-Audio-Outputs for Cava has been added to mpd.conf" #
    echo " " #
    echo " " #
    sudo service mpd restart #
fi
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo " " #
echo " " #
echo " " #
echo "This is the Pre-Configuration Utility for NR1-UI." #
echo " " #
echo " " #
echo " " #
echo " " #
echo " " #
echo "________________________________ " #
echo "Please select your Display-Type." #
echo "________________________________" #
echo " " #
echo " " #
echo "_____________________ " #
echo "Valid selections are:" #
echo "1 -> for ssd1306" #
echo "2 -> for ssd1322" #
echo "3 -> for Braun-specific" #
echo "---> " #
getDisplayType() { #
  read -p "Enter your decision: " DisplayNumber #
  case "$DisplayNumber" in #
    1) #
      sed -i 's/\(DisplayTechnology = \)\(.*\)/\1"'"i2c1306"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo " " #
      echo "Set Display-Type as ssd1306" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(DisplayTechnology = \)\(.*\)/\1"'"spi1322"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo "Set Display-Type as ssd1322" #
      return 0 #
      ;; #         
    3) #
      sed -i 's/\(DisplayTechnology = \)\(.*\)/\1"'"Braun"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo "Set Display-Type as Braun-Specific" #
      return 0 #
      ;; #  
    *) #
      printf %s\\n "Please enter '1' or '2' or '3'" #
      return 1 #
      ;; #
  esac #
} #
until getDisplayType; do : ; done #
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo " " #
getScreenLayout1306() { #
  read -p "Enter your decision: " DisplayNumber #
  case "$DisplayNumber" in #
    1) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Spectrum-Screen"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "Spectrum-Screen" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Layout as Spectrum-Screen" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Progress-Bar"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "Progress-Bar" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Layout as Progress-Bar" #
      return 0 #
      ;; #         
    *) #
      printf %s\\n "Please enter a number between '1' and '2'" #
      return 1 #
      ;; #
  esac #
} #
getScreenLayout1322() { #
  read -p "Enter your decision: " DisplayNumber #
  case "$DisplayNumber" in #
    1) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Spectrum-Left"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "Spectrum-Left" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as Spetrum-Left" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Spectrum-Center"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "Spectrum-Center" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as Spetrum-Center" #
      return 0 #
      ;; #         
    3) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Spectrum-Right"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "Spectrum-Right" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as Spetrum-Right" #
      return 0 #
      ;; #  
    4) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "No-Spectrum" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as No-Spetrum" #
      return 0 #
      ;; #
    5) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Modern"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as Modern" #
      return 0 #
      ;; #         
    6) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"VU-Meter-1"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "VU-Meter-1" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as VU-Meter-1" #
      return 0 #
      ;; #        
    7) #    
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"VU-Meter-2"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo "VU-Meter-2" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as VU-Meter-2" #
      return 0 #
      ;; #
    8) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"VU-Meter-Bar"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "VU-Meter-Bar" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as VU-Meter-Bar" #
      return 0 #
      ;; #         
    9) #
      sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Modern-simplistic"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "Modern-simplistic" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
      echo " " #
      echo "Set Screen Layout as Modern-simplistic" #
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
fi
if [[ $CAVATag -eq 2 && $DisplayNumber -eq 2 ]];
   sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
fi #
if [[ $CAVATag -eq 1 ]];
then
    echo "_________________________________" #
    echo "Please select your Screen Layout." #
    echo "_________________________________" #
    echo " " #
    echo "You can find Previews/Screenshots here: " #
    echo "https://github.com/Maschine2501/NR1-UI " #
    if [ $DisplayNumber -eq 1 ]; #
    then #
       echo "_____________________" #
       echo "Valid selections are:" #
       echo "1 -> Spectrum-Screen" #
       echo "2 -> Progress-Bar" #
       echo "---> " #
       until getScreenLayout1306; do : ; done #
    else #
       echo "_____________________ " #   
       echo "Valid selections are:" #
       echo "1 -> for Spectrum-Left" #
       echo "2 -> for Spectrum-Center" #
       echo "3 -> for Spectrum-Right" #
       echo "4 -> for No-Spectrum" #
       echo "5 -> for Modern" #
       echo "6 -> for VU-Meter-1" #
       echo "7 -> for VU-Meter-2" #
       echo "8 -> for VU-Meter-Bar" #
       echo "9 -> for Modern-simplistic" #
       echo "---> " #
       until getScreenLayout1322; do : ; done #
    fi
fi #
if [[ $CAVATag -eq 2 ]]; #
then #
    if [ $DisplayNumber -eq 1 ];
    then #
        sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"Progress-Bar"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
        echo "Progress-Bar" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
    fi
    if [ $DisplayNumber -eq 2 ]; #
        sed -i 's/\(NowPlayingLayout = \)\(.*\)/\1"'"No-Spectrum"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
        echo "No-Spectrum" > /home/volumio/NR1UI/ConfigurationFiles/LayoutSet.txt #
    fi
fi #
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo "_______________________________" #
echo "Should the Display be rotated?" #
echo "_______________________________"
echo " " #
echo "_____________________ " #
echo "Valid selections are:" #
echo "1 -> Display not rotated" #
echo "2 -> Display rotated 180 degrees " #
echo "---> " #
getDisplayRotation() { #
  read -p "Enter your decision: " RotationNumber #
  case "$RotationNumber" in #
    1) #    
      sed -i 's/\(oledrotation = \)\(.*\)/\10/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo " " #
      echo "Set Display-Rotation to zero Rotation." #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(oledrotation = \)\(.*\)/\12/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo "Set Display-Rotation to 180 degrees Rotation" #
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
echo " " #
echo "__________________________________" #
echo "Do you use LED's?" #
echo "__________________________________" #
echo " " #
echo "More informations here: " #
echo "https://github.com/Maschine2501/NR1-UI/wiki/LED-Wiring " #
echo " " #
echo "_____________________ " #
echo "Valid selections are:" #
echo "1 -> Yes" #
echo "2 -> No" #
echo "---> " #
getLEDUsage() { #
  read -p "Enter your decision: " LEDUsageNumber #
  case "$LEDUsageNumber" in #
    1) #    
      sed -i 's/\(ledActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo " " #
      echo "Activated LED-Option" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(ledActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      sed -i 's/\(ledTechnology = \)\(.*\)/\1None/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py # 
      echo " " #
      echo "Deactivated LED-Option" #
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
      echo "Activated LED-Type: GPIO" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(ledTechnology = \)\(.*\)/\1"'"pcf8574usage"'"/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo " " #
      echo "Activated LED-Type: PCF8574" #
      echo " " #
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
   echo " " #
   echo "__________________________________" #
   echo "Please select your LED Technology:" #
   echo "__________________________________" #
   echo " " #
   echo "More informations here: " #
   echo "https://github.com/Maschine2501/NR1-UI/wiki/LED-Wiring " #
   echo " " #
   echo "_____________________" #
   echo "Valid selections are:" #
   echo "1 -> if you connect LED's directly to the GPIO's of the Raspberry" #
   echo "2 -> if you use an PCF8574 i2c device" #
   echo "---> " #
   until getLEDType; do : ; done #
fi #
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo "________________________________" #
echo "Do you use the Standby-Circuit?" #
echo "________________________________" #
echo " " #
echo "More informations here: " #
echo "https://github.com/Maschine2501/NR1-UI/wiki/Standby-Module " #
echo " " #
echo "WARNING: Do not select YES if you do not have connected the circuit!!!" #
echo " " #
echo "______________________ " #
echo "Valid selections are:" #
echo "1 -> Yes" #
echo "2 -> No" #
echo " " #
StandbyUsage() { #
  read -p "Enter your decision: " StandbyNumber #
  case "$StandbyNumber" in #
    1) #   
      sed -i 's/\(StandbyActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo "dtoverlay=gpio-shutdown" >> /boot/userconfig.txt #
      echo " " #
      echo "Activated Standby-Function" #
      return 0 #
      ;; #
    2) #
      sed -i 's/\(StandbyActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      echo "Deactivated Standby-Function" #
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
echo " " #
echo "__________________________________________________" #
echo "Please select your Button- / Rotary- configuration" #
echo "__________________________________________________ " #
echo " " #
echo "*standard*-configuration means a conection like this: " #
echo "https://raw.githubusercontent.com/Maschine2501/NR1-UI/master/wiki/wiring/Wiring.jpg" #
echo " " #
echo "_____________________" #
echo "Valid selections are:" #
echo "1 -> standard" #
echo "2 -> custom" #
echo "--->" #
getGPIONumberA() { #
  read -p "Please enter the BCM Number for Button A :" ANumber #
  case "$ANumber" in #
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27) #    
      sed -i "s/\(oledBtnA = \)\(.*\)/\1$ANumber/" /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
      echo " " #
      return 0 #
      ;; #
    *) #
      printf %s\\n "Number was out of range...(must be 0-26)" #
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
      printf %s\\n "Number was out of range...(must be 0-26)" #
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
      printf %s\\n "Number was out of range...(must be 0-26)" #
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
      printf %s\\n "Number was out of range...(must be 0-26)" #
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
      printf %s\\n "Number was out of range...(must be 0-26)" #
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
      printf %s\\n "Number was out of range...(must be 0-26)" #
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
      printf %s\\n "Number was out of range...(must be 0-26)" #
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
      echo "Set standard-buttonlayout" #
      return 0 #
      ;; #
    2) #
      echo "Please Enter the BCM-(GPIO) Number for each Button." #
      echo " " #
      echo "For BCM2 enter 2, for BCM17 enter 17..." #
      echo "BCM-list: https://de.pinout.xyz/#" #
      echo " " #
      echo "the input is not filtered!!!"  #
      echo "-> if you enter something wrong, something wrong will happen!" #
      echo " " #
      until getGPIONumberA; do : ; done #
      until getGPIONumberB; do : ; done #
      until getGPIONumberC; do : ; done #
      until getGPIONumberD; do : ; done #     
      until getGPIONumberL; do : ; done #
      until getGPIONumberR; do : ; done #
      until getGPIONumberRB; do : ; done #      
      echo " " #
      echo "Set custom-buttonlayout" #
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
echo " " #
echo "___________________________________________________" #
echo "Please enter a Value for Pause -> to -> Stop -Time." #
echo "___________________________________________________ " #
echo " " #
echo "Value is in Seconds = 15 = 15 Seconds." #
echo "After this time, while playback is paused, player will Stop and return to Standby-Screen." #
echo " " #
echo "____________________________________________ " #
echo "Valid values are numbers between 1 and 86400" #
echo "86400 seconds are 24 hours..." #
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
if [[ $CAVATag -eq 1 ]];
then
    echo "_________________________________________________________________ " #
    echo " " #
    echo " " #
    echo " " #
    echo " " #
    echo "________________________________" #
    echo "Do you want to set a Buffertime?" #
    echo "________________________________" #
    echo " " #
    echo "What is a Buffertime, and why do I (may) need it? " #
    echo "------------------------------------------------- " #
    echo "The way of the audio-signal to your speaker is much faster," #
    echo "faster then the way to the spectrum display." #
    echo "--> This results in an asynchronous spectrum on the display. " #
    echo "" #
    echo "Do you want to set a Buffer-Time now?" #
    echo "(you also can do it later manually...) " #
    echo "" #
    echo "Valid selections are: " #
    echo "1 -> Yes" #
    echo "2 -> No" #
    echo "--->" #
    getBufferTimeT() { #
      read -p "Enter your decision: " BufferTimeT #
      case "$BufferTimeT" in #
        1) #    
          echo " " #
          /bin/bash /home/volumio/NR1-UI/mpd-buffertime.sh #
          echo "Buffertime was set..." #
          echo " " #
          echo "You can change the value anytime by typying: " #
          echo "   cd' " #
          echo "   bash /home/volumio/NR1-UI/mpd-buffertime.sh"
          echo " " #
          return 0 #
          ;; #
        2) #
          echo " " #
          echo "Buffertime was not set..." #
          echo " " #
          echo "You can set it later by typying: " #
          echo "   cd' " #
          echo "   bash /home/volumio/NR1-UI/mpd-buffertime.sh" #
          echo " " #
          return 0 #
          ;; #   
        *) #
          printf %s\\n "Please enter '1' or '2'..." #
          return 1 #
          ;; #
      esac #
    } #
    until getBufferTimeT; do : ; done #
fi
echo " " #
echo " " #
echo " " #
echo " " #
echo "Installation has finished, congratulations!" #
echo " " #
echo " " #
echo "Please have a look in the Installation instructions to finish setup." #                                                                                                                        
echo " " #
echo "https://github.com/Maschine2501/NR1-UI/wiki/Installation-Steps-(for-Python3.8.5-Version---Bash-Script)" #
echo " " #
echo " " #
echo " " #
exit 0
