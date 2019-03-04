import wpilib
from wpilib import Solenoid, DoubleSolenoid
from wpilib.command import Subsystem

class Climber(Subsystem):
  def __init__(self, can_id=0, channel_1=1, channel_2=2):
    super().__init__()

    self.solenoid = DoubleSolenoid(can_id, channel_1, channel_2)

  def set(self, state):
    self.solenoid.set(state)

  def extend(self):
    self.set(1)

  def retract(self):
    self.set(2)
