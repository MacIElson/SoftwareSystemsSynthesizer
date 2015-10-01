//Sine out w/ 40kHz sampling rate
//by Amanda Ghassaei
//http://www.instructables.com/id/Arduino-Audio-Output/
//Sept 2012

/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
*/

#ifndef cbi // Definitions for setting and clearing register bits
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

byte sine[] = {127, 134, 142, 150, 158, 166, 173, 181, 188, 195, 201, 207, 213, 219, 224, 229, 234, 238, 241, 245, 247, 250, 251, 252, 253, 254, 253, 252, 251, 250, 247, 245, 241, 238, 234, 229, 224, 219, 213, 207, 201, 195, 188, 181, 173, 166, 158, 150, 142, 134, 127, 119, 111, 103, 95, 87, 80, 72, 65, 58, 52, 46, 40, 34, 29, 24, 19, 15, 12, 8, 6, 3, 2, 1, 0, 0, 0, 1, 2, 3, 6, 8, 12, 15, 19, 24, 29, 34, 40, 46, 52, 58, 65, 72, 80, 87, 95, 103, 111, 119,};
int notes[] = {50,110,120,130,140,150,160,170,255};

int t = 0;//time

int j = 0;

long previousMillis = 0; 
unsigned long currentMillis = 0;

long interval = 1000;//

void setup(){
  //set digital pins 0-7 as outputs
  for (int i=0;i<8;i++){
    pinMode(i,OUTPUT);
  }
  
  cli();//disable interrupts
  //set timer0 interrupt at 40kHz
  TCCR2A = 0;// set entire TCCR0A register to 0
  TCCR2B = 0;// same for TCCR0B
  TCNT2  = 0;//initialize counter value to 0
  // set compare match register for 40khz increments
  OCR2A = 200;// = (16*10^6) / (40000*8) - 1 (must be <256)
  // turn on CTC mode
  TCCR2A |= (1 << WGM21);
  // Set CS11 bit for 8 prescaler
  TCCR2B |= (1 << CS21); 
  // enable timer compare interrupt
  TIMSK2 |= (1 << OCIE2A);
  sei();//enable interrupts
  
}


ISR(TIMER2_COMPA_vect){ //40kHz interrupt routine
  PORTD = sine[t];//send sine wave to DAC, centered around (127/255)*5 = 2.5V
  t++;//increment t
  if (t > 99){//reset t to zero
    t = 0;
  }
}

void loop(){
  
  currentMillis = millis();
 
  if(currentMillis - previousMillis > interval) {
 
    // save the last time you blinked the LED
 
    previousMillis = currentMillis;
  
    //cbi(TCCR1A,COM0A1) ; // disconnect pulse clock
    OCR2A = notes[j];   // update timer value
    //sbi(TCCR1A,COM0A1) ; // connect pulse clock
   
    j++;//increment i
    if (j > 8){//reset i to zero
      j = 0;
    }
  }


}


