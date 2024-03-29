#!/bin/bash
set +e #
echo -e "\e[92m    _   ______ ___      __  ______\e[0m" #
echo -e "\e[92m   / | / / __ <  /     / / / /  _/\e[0m" #
echo -e "\e[92m  /  |/ / /_/ / /_____/ / / // /  \e[0m" #
echo -e "\e[92m / /|  / _, _/ /_____/ /_/ // /   \e[0m" #
echo -e "\e[92m/_/ |_/_/ |_/_/      \____/___/   \e[0m" #
echo "" #
echo -e "\e[92mSeting up...\e[0m" #
echo -e "\e[92mIinstalling all needed Modules and Librarys\e[0m" #
echo "" #
echo "_________________________________________________________ " #
sudo dpkg-reconfigure tzdata #
sudo apt-get update #
sudo apt-get install -y python3-setuptools python3-pip python-rpi.gpi #
sudo pip3 install pycurl rpi.gpio psutil socketIO-client pcf8574 pycurl gpiozero readchar numpy requests luma.lcd readchar pillow #
sudo apt-get install -y libfftw3-dev libasound2-dev libncursesw5-dev libpulse-dev libtool libiniparser-dev libsdl2-2.0-0 libsdl2-dev libffi-dev libbz2-dev libexpat1-dev liblzma-dev libncurses5-dev libncursesw5-dev libreadline-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libfreetype6-dev libatlas-base-dev libjpeg-dev libfftw3-dev libasound2-dev libncursesw5-dev libtool libcurl4 libssl-dev git autoconf automake make m4 #
git clone https://github.com/Maschine2501/cava.git #
git clone https://github.com/Maschine2501/cava2.git /home/volumio/CAVAinstall #
sudo chmod +x /home/volumio/NR1-UI/PreConfiguration.sh #
sudo chmod +x /home/volumio/NR1-UI/pcf-i2c-adress-config.sh #
sudo chmod +x /home/volumio/NR1-UI/ftp.sh #
sudo echo "dtparam=spi=on" >> /boot/userconfig.txt #
sudo echo "dtparam=i2c=on" >> /boot/userconfig.txt #
sudo pip3 install -U pip #
sudo pip3 install -U setuptools #
sudo pip3 install --upgrade setuptools pip wheel #
sudo pip3 install --upgrade luma.oled #
cd #
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo " " #
echo " " #
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
echo -e "\e[4;92mDo you want to activate (Touch-)Display-Support?\e[0;0m" #
echo -e "\e[92mNeeded for "'"unofficial"'" LCD displays...\e[0m" #
echo "" #
echo -e "\e[91m---> Touchdisplay Plugin in Volumio needed!!! \e[0m" #
echo -e "\e[91m------> Please install Plugin after Setup. \e[0m" #
echo " " #
echo "______________________ " #
echo -e "\e[93mValid selections are: \e[0m" #
echo -e "1 -> \e[92m5-Inch / 800x480 Pixel\e[0m" #
echo -e "2 -> \e[92m7-Inch / 1024x600 Pixel\e[0m" #
echo -e "3 -> \e[92m8,8-Inch / 1920x480 Pixel\e[0m" #
echo -e "4 -> \e[91mNo (Touch-)screen\e[0m" #
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
      echo "hdmi_group=2" >> /boot/userconfig.txt #
      echo "hdmi_mode=87" >> /boot/userconfig.txt #
      echo "hdmi_timings=480 0 30 30 30 1920 0 6 6 6 0 0 0 60 0 55296000 8" >> /boot/userconfig.txt #
      echo "hdmi_drive=2" >> /boot/userconfig.txt #
      echo "display_rotate=1" >> /boot/userconfig.txt #
      echo "hdmi_force_mode=1" >> /boot/userconfig.txt #
      echo "framebuffer_width=1920" >> /boot/userconfig.txt #
      echo "framebuffer_height=480" >> /boot/userconfig.txt #
      echo "max_framebuffer_width=1920" >> /boot/userconfig.txt #
      echo "max_framebuffer_height=1920" >> /boot/userconfig.txt #
      echo " " #
      echo -e "\e[92mTouch-Display-Support enabled...\e[0m" #
      return 0 #
      ;; #
    4) #
      echo " " #
      echo -e "\e[92mTouch-Display-Support disabled...\e[0m" #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1', '2', '3' or '4'" #
      return 1 #
      ;; #
  esac #
} #
until getDisp; do : ; done #
sed -i 's/\(SpectrumActive = \)\(.*\)/\1True/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py #
sed -i 's/\(NR1UIRemoteActive = \)\(.*\)/\1False/' /home/volumio/NR1-UI/ConfigurationFiles/PreConfiguration.py
mkdir /home/volumio/src #
cd #
echo -e "\e[92mInstalling Cava...\e[0m"
cd /home/volumio/src #
wget http://www.fftw.org/fftw-3.3.10.tar.gz #
tar zxvf fftw-3.3.10.tar.gz #
sudo mkdir /usr/local/fftw #
cd fftw-3.3.10 #
./configure --prefix=/usr/local/fftw --disable-fortran #
make #
sudo make install #
make clean #
./configure --enable-float --prefix=/usr/local/fftw --disable-fortran #
make #
sudo make install #
cd #
cd /home/volumio/cava #
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
echo -e "\e[92mInstalling NR1-UI and Service File...\e[0m"
chmod +x /home/volumio/NR1-UI/nr1ui.py #
sudo cp /home/volumio/NR1-UI/service-files/nr1uibuster.service /lib/systemd/system/ #
sudo systemctl daemon-reload #
sudo systemctl enable nr1uibuster.service #
sudo sudo cp /home/volumio/NR1-UI/ConfigurationFiles/mpd.conf.tmpl /volumio/app/plugins/music_service/mpd #
echo -e "\e[92mFifo-Audio-Outputs for Cava has been added to mpd.conf\e[0m"
sudo service mpd restart #
echo "_________________________________________________________________ " #
echo "" #
echo "" #
echo "" #
echo -e "\e[4;92mPlease select your SPI/I2C Display-Type.\e[0;0m" #
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
echo "_________________________________________________________________ " #
echo " " #
echo -e "\e[4;92mShould the SPI/I2C Display be rotated? \e[0;0m" #
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
echo -e "\e[93mhttps://github.com/Maschine2501/NR1-UI/wiki/Volumio-Buster-Installation\e[0m" #
echo " " #
echo " " #
echo " " #
echo -e "\e[91mPlease set Audio-Output to HDMI or Headphones and save setting.\e[0m" #
echo -e "\e[91mNow re-select your DAC/Playback device and save aggain.\e[0m" #
echo " " #
echo " " #
echo " " #
exit 0 #
