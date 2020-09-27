#!/bin/bash
sudo apt-get install -y python-smbus #
sudo apt-get install -y i2c-tools #
echo "_________________________________________________________________ " #
echo " " #
echo " " #
echo " " #
echo " " #
echo "_______________________________________________________________________ " #
echo "This is the Configuration for the I2C-adress of the PCFxxxx Controller." #
echo "_______________________________________________________________________ " #
echo " " #
echo "Please make sure that your PCF8574 module is cocnnected. " #
echo "-----------------------------" #
echo "SDA <-> BCM2 (Physical Pin 3) " #
echo "SCL <-> BCM3 (Physical Pin 5)  " #
echo "+5V and GND also connected" #
echo "----------------------------- " #
echo " " #
sudo i2cdetect -y 1  #
echo "_______________________________________________" #
echo "Now, note your I2C-adress! (displayed above...)" #
echo "_______________________________________________" #
echo " " #
echo "Do you use a PCF8574 or a PCF8574A?" #
echo "Valid selections are: " #
echo "1 -> PCF8574" #
echo "2 -> PCF8574A" #
echo "--->" #
getPCF8574() { #
  echo "Please enter the adress..." #
  echo "Just enter the number behind the 0x." #
  echo "(For 0x20 just type 20)" #
  read -p "Enter your decision: " PCF8574 #
  case "$PCF8574" in #
    20) #    
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\120/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x20 is selected..." #
      echo " " #
      return 0 #
      ;; #
    21) #
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\121/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x21 is selected..." #
      echo " " #
      return 0 #
      ;; #   
    22)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\122/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x22 is selected..." #
      echo " " #
      return 0 #
      ;;     
    23)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\123/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x23 is selected..." #
      echo " " #
      return 0 #
      ;;     
    24)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\124/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x24 is selected..." #
      echo " " #
      return 0 #
      ;;     
    25)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\125/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x25 is selected..." #
      echo " " #
      return 0 #
      ;;     
    26)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\126/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x26 is selected..." #
      echo " " #
      return 0 #
      ;;     
    27)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\127/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x27 is selected..." #
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
  echo "Please enter the adress..." #
  echo "Just enter the number behind the 0x." #
  echo "(For 0x38 just type 38)" #
  read -p "Enter your decision: " PCF8574A #
  case "$PCF8574A" in #
    38) #    
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\138/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x38 is selected..." #
      echo " " #
      return 0 #
      ;; #
    39) #
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\139/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x39 is selected..." #
      echo " " #
      return 0 #
      ;; #   
    3A)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13A/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x3A is selected..." #
      echo " " #
      return 0 #
      ;;     
    3B)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13B/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x3B is selected..." #
      echo " " #
      return 0 #
      ;;     
    3C)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13C/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x3C is selected..." #
      echo " " #
      return 0 #
      ;;     
    3D)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13D/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x3D is selected..." #
      echo " " #
      return 0 #
      ;;     
    3E)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13E/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x3E is selected..." #
      echo " " #
      return 0 #
      ;;     
    3F)
      echo " " #
      sed -i 's/\(pcf_address = 0x\)\(.*\)/\13F/' /home/volumio/NR1-UI/modules/StatusLEDpcf.py #
      echo "0x3F is selected..." #
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
      echo "PCF8574 is selected..." #
      echo " " #
      until getPCF8574; do : ; done #
      return 0 #
      ;; #
    2) #
      echo " " #
      echo "PCF8574 is selected..." #
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