//   ____    ____   ______    _____   _______     ____    __    
//  |_   \  /   _|.´ ____ \  / ___ `.|  _____|  .'    '. /  |   
//    |   \/   |  | (___ \_||_/___) || |____   |  .--.  |`| |   
//    | |\  /| |   _.____'.  .'____.''_.____''.| |    | | | |   
//   _| |_\/_| |_ | \____\ \/ /_____ | \____) ||  `--'  |_| |_  
//  |_____||_____| \_______||_______| \______.' '.____.'|_____| 
//
//   www.github.com/Maschine2501                                                            
//
//   ATTINY85 <-> RaspberryPI StandBy-Logic
//   For more Informations visit: https://github.com/Maschine2501/NR1-UI
//

int Relais = 0;                            // PB0 -> connected to base of BC548 (circuit under: www.github.com/Maschine2501/NR1-UI/wiki/ )
int PiStatusSend = 1;                      // PB1 -> connected to pin 37 (GPIO26) @ raspberry
int Button = 2;                            // PB2 -> connected to powerbutton (other side +5V)
int PiStatusReceive = 4 ;                  // PB4 -> connected to pin 33 (GPIO13) @ raspberry

// Start Variables:
boolean PRS = LOW;                         // Previous state of therelais
boolean NRS = LOW;                         // New state of the relais
boolean RS = LOW;                          // Actuall state of the relais
boolean PS = LOW;                          // Actuall state of the raspberry
boolean PPS = LOW;                         // Previous state of the raspberry
boolean NPS = LOW;                         // New state of the raspberry


void setup()
{
  pinMode(Relais, OUTPUT);                                                                                                                                                                                                                                                                                                                                                                                                                  
  digitalWrite(Relais, LOW);

  pinMode(PiStatusSend, OUTPUT);
  digitalWrite(PiStatusSend, LOW);

  pinMode(Button, INPUT);

  pinMode(PiStatusReceive, INPUT);
}

void loop()
{
  NRS = digitalRead(Button);
  
  NPS = digitalRead(PiStatusReceive);
  
  if ( NRS != PRS || NPS != PPS )
  {
    if ( NRS == HIGH || NPS == LOW )
    {
      if ( RS == LOW ) {                         // Start Point -> Everything is off/low -> button is pressed
        digitalWrite(Relais, HIGH);              // Set Relais HIGH
        digitalWrite(PiStatusSend, HIGH);        // Set PiStatusSend HIGH
        delay(80000);                            // wait 80sec for pi to boot
        RS = HIGH; 
      }
      else if ( NPS == LOW ){                    // if Relais is on and pi signal is low (pi is shutdown)
        delay(30000);                            // wait 30sec for pi to boot
        NPS = digitalRead(PiStatusReceive);      // check aggain if pi is off
        if ( NPS == LOW ) {
          digitalWrite(PiStatusSend, LOW);       // Set PiStatusSend LOW
          digitalWrite(Relais, LOW);             // Set Relais LOW
          RS = LOW;
          PS = LOW; 
        }
        else {
          PS = HIGH; 
        }
      }
      else {                                     // If PI an Relais is on and Button is pressed.
        digitalWrite(PiStatusSend, LOW);         // Set PiStatusSend LOW
        delay(30000);                            // wait 30 Sec to shutdown all services on your Pi
        if ( NPS == LOW ) {
          digitalWrite(Relais, LOW);             // Set Relais LOW
          RS = LOW;
          PS = LOW; 
        }
        else {
          PS = HIGH; 
        }
      }
      
    }
    PRS = NRS;
    PPS = NPS;
  }
}
