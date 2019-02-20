import wpilib
from wpilib import TimedRobot, Timer, ArcadeDrive, DifferentialDrive, Spark, Joystick

from components import drive, wrist, intake#, popper, camera

class Wheatley(TimedRobot):
  def robotInit(self):
    """
    Init Robot
    """

    # Robot Components
    # Constructor params are PWM Ports on the RIO
    self.drive = drive.Drivetrain(0,1,2,3)
    self.wrist = wrist.Wrist(4)
    self.intake = intake.Intake(5)
    #self.popper = popper.Popper(1,2)

    self.xbox = Joystick(0)
    self.joystick = Joystick(1)

    self.timer = Timer()

  def autonomousInit(self):
    """
    Runs one time whenever the bot enters auto mode
    """
    self.timer.reset()
    self.timer.start()



  def autonomousPeriodic(self):
    """
    loops during auto period
    """
    teleopPeriodic() # TODO: remove soon once auto code works


  def teleopPeriodic(self):
    self.drive.drive.ArcadeDrive(self.xbox.getRawAxis(1),
                                self.xbox.getRawAxis(4))


    # bumpers control wrist/popper
    if self.xbox.getRawButton(5):
      self.wrist.up()
    elif self.xbox.getRawButton(6):
      self.wrist.down()
    else:
      self.wrist.stop()

    # Popper (
    self.popper.set(self.xbox.getRawButton(5))

    # Intake Code (Triggers)
    self.intake.set(self.xbox.getRawAxis(2) + (-1.0 * self.xbox.getRawAxis(3)))


if __name__ == '__main__':
  wpilib.run(Wheatley)

