#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from time import sleep
class RasPiBot:

   #=========================================================================
   # Setting up the servomotors
   #========================================================================
   HEAD = 0
   NECK = 1
   LEFT_SHOULDER = 2
   LEFT_BICEP = 3
   LEFT_WRIST = 4
   LEFT_HAND = 5
   LEFT_HIP = 6
   LEFT_KNEE = 7
   LEFT_ANKLE =8
   RIGHT_SHOULDER = 9
   RIGHT_BICEP = 10
   RIGHT_WRIST = 11
   RIGHT_HAND = 12
   RIGHT_HIP = 13
   RIGHT_KNEE = 14
   RIGHT_ANKLE = 15

   #when robot starts, each motor is set to 0 angle
   listAngle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

   #========================================================================
   # Setting up the 16 channels servos
   #=======================================================================
   pwm = PWM(0x40)
   #Note if you'd like more ouput you can instead run:
   #pwm = PWM(0x40,debug-=True)

   servoMin = 150
   servoMax = 600
   minAngle = -90
   maxAngle = 90
   pwm.setPWMFreq(50)

   @staticmethod
   def DegreesToPulseLength(degrees,in_min,in_max,out_min,out_max):
      return ((degrees - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

   def Rotate(self,servoNumber,angle):
      if(servoNumber < 0 or servoNumber > 15):
         print("Invalid servo number (0-15)")
      elif (angle <- 90 or angle > 90):
         print("Invalid rotation angle (-90 - 90")
      else:
         pulseLength = self.DegreesToPulseLength(angle+self.listAngle[servoNumber],self.minAngle,self.maxAngle,self.servoMin,self.servoMax)
         self.listAngle[servoNumber] = self.listAngle[servoNumber] + angle
         self.pwm.setPWM(servoNumber,50,pulseLength)

   def MoveTo(self, servoNumber, angle):
      if(servoNumber < 0 or servoNumber > 15):
         print("Invalid servo number (0-15)")
      elif (angle <-90 or angle > 90):
         print("Invalid angle (-90 - 90)")
      else:
         pulseLength = self.DegreesToPulseLength(angle, self.minAngle, self.maxAngle, self.servoMin, self.servoMax)
         self.listAngle[servoNumber] = angle
         self.pwm.setPWM(servoNumber,50,pulseLength)

#Example
#robot = RasPiBot()
#while True:
  # print("Wich motor do you want to move?")
  # motor = int(raw_input())
  # print("Rotation angle between -90 and 90:")
  # ang = int(raw_input())
  # robot.MoveTo(motor,ang)
  # robot.Rotate(motor,ang)


