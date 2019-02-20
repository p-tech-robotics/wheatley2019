import wpilib
from wpilib import Spark

class Wrist:
  """
  Backup mech for hatch panels
  """

  def __init__(self, port):
    self.motor = Spark(port)

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


