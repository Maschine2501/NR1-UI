#!/bin/bash
echo "___________________________________________________________________ " #
echo " " #
echo " " #
echo "___________________________________________________________________ " #
echo "If you have noticed a Latency between Audio and Spectrum on Screen," #
echo "you can change it here." #
echo "___________________________________________________________________ " #
echo " " #
echo " " #
echo "_____________________________ " #
echo "The Value is in nano seconds." #
echo "1000000 nano seconds = 1 sec"
echo "500000 is the default value..." #
echo " "
echo "_____________________"
echo "Valid selections are: " #
echo "1 -> Yes" #
echo "2 -> No" #
echo "---> " #
echo " " #
getBuffertime() {#
  echo " "
  echo "_________________________________ "   
  echo "Remember: These are nano Seconds! "  
  echo "_________________________________ "  
  echo ""  
  read -p "Please enter a value between 10000 and 9999999:" BufferT #
  case "$BufferT" in
    [1-9][0-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9][0-9][0-9])
      cd /etc
      sed -i '60i\                buffer_time     "'""$bufferT""'"' mpd.conf
      echo " "
      echo -n "Set Buffer-Time to "; echo -n "${BufferT} "; echo -n "nano-seconds" #
      return 0
      ;;
    *)
      printf %s\\n "Please enter a number between '10000' and '9999999'"
      return 1
      ;;
  esac
}
getBuffertimeActive() {
  read -p "Do you want to change the Buffer-Time?" BufferActive #
  case "$BufferActive" in
    1)
      until getBuffertime; do : ; done  
      echo " "
      return 0
      ;;
    2)
      echo " "
      echo " "
      echo "Buffer-Time was not activated.."
      echo " "
      echo " "
      return 0
      ;;
    *)
      printf %s\\n "Please enter a number between '1' and '2'"
      return 1
      ;;
  esac
}
until getBuffertimeActive; do : ; done

echo " " #
echo " " #
sudo service mpd restart