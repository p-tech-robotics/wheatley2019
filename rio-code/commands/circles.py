from wpilib.command import Command

class Circles(Command):
  """
  Robot go sicko mode (drives in circles)
  """

  def __init__(self, robot):
    super().__init__()

    self.robot = robot
    self.requires(self.robot.drivetrain)
    self.setTimeout(10)

  def initialize(self):
    """ Called before command runs the first time"""

  def execute(self):
    """Calls repeatedly when cmd is scheduled to run"""
    self.robot.drivetrain.drive.arcadeDrive(0, 0.5)


  def isFinished(self):
    """make this return true when command no longer needs to run execute() """
    return self.isTimedOut() # runs until interrupted

  def end(self):
    """called once isFinished returns true"""
    self.robot.drivetrain.drive.arcadeDrive(0,0)

  def interrupted(self):
      """ called when another command required the same subsystems are scheduled to run"""
      self.end()