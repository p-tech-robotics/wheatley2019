import wpilib
from wpilib import Spark
from wpilib.command import Subsystem

from commands.operateintake import OperateIntake

class Intake(Subsystem):
  """
  cargo intake
  """

  def __init__(self, port, robot):
    super().__init__()
    self.motor = Spark(port)
    self.robot = robot

  def set(self, speed):
    """
    Sets motor speed (float val [-1,1])
    """
    self.motor.set(speed)

  def up(self):
    self.set(1)

  def down(self):
    self.set(-1)

  def stop(self):
    self.set(0)
  
  def initDefaultCommand(self):
    self.setDefaultCommand(OperateIntake(self.robot))

