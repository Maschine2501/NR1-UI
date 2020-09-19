#!/bin/bash
echo "audio_output {" >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo '    type     "fifo"' >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo '    name     "my_fifo"' >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo '    path     "/tmp/mpd.fifo"' >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo '    format   "44100:16:2"' >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo "}" >> /etc/mpd.conf
echo "audio_output {" >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo '    type     "fifo"' >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo '    name     "my_fifo2"' >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo '    path     "/tmp/mpd2.fifo"' >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo '    format   "44100:16:2"' >> /etc/mpd.conf
echo " " >> /etc/mpd.conf
echo "}" >> /etc/mpd.conf
echo " " #
echo " " #
echo "Fifo-Audio-Outputs for Cava has been added to mpd.conf" #
echo " " #
echo " " #
sudo service mpd restart