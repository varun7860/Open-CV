#include<Servo.h>

////////////////Initialise Pot Variables//////////////////
int base_pot = A0;
int shoulder_pot = A1;
int wrist_pot = A2;
int gripper_pot = A3;

int pos1;
int pos2;
int pos3;
int pos4;

int a_pos;
int b_pos;
int c_pos;
int d_pos;

int minimum=0;
int maximum =180;
/////////////////////////End//////////////////////////////

///////////////////Objects Of Servo Motors///////////////
Servo base_servo;
Servo shoulder_servo;
Servo wrist_servo;
Servo gripper_servo;
///////////////////////////////End/////////////////////////


void setup() 
{
  Serial.begin(9600);

  base_servo.attach(3);
  shoulder_servo.attach(5);
  wrist_servo.attach(6);
  gripper_servo.attach(9);

  pinMode(base_pot,INPUT);
  pinMode(shoulder_pot,INPUT);
  pinMode(wrist_pot,INPUT);
  pinMode(gripper_pot,INPUT);

  base_servo.write(90);
  shoulder_servo.write(90);
  wrist_servo.write(90);
  gripper_servo.write(70);
  
}

void loop() 
{
  pos1=analogRead(A0);
  a_pos=map(pos1,0,1024,minimum,maximum);
  base_servo.write(a_pos);
  Serial.println(a_pos);
  
  pos2=analogRead(A1);
  b_pos=map(pos2,0,1024,minimum,maximum);
  shoulder_servo.write(b_pos);
  
  pos3=analogRead(A2);
  c_pos=map(pos3,0,1024,minimum,maximum);
  wrist_servo.write( c_pos);
  Serial.println(c_pos);
  
  pos4=analogRead(A3);
  d_pos=map(pos4,0,1024,minimum,maximum);
  gripper_servo.write(d_pos);
  Serial.println(d_pos);
}
