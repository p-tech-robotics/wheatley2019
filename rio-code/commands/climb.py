from wpilib.command import Command

class LiftFront(Command):
  def __init__(self,robot):
    super().__init__()

    self.robot = robot

    self.requires(self.robot.front_climber)
    self.setTimeout(1)

  def initialize(self):
    """ called once when the command runs """

    self.robot.front_climber.extend()

  def execute(self):
    """ runs repeatedly as long as cmd is cheduled to run"""
    pass

  def isFinished(self):
    """ returns true once it no longer needs to execute """
    return self.isTimedOut()

  def end(self):
    """ called after isFinished returns true """
    self.robot.front_climber.retract()

  def interrupted(self):
    """ called when another command interrups this one """
    self.end()
