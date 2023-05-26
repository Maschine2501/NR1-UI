Inspired by: [diehardsk/Volumio-OledUI](https://github.com/diehardsk/Volumio-OledUI) // 
This is the Python3 version of [Maschine2501/Volumio-OledUI](https://github.com/Maschine2501/Volumio-OledUI/)

---

## [1. Installation steps]
---
Step [1: Download Volumio onto your sd card]

a) Download Raspberry Pi Imager: 
Go to the Raspberry Pi website (www.raspberrypi.org) and download the Raspberry Pi Imager for your operating system (Windows, macOS, or Linux). Install the imager on your computer.

b) Insert the SD card: 
Insert the SD card into your computer's SD card reader.

c) Launch Raspberry Pi Imager: 
Open the Raspberry Pi Imager software that you installed in step 1.

d) Select the operating system: 
In Raspberry Pi Imager, click on "Choose OS" and scroll down to find "Media Player OS" in the list. Then select "Volumio" from the options.

e) Choose the target storage: 
Click on "Choose SD Card" and select the SD card that you inserted in step 2. Make sure to choose the correct one, as the imager will erase all data on the selected card.

f) Write the image: 
Click on "Write" to start writing the Volumio image to the SD card. This process may take a few minutes to complete.

g) Eject the SD card: 
Once the writing process is finished, safely eject the SD card from your computer.

---
## [Step 2: Install Volumio]


a) Power on the Raspberry Pi: 
Connect the power supply to the Raspberry Pi, and it will boot up.

b) Find Volumio's Wi-Fi access point: 
Wait for a few minutes for Volumio to start up its Wi-Fi hotspot. It creates a temporary Wi-Fi network to allow you to connect and configure it. Look for a Wi-Fi network named something like "Volumio" or "Volumio-xxxx" (where "xxxx" represents a unique identifier).

c) Connect to Volumio's Wi-Fi network: 
On your computer or mobile device, go to the Wi-Fi settings and select the Volumio Wi-Fi network. Connect to it using the default password, which is typically "volumio2" (without quotes).

d) Access the Volumio web interface: 
Once connected to the Volumio Wi-Fi network, open a web browser and enter "volumio.local" or "http://192.168.211.1" in the address bar. This will take you to the Volumio web interface.

e) Set up Wi-Fi: 
In the Volumio web interface, navigate to the "Network" section. Here, you can select your Wi-Fi network from the available networks and enter the necessary credentials (such as SSID and password). Save the settings.

f) Reconnect to your regular Wi-Fi network: 
Once you have configured the Wi-Fi settings in Volumio, disconnect from Volumio's Wi-Fi network on your computer or mobile device. Reconnect to your regular Wi-Fi network.

g) Access Volumio on your network: 
After reconnecting to your regular Wi-Fi network, you can now access Volumio by entering "volumio.local" or the IP address assigned to the Raspberry Pi by your router in the web browser on any device connected to the same network.

By following these steps, you should be able to connect to Volumio on your Raspberry Pi headlessly using its Wi-Fi access point and configure it to connect to your desired Wi-Fi network.
```
git clone http://github.com/theshepherdmatt/NR1-UI.git

bash NR1-UI/install.sh
```

![MS2501](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/MadeByGloria.jpg)
[Logo made by glorious @Klassik_Otaku](http://www.instagram.com/klassik_otaku)

