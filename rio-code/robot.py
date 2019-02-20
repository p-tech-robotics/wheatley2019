import wpilib
from wpilib import TimedRobot, ArcadeDrive, DifferentialDrive, Spark, Joystick

from components import drive#, wrist, intake, popper, camera

class Wheatley(TimedRobot):
  def robotInit(self):
    """
    Init Robot
    """

    # Robot Components
    # Constructor params are PWM Ports on the RIO
    self.drive = drive.Drivetrain(0,1,2,3)
    #self.wrist = wrist.Wrist(4)
    #self.intake = intake.Intake(5)
    #self.popper = popper.Popper(1,2)

    self.xbox = Joystick(0)
    self.joystick = Joystick(1)

  def teleopInit(self):
    return NotImplemented

  def teleopPeriodic(self):
    return NotImplemented


if __name__ == '__main__':
  wpilib.run(Wheatley)

