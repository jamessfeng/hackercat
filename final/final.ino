#include <AFMotor.h>


#define SensorPin A0 
#define LDRPin A1


AF_DCMotor motor1(1);
int buttonPin = 2;
int buttonState = 0;
float rawValue = 0; 
int dryValue = 0;
int wetValue = 773;
int lowValue = 0; 
int highValue = 1023; 
int PercentageLowValue = 0;
int PercentageHighValue = 100;
int moistureLevel = 0; 
int sensorValue =0; 
int lightLevel = 0; 
int pwm = 2; 
int motorDrive = 6; // The output to the transistor that drives the motor
String str = "";

void setup() { 
 Serial.begin(9600); 
 Serial.println("CLEARDATA"); //clears up any data left from previous projects

Serial.println("LABEL,Time,Water,Sunlight"); //always write LABEL, so excel knows the next things will be the names of the columns (instead of Acolumn you could write Time for instance)

Serial.println("RESETTIMER"); //resets timer to 0

 motor1.setSpeed(255);
 pinMode(buttonPin, INPUT);

} 

void loop() { 
  
   rawValue =  analogRead(SensorPin); 
   moistureLevel= map(rawValue, dryValue, wetValue, PercentageLowValue, PercentageHighValue);

   sensorValue = analogRead(LDRPin); // read the value from the sensor
   lightLevel= map(sensorValue, lowValue, highValue, PercentageLowValue, PercentageHighValue);
   delay(1); 
   
    str = "DATA,TIME," + String(moistureLevel) + "," + String(lightLevel) + ",";
    Serial.println(str); //writes the time in the first column A and the time since the measurements started in column B
    delay(3000);
//    Serial.println("CLEARDATA"); //clears up any data left from previous projects
 
    
   buttonState = digitalRead(buttonPin);
  if(buttonState == HIGH){
    
      motor1.run(FORWARD);
      
      //Serial.println("Watering");
      delay(6000);
      motor1.run(RELEASE);
  }

} 
