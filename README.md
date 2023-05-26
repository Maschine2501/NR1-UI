Inspired by: [diehardsk/Volumio-OledUI](https://github.com/diehardsk/Volumio-OledUI) // 
This is the Python3 version of [Maschine2501/Volumio-OledUI](https://github.com/Maschine2501/Volumio-OledUI/)

---

## [1. Installation steps]
---
Welcome to the Raspberry Pi installation extravaganza! This comprehensive guide will take you through a series of steps to set up your Raspberry Pi with Volumio, the magical music player. We'll begin by installing the Raspberry Pi Imager, a handy tool that brings your Pi to life. Then, we'll dive into Volumio, a music player that will make your ears tingle with joy. To connect and control your Pi remotely, we'll harness the power of PuTTY, allowing for seamless access. And the grand finale awaits as we clone the NR1-UI repository from GitHub, unlocking a treasure trove of marvelous software wonders. So, fasten your seatbelts and get ready for a whimsical Raspberry Pi adventure that will leave you with a fully-equipped music powerhouse!
---
Step [1: Download Volumio onto your sd card]

a) Download Raspberry Pi Imager: 
On your pc or laptop go to the Raspberry Pi website (www.raspberrypi.org) and download the Raspberry Pi Imager for your operating system (Windows, macOS, or Linux). Install the imager on your computer. 
Here's a link to download the imager for windows https://downloads.raspberrypi.org/imager/imager_latest.exe
And Mac https://downloads.raspberrypi.org/imager/imager_latest.dmg

b) Insert the SD card: 
Insert the SD card into your computer's SD card reader. 
If your pc doesn't have a sd card slot you might need a usb sd card adapter like this https://amzn.eu/d/9YCCNkn

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


a) Insert your SD and power up:
Insert you sd card into the slot underneath the Raspberry Pi, and connect the power supply to boot it up.

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

---
## [Step 3: Install Putty]

Now we are going 'Headless' which means operating the device without a dedicated monitor, keyboard, or mouse connected to it. Instead, you can access and control the Raspberry Pi remotely from another device, such as a computer or smartphone, using network protocols like SSH (Secure Shell) or VNC (Virtual Network Computing). This allows you to interact with and manage the Raspberry Pi without the need for physical peripherals directly connected to it, making it more convenient for certain use cases or environments.

a) Download PuTTY: 
Go to the PuTTY website (www.putty.org) and download the PuTTY installer for your operating system. Choose the appropriate installer based on your system architecture (32-bit or 64-bit). (Don't worry if you choose the wrong one as your pc will let you know)

b) Run the PuTTY installer: 
Double-click on the downloaded PuTTY installer file to run the installation wizard.

c) Follow the PuTTY installation steps: 
The installation wizard will guide you through the installation process. Accept the license agreement, choose the installation location, and select additional components if desired. Leave the default settings unless you have specific preferences.

d) Launch PuTTY: 
After the installation is complete, launch PuTTY from your Start menu or desktop shortcut.

e) Configure PuTTY for SSH connection:
In the PuTTY configuration window, enter the IP address of your Raspberry Pi running Volumio in the "Host Name (or IP address)" field.

f) Set the connection type: 
Make sure the connection type is set to "SSH."

g) Connect to Volumio: 
Click the "Open" button to initiate the SSH connection to your Raspberry Pi running Volumio.

h) Enter login credentials: 
When prompted, enter the login credentials for Volumio. By default, the username is "volumio," and the password is "volumio."

i) Begin using Volumio through SSH: 
Once successfully connected, you can use the command-line interface to control and configure Volumio.

That's it! You have now installed PuTTY and established an SSH connection to your Volumio instance running on the Raspberry Pi. You can now interact with Volumio headlessly using the PuTTY terminal on your PC.

---
## [Step 3: Install the main NR1-UI software]

a) Open PuTTY: 
Launch the PuTTY application on your computer (if its not already open)

b) Connect to your Raspberry Pi: 
Enter the IP address of your Raspberry Pi running Volumio in the "Host Name (or IP address)" field. Make sure the connection type is set to "SSH." Click the "Open" button to initiate the SSH connection.

c) Login: 
When prompted, enter the login credentials for Volumio. By default, the username is "volumio," and the password is "volumio."

e) Clone the repository: 
In the PuTTY terminal, copy and paste the 2 lines below and press Enter:

```
git clone http://github.com/theshepherdmatt/NR1-UI.git

bash NR1-UI/install.sh
```
This will take upto 40 - 50 minutes, so put the kettle on or walk the dog and let the pi do its thing.

![MS2501](https://github.com/Maschine2501/NR1-UI/blob/master/wiki/MadeByGloria.jpg)
[Logo made by glorious @Klassik_Otaku](http://www.instagram.com/klassik_otaku)

