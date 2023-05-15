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
      sudo apt install proftpd-basic #
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