from wpilib.command import Command

class DriveBot(Command):
  """
  Arcade Drive with Xbox Controller
  """

  def __init__(self, robot):
    super().__init__()

    self.robot = robot
    self.requires(self.robot.drivetrain)

  def initialize(self):
    """ Called before command runs the first time"""

  def execute(self):
    """Calls repeatedly when cmd is scheduled to run"""
    self.robot.drivetrain.drive.arcadeDrive(self.robot.oi.getSteer(), self.robot.oi.getSpeed())


  def isFinished(self):
    """make this return true when command no longer needs to run execute() """
    return False # runs until interrupted

  def end(self):
    """called once isFinished returns true"""
    self.robot.drivetrain.drive.arcadeDrive(0,0)

  def interrupted(self):
      """ called when another command required the same subsystems are scheduled to run"""
      self.end()
