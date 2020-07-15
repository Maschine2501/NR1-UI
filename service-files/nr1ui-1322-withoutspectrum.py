[Unit]
Description=NR1-UI-1322-withoutspectrum
 
[Service]
Type=simple
WorkingDirectory=/home/volumio
ExecStart=/usr/local/bin/python3 -u /home/volumio/NR1-UI/nr1ui-1322-withoutspectrum.py
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=nr1ui-1322-withoutspectrum
User=volumio
Group=volumio
 
[Install]
WantedBy=multi-user.target
