#include <ros.h>
#include "geometry_msgs/Twist.h" 
#include <std_msgs/Int16.h>
#include <std_msgs/String.h>

int ledPin = 13;
int buttom_red_right = 7;
int buttom_green_left = 6;
int buttom_green_change = 5;

ros::NodeHandle  nh;
std_msgs::Int16 sensorData;
std_msgs::Int16 cmdBTN;
std_msgs::Int16 motion;
geometry_msgs::Twist msg;



void control_LED( const std_msgs::Int16& cmd_msg)
{
  int value = cmd_msg.data;
  digitalWrite(ledPin, value);   // blink the led
}
ros::Subscriber<std_msgs::Int16> ledsub("Topic_LED_13", &control_LED );
ros::Publisher Status("Status",&motion);

void setup() 
{
  pinMode(ledPin, OUTPUT);
  pinMode(buttom_red_right,INPUT);
  pinMode(buttom_green_change,INPUT);
  pinMode(buttom_green_left,INPUT);
  digitalWrite(ledPin, 1); 
  nh.initNode();
  nh.subscribe(ledsub);
  nh.advertise(Status);
}
int mode=0;
void loop() 
{
  int BTN1 = digitalRead(buttom_red_right);
  int BTN2 = digitalRead(buttom_green_left);
  int BTN3 = digitalRead(buttom_green_change);
  int sensorData;
  if (BTN3 == 0)
  {
    mode=~mode;
  }
  if(BTN1==0&&BTN2==0)
  {
    if(mode == 0)
    {
      motion.data = 1;
      Status.publish(&motion);
      delay(100);
    }
    else
    {
      motion.data = 2;
      Status.publish(&motion);
      delay(100);
    }
  }
  else if (BTN2==0)
  {
    motion.data = 3;
    Status.publish(&motion);
    delay(100);
  }
  else if (BTN1==0)
  {
    motion.data = 4;
    Status.publish(&motion);
    delay(100);
  }
  nh.spinOnce();
  delay(1);
}
