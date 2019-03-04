from wpilib.command import Command

class LiftFront(Command):
  def __init__(self,robot):
    super().__init__()

    self.robot = robot

    self.requires(self.robot.front_lift)
    self.setTimeout(1)

  def initialize(self):
    """ called once when the command runs """

    self.robot.front_lift.extend()

  def execute(self):
    """ runs repeatedly as long as cmd is cheduled to run"""
    pass

  def isFinished(self):
    """ returns true once it no longer needs to execute """
    return self.isTimedOut()

  def end(self):
    """ called after isFinished returns true """
    self.robot.front_lift.retract()

  def interrupted(self):
    """ called when another command interrups this one """
    self.end()

class LiftRear(Command):
  def __init__(self,robot):
    super().__init__()

    self.robot = robot

    self.requires(self.robot.rear_lift)
    self.setTimeout(1)

  def initialize(self):
    """ called once when the command runs """

    self.robot.rear_lift.extend()

  def execute(self):
    """ runs repeatedly as long as cmd is cheduled to run"""
    pass

  def isFinished(self):
    """ returns true once it no longer needs to execute """
    return self.isTimedOut()

  def end(self):
    """ called after isFinished returns true """
    self.robot.rear_lift.retract()

  def interrupted(self):
    """ called when another command interrups this one """
    self.end()
