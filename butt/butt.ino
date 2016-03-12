#include <Wire.h>
#include "MMA7660.h"
MMA7660 accelemeter;

const int butt1 = 2;
const int butt2 = 3;
const int butt3 = 4;

int buttState1 = 0;
int buttState2 = 0;
int buttState3 = 0;

void setup()                    
{
   //accelemeter.init();
   Serial.begin(9600);
   pinMode(butt1, INPUT);
   pinMode(butt2, INPUT);
   pinMode(butt3, INPUT);
}

void loop()                    
{
    //long start = millis();

    //Serial.println(millis() - start);        // check on performance in milliseconds
    buttState1 = digitalRead(butt1);
    buttState2 = digitalRead(butt2);
    buttState3 = digitalRead(butt3);
    
    if (buttState1==HIGH){
      Serial.print("1");
    }else{
      Serial.print("0");
    }
    
    if (buttState2==HIGH){
      Serial.print("1");
    }else{
      Serial.print("0");
    }
    
    if (buttState3==HIGH){
      Serial.print("1");
    }else{
      Serial.print("0");
    }
    
    //int8_t x;
    //int8_t y;
    //int8_t z;
    //float ax,ay,az;
    //accelemeter.getXYZ(&x,&y,&z);
    
    //Serial.print("x = ");
    //Serial.println(x); 
    //Serial.print("y = ");
    //Serial.println(y);   
    //Serial.print("z = ");
    //Serial.println(z);
  	
    //accelemeter.getAcceleration(&ax,&ay,&az);
  
    // delay(10);                             // arbitrary delay to limit data to serial port 
}

