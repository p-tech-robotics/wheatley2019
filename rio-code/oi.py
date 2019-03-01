import wpilib
from wpilib import shuffleboard
from wpilib.buttons import JoystickButton

from wpilib.shuffleboard import Shuffleboard as SB

from commands.drivebot import DriveBot
from commands.pop import Pop
from commands.operateintake import OperateIntake
from commands.circles import Circles

class OI:
  def __init__(self, robot):

    self.robot = robot
    self.xbox = wpilib.Joystick(0)

    self.l_trigger = self.xbox.getRawAxis(2)
    self.r_trigger = self.xbox.getRawAxis(3)

    self.l_bumper = JoystickButton(self.xbox, 6)
    self.r_bumper = JoystickButton(self.xbox, 5)

    self.a_button = JoystickButton(self.xbox, 1)
    
    self.steer = self.xbox.getRawAxis(0)
    self.speed = self.l_trigger - self.r_trigger

    
    self.l_bumper.whenPressed(Pop(self.robot))

    self.a_button.whenPressed(Circles(self.robot))

  def getSteer(self):
    return self.steer

  def getSpeed(self):
    return self.speed
