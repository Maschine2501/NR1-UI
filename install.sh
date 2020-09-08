#!/bin/bash
set +e #
cd #
echo "configuring Config.txt"
sudo cp /home/volumio/NR1-UI/config/config.txt /boot/ #
echo "Installing Python 3.5.2 and dependencies"
sudo apt-get update #
sudo apt-get install -y build-essential libc6-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev #
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz #
tar -zxvf Python-3.5.2.tgz #
cd Python-3.5.2 #
./configure && make -j4 && sudo make install #
cd #
alias python3=python3.5 #
echo "Updating default pip installation"
sudo pip3 install -U pip #
sudo pip3 install -U setuptools #
echo "installing all other dependencies" #
sudo apt-get install -y python3-dev python3-setuptools python3-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio libffi-dev libcurl4-openssl-dev libssl-dev git-core autoconf make libtool libfftw3-dev libasound2-dev libncursesw5-dev libpulse-dev libtool #
sudo pip3 install --upgrade setuptools pip wheel #
sudo pip3 install --upgrade luma.oled #
sudo pip3 install psutil socketIO-client pcf8574 pycurl gpiozero readchar numpy #
echo "Installing Cava(1)"
git clone https://github.com/Maschine2501/cava.git #
cd cava #
sudo bash autogen.sh #
./configure && make -j4 && sudo make install #
cd #
echo "Copying mpd.conf"
echo "# Volumio MPD Configuration File
# Files and directories #######################################################
music_directory		"/var/lib/mpd/music"
playlist_directory		"/var/lib/mpd/playlists"
db_file			"/var/lib/mpd/tag_cache"
log_file			"/var/log/mpd.log"
#pid_file			"/var/run/mpd/pid"
#state_file			"/var/lib/mpd/state"
#sticker_file                   "/var/lib/mpd/sticker.sql"
###############################################################################
# General music daemon options ################################################
user				"mpd"
group                          "audio"
bind_to_address		"any"
#port				"6600"
#log_level			"default"
gapless_mp3_playback			"no"
#save_absolute_paths_in_playlists	"no"
#metadata_to_use	"artist,album,title,track,name,genre,date,composer,performer,disc"
auto_update    "yes"
#auto_update_depth "3"
###############################################################################
# Symbolic link behavior ######################################################
follow_outside_symlinks	"yes"
follow_inside_symlinks		"yes"
###############################################################################
# Input #######################################################################
#
input {
        plugin "curl"
#       proxy "proxy.isp.com:8080"
#       proxy_user "user"
#       proxy_password "password"
}
###############################################################################
# Decoder ################################################################
###############################################################################
# Audio Output ################################################################
resampler {      
  		plugin "soxr"
  		quality "high"
  		threads "1"
}
audio_output {
		type		"alsa"
		name		"alsa"
		device		"hw:1,0"
                buffer_time     "1200000"
		dop			"no"
}
audio_output {
    type            "fifo"
    enabled         "no"
    name            "multiroom"
    path            "/tmp/snapfifo"
    format          "44100:16:2"
}
#replaygain			"album"
#replaygain_preamp		"0"
volume_normalization		"no"
###############################################################################
# MPD Internal Buffering ######################################################
audio_buffer_size		"2048"
buffer_before_play		"10%"
###############################################################################
# Resource Limitations ########################################################
#connection_timeout		"60"
max_connections			"20"
max_playlist_length		"81920"
max_command_list_size		"81920"
max_output_buffer_size		"81920"
###############################################################################
# Character Encoding ##########################################################
filesystem_charset		"UTF-8"
id3v1_encoding			"UTF-8"
###############################################################################
audio_output {
    type     "fifo"
    name     "my_fifo"
    path     "/tmp/mpd.fifo"
    format   "44100:16:2"
}
audio_output {
    type     "fifo"
    name     "my_fifo2"
    path     "/tmp/mpd2.fifo"
    format   "44100:16:2"
}" > /etc/mpd.conf #
cd #
echo "Installing Cava 2 (used for loudness-graph)"
git clone https://github.com/Maschine2501/cava.git /home/volumio/CAVAinstall #
cd /home/volumio/CAVAinstall #
sudo bash ./autogen.sh #
./configure --prefix=/home/volumio/CAVA2 && make -j4 && sudo make install #
cd #
echo "installing NR1-UI..."
#git clone https://github.com/Maschine2501/NR1-UI.git /home/volumio/NR1-UI #
chmod +x /home/volumio/NR1-UI/nr1ui.py #
#sudo chmod 777 /home/volumio/NR1-UI-Plugin
#sudo chmod 777 /home/volumio/NR1-UI/
sudo cp /home/volumio/NR1-UI/service-files/nr1ui.service /lib/systemd/system/ #
sudo cp /home/volumio/NR1-UI/service-files/cava1.service /lib/systemd/system/ #
sudo cp /home/volumio/NR1-UI/service-files/cava2.service /lib/systemd/system/ #
sudo systemctl daemon-reload #
sudo systemctl enable nr1ui.service #
sudo systemctl enable cava1.service #
sudo systemctl enable cava2.service #
#sudo chmod 777 /home/volumio/NR1-UI-Plugin
#sudo chmod 777 /home/volumio/NR1-UI
echo " "
echo " "
echo "Installation has finished, congratulations!"
echo " "
echo " "
echo "Please restart MPD and reboot your device after!!!"
echo " "
echo "use:"
echo " "
echo "sudo service mpd restart"
echo " "
echo "sudo reboot"
echo " "
echo " "
echo " "
exit 0
