import wpilib
from wpilib import TimedRobot, Timer, Joystick, CameraServer, PowerDistributionPanel, DriverStation

from components import drive, wrist, popper, encoders, imu#, statemachine

class Wheatley(TimedRobot):
<<<<<<< HEAD
  kSpeedLim = 0.8
  kSteerLim = 0.75
=======
  kSpeedLimit = 0.8 # to prevent driver from tipping robot
  kAutoLimit = 0.2 # for testing only, can increase later if things look good
>>>>>>> eca0e92659d91e6e1a791099ccf239d74a943b61
  def robotInit(self):
    """
    Init Robot
    """

    # Robot Components
    # Constructor params are PWM Ports on the RIO
    self.drive = drive.Drivetrain(1,2,3,4)
<<<<<<< HEAD
    self.intake = intake.Intake(0)
    self.popper = popper.Popper(0,0)
=======
    self.intake = intake.Intake(5)
    self.popper = popper.Popper(1,0)
>>>>>>> eca0e92659d91e6e1a791099ccf239d74a943b61

    self.imu = imu.IMU(2)
    self.encoders = encoders.Encoders()

    self.xbox = Joystick(0)

    CameraServer.launch("components/camera.py:main")

    self.timer = Timer()
  
<<<<<<< HEAD

  def robotPeriodic(self):

    # speed = self.xbox.getRawAxis(1)
    speed = self.kSpeedLim*((self.xbox.getRawAxis(3) - self.xbox.getRawAxis(2))**3) #speed limited triggers with cubic feedback
    steer = self.kSteerLim*(self.xbox.getRawAxis(0)**3) # left stick x axis
    self.drive.drive.arcadeDrive(speed,
                                steer)


    # Popper (
    
    if self.xbox.getRawButton(5) == True:
      self.popper.extend()
    else:
      self.popper.retract()
    # Intake Code (Triggers)
    self.intake.set(self.xbox.getRawAxis(5))


=======
>>>>>>> eca0e92659d91e6e1a791099ccf239d74a943b61
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
<<<<<<< HEAD
  '''
=======
  def teleopPeriodic(self):
    """
    teleop code
    """
    #speed = xbox.getRawAxis(4)

    # triggers for speed, left stick for steer
    speed= self.kDriveMax*((xbox.getRawAxis(3) - getRawAxis(2))**3) # cubic response
    steer = self.getRawAxis(0)**3

    self.drive.drive.arcadeDrive(speed,
                                steer)


    # Popper (Left Bumper)
    self.popper.set(self.xbox.getRawButton(4))

    # Intake Code (Right Stick)
    self.intake.set(self.xbox.getRawAxis(5))


>>>>>>> eca0e92659d91e6e1a791099ccf239d74a943b61

if __name__ == '__main__':
  wpilib.run(Wheatley)


  print(r"""
   _____ ________ __ ______
  / ___// ____/ // /|__   /
 / __ \/___ \/ // /  /_  /
/ /_/ /___/ /__  _/___/ /       ____________________  __
\____/_____/__/_/______/_  ____/_  __/ ____/ ____/ / / /
   / __ \/ / / / __ `__ \/ __ `// / / __/ / /   / /_/ /
  / /_/ / /_/ / / / / / / /_/ // / / /___/ /___/ __  /
 / .___/\__,_/_/ /_/ /_/\__,_//_/ /_____/\____/_/ /_/
/_/        __               __  __              ___   ____ _______
 _      __/ /_  ___  ____ _/ /_/ /__  __  __   |__ \ / __ <  / __ \
| | /| / / __ \/ _ \/ __ `/ __/ / _ \/ / / /   __/ // / / / / /_/ /
| |/ |/ / / / /  __/ /_/ / /_/ /  __/ /_/ /   / __// /_/ / /\__, /
|__/|__/_/ /_/\___/\__,_/\__/_/\___/\__, /   /____/\____/_//____/
                                   /____/
  """)
