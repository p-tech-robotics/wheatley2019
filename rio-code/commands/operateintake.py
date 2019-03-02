from wpilib.command import Command

class OperateIntake(Command):
  """
  Control intake using joystick or trigger
  """

  def __init__(self, robot):
    super().__init__()

    self.robot = robot

    self.requires(self.robot.intake)

  def initialize(self):
    """ called before cmd runs the first time """
    
  def execute(self):
    """ runs till it dont need to """
    self.robot.intake.set(self.robot.oi.getIntakeSpeed())

  def end(self):
    """ called once isFinished returns true """
    self.robot.intake.set(0)

  def interrupted(self):
    """ called once a subsystem command conflict occurs """
    self.end()
