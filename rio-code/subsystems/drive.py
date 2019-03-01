import wpilib
from wpilib import Spark, SpeedControllerGroup
from wpilib.drive import DifferentialDrive

from wpilib.command import Subsystem
from commands import circles, drivebot

class Drivetrain(Subsystem):
  """
  Robot Drivetrain
  """
  def __init__(self, 
          robot,
      l_f_port=0,
      l_r_port=1,
      r_f_port=2,
      r_r_port=3):
    """
    Initialize ports for bot

    var naming scheme: (side)_(position)_(object), ex: l_f_port is left_front_port
    """
    super().__init__()
    self.robot = robot

    # Motors on Left Side
    self.l_f_motor = Spark(l_f_port)
    self.l_r_motor = Spark(l_r_port)

    # Motors on Right Side
    self.r_f_motor = Spark(r_f_port)
    self.r_r_motor = Spark(r_r_port)

    # Motor groups
    self.l_group = SpeedControllerGroup(self.l_f_motor, self.l_r_motor)
    self.r_group = SpeedControllerGroup(self.r_f_motor, self.r_r_motor)

    self.drive = DifferentialDrive(self.l_group, self.r_group)

  def initDefaultCommand(self):
    self.setDefaultCommand(drive_bot(self.robot))

  

