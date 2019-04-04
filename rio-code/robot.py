import wpilib
from wpilib import Timer, Joystick, CameraServer, PowerDistributionPanel, DriverStation
from commandbased import CommandBasedRobot
from subsystems import drive, intake, popper, encoders, imu, lift#, statemachine

import math

from oi import OI

class Wheatley(CommandBasedRobot):

  def robotInit(self):
    """
    Init Robot
    """

    # Robot Components
    # Constructor params are PWM Ports on the RIO
    self.drivetrain = drive.Drivetrain(self, 1,2,3,4)
    self.intake = intake.Intake(0, self)
    self.popper = popper.Popper(0,0)
    
    self.front_lift = lift.Lift(0,1,2)
    self.rear_lift = lift.Lift(0,5,4)
    
    self.imu = imu.IMU(2)
    self.encoders = encoders.Encoders()

    CameraServer.launch("subsystems/camera.py:main")
    self.oi = OI(self) 

    
    #self.drivecommand = DriveCommandGroup()
    
    self.timer = Timer()
    
  
  def autonomousInit(self):
    """
    Runs one time whenever the bot enters auto mode
    """
    #self.drivecommand.start()

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
