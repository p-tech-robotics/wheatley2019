import wpilib
from magicbot import MagicRobot

#from components.component1 import Component1

from components import Wrist, Intake, Popper

clas MyRobot(MagicRobot):
  #component1 = Component1

  k_constant = 1

  def createObjects(self):
    """Initialize all motors and sensors"""

    self.component1_motor = wpilib.Spark(1)
    self.component2


  def teleopInit(self):
    """called when teleop starts"""

  def teleopPeriodic(self):
    """called on each iteration of teleop loop"""


if __name__ == '__main__':
  wpilib.run(MyRobot)

