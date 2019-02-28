import wpilib
from wpilib import TimedRobot, Timer, Joystick, CameraServer, PowerDistributionPanel, DriverStation

from components import drive, wrist, intake, popper, encoders

class Wheatley(TimedRobot):
  kSpeedLim = 0.8
  def robotInit(self):
    """
    Init Robot
    """

    # Robot Components
    # Constructor params are PWM Ports on the RIO
    self.drive = drive.Drivetrain(1,2,3,4)
    self.wrist = wrist.Wrist(0)
    self.intake = intake.Intake(5)
    self.popper = popper.Popper(0,0)

    self.encoders = encoders.Encoders()

    self.xbox = Joystick(0)
    self.joystick = Joystick(1)

    CameraServer.launch("components/camera.py:main")

    self.timer = Timer()
  

  def robotPeriodic(self):

    # speed = self.xbox.getRawAxis(1)
    speed = self.kSpeedLim*((self.xbox.getRawAxis(3) - self.xbox.getRawAxis(2))**3) #speed limited triggers with cubic feedback
    steer = self.xbox.getRawAxis(0) # left stick x axis
    self.drive.drive.arcadeDrive(speed,
                                steer)


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
    self.intake.set(self.xbox.getRawAxis(5))


  def autonomousInit(self):
    """
    Runs one time whenever the bot enters auto mode
    """
    self.timer.reset()
    self.timer.start()

  '''
  def autonomousPeriodic(self):
    """
    loops during auto period
    """

    self.teleopPeriodic() # TODO: remove soon once auto code works
  '''

if __name__ == '__main__':
  wpilib.run(Wheatley)

