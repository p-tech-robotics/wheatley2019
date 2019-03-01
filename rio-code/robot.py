import wpilib
from wpilib import TimedRobot, Timer, Joystick, CameraServer, PowerDistributionPanel, DriverStation

from components import drive, intake, wrist, popper, encoders, imu#, statemachine

import math
def circles(self):
  self.drive.drive.arcadeDrive(0, -0.3)

class Wheatley(TimedRobot):
  kSpeedLim = 0.8
  kSteerLim = 0.75

  state = 1
  circles = circles

  def robotInit(self):
    """
    Init Robot
    """

    # Robot Components
    # Constructor params are PWM Ports on the RIO
    self.drive = drive.Drivetrain(1,2,3,4)
    
    self.intake = intake.Intake(0)
    self.popper = popper.Popper(0,0)

    self.imu = imu.IMU(2)
    self.encoders = encoders.Encoders()

    self.xbox = Joystick(0)

    CameraServer.launch("components/camera.py:main")
    
    self.shuffleboard()
    #self.myBoolean.value = True
    self.timer = Timer()
    self.statemachine = {
          0: self.teleopRobot(),
          1: self.circles(),
          }
    
    self.turnBool = False
  
  def shuffleboard(self):
    '''
    NetworkTables.initialize(server='roborio-6543-frc.local')
    
    self,sd = NetworkTables.getTable('SmartDashboard')
    sd.putBool = ("Teleop", False)
    sd.putBool = ("Teleop", False)
    self.tab = Shuffleboard.getTab("Wheatley 2019")
    '''

    self.booleanTest = (wpilib.shuffleboard.Shuffleboard.getTab("test tab")
            .add(title="testbool", value=False)
            .withWidget("Toggle Button")
            .getEntry()
            )
    
    self.camera1  = (wpilib.shuffleboard.Shuffleboard.getTab("test tab")
            .add(title="camera 1", value=0)
            .withWidget(wpilib.shuffleboard.BuiltInWidgets.kCameraStream)
            .getEntry()
            )
    
    self.camera2  = (wpilib.shuffleboard.Shuffleboard.getTab("test tab")
            .add(title="camera 2", value=1)
            .withWidget(wpilib.shuffleboard.BuiltInWidgets.kCameraStream)
            .getEntry()
            )
  def stateSelector(self):
    """
    selects robot state, overrides if "a" button is pressed on the
    """
    if self.xbox.getRawButton(0) == True:
        self.state = 0 
    else if self.booleanTest.value == True:
        self.state = 1

  def robotPeriodic(self):
    #self.teleopRobot()
    self.stateSelector()
    self.booleanTest.setBoolean(False)
    self.statemachine[self.state]

  def circles(self):
      self.drive.drive.arcadeDrive(0, 0.5)

  def teleopRobot(self):
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


  def autonomousInit(self):
    """
    Runs one time whenever the bot enters auto mode
    """
    self.timer.reset()
    self.timer.start()

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
