#!/bin/bash
sudo apt-get install -y python-smbus #
sudo apt-get install -y i2c-tools #
echo "_________________________________________________________________ " #
echo " " #
echo -e "\e[4;92mThis is the Configuration for the I2C-adress of the PCFxxxx Controller.\e[0;0m" #
echo " " #
echo -e "\e[4;91mPlease make sure that your PCF8574 module is cocnnected! \e[0;0m" #
echo "" #
echo -e "\e[93mSDA <-> BCM2 (Physical Pin 3) \e[0m" #
echo -e "\e[93mSCL <-> BCM3 (Physical Pin 5)  \e[0m" #
echo -e "\e[93m+5V and GND also connected\e[0m" #
echo " " #
sudo i2cdetect -y 1  #
echo "_______________________________________________" #
echo ""  #
echo -e "\e[4;92mNow, note your I2C-adress! (displayed above...)\e[0m" #
echo " " #
echo -e "\e[93mDo you use a PCF8574 or a PCF8574A?\e[0m" #
echo -e "\e[93mValid selections are: \e[0m" #
echo -e "1 -> \e[92mPCF8574\e[0m" #
echo -e "2 -> \e[92mPCF8574A\e[0m" #
echo -e "\e[93m--->\e[0m" #
getPCF8574() { #
  echo -e "\e[93mPlease enter the adress...\e[0m" #
  echo -e "\e[93mJust enter the number behind the 0x.\e[0m" #
  echo -e "\e[93m(For 0x20 just type 20)\e[0m" #
  read -p "Enter your decision: " PCF8574 #
  case "$PCF8574" in #
    20) #    
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\120/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x20 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;; #
    21) #
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\121/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x21 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;; #   
    22)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\122/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x22 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    23)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\123/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x23 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    24)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\124/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x24 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    25)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\125/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x25 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    26)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\126/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x26 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    27)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\127/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x27 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    *) #
      printf %s\\n "Please enter a '20', '21', '22', '23', '24', '25', '26' or '27'" #
      return 1 #
      ;; #
  esac #
} #
getPCF8574A() { #
  echo -e "\e[93mPlease enter the adress...\e[0m" #
  echo -e "\e[93mJust enter the number behind the 0x.\e[0m" #
  echo -e "\e[93m(For 0x38 just type 38)\e[0m" #
  read -p "Enter your decision: " PCF8574A #
  case "$PCF8574A" in #
    38) #    
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\138/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x38 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;; #
    39) #
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\139/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x39 is selected...\e[0m" #
      echo " " #
      return 0 #
      ;; #   
    3A)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13A/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x3A is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    3B)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13B/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x3B is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    3C)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13C/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x3C is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    3D)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13D/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x3D is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    3E)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13E/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x3E is selected...\e[0m" #
      return 0 #
      ;;     
    3F)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13F/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo -e "\e[92m0x3F is selected...\e[0m" #
      echo " " #
      return 0 #
      ;;     
    *) #
      printf %s\\n "Please enter a '38', '39', '3A', '3B', '3C', '3D', '3E' or '3F'" #
      return 1 #
      ;; #
  esac #
} #
getPCF() { #
  read -p "Enter your decision: " PCF #
  case "$PCF" in #
    1) #    
      echo " " #
      echo -e "\e[92mPCF8574 is selected...\e[0m" #
      echo " " #
      until getPCF8574; do : ; done #
      return 0 #
      ;; #
    2) #
      echo " " #
      echo -e "\e[92mPCF8574 is selected...\e[0m" #
      echo " " #
      until getPCF8574A; do : ; done #
      return 0 #
      ;; #        
    *) #
      printf %s\\n "Please enter '1' or '2'" #
      return 1 #
      ;; #
  esac #
} #
until getPCF; do : ; done #