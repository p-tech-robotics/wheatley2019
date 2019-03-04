from wpilib.command import Command

class Pop(Command):
  def __init__(self,robot):
    super().__init__()

    self.robot = robot

    self.requires(self.robot.popper)
    self.setTimeout(1)

  def initialize(self):
    """ called once when the command runs """

    self.robot.popper.set(True)

  def execute(self):
    """ runs repeatedly as long as cmd is cheduled to run"""
    pass

  def isFinished(self):
    """ returns true once it no longer needs to execute """
    return self.isTimedOut()

  def end(self):
    """ called after isFinished returns true """
    self.robot.popper.set(False)

  def interrupted(self):
    """ called when another command interrups this one """
    self.end()
