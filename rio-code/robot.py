import wpilib
from wpilib import TimedRobot, ArcadeDrive, DifferentialDrive, Spark

from components import drive, wrist, intake, popper

class Wheatley(TimedRobot):
  def robotInit(self):
    # Initialize components
    # Constructor params are PWM Ports on the RIO
    self.drive = drive.Drivetrain(0,1,2,3)
    self.wrist = wrist.Wrist(4)
    self.intake = intake.Intake(5)
    self.popper = popper.Popper(1,2)

  def



if __name__ == '__main__':
  wpilib.run(Wheatley)

