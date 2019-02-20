import wpilib
from wpilib import Solenoid, DoubleSolenoid

class Popper:
  def __init__(self, can_id=0, channel=0):
    self.solenoid = Solenoid(can_id, channel)

  def set(self, state):
    self.solenoid.set(state)

  def extend(self):
    self.set(True)

  def retract(self):
    self.set(False)
