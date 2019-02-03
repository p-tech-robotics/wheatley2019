#!/usr/bin/env python3
"""
This is a demo program showing the use of the RobotDrive class,
specifically it contains the code necessary to operate a robot with
tank drive.
"""
import wpilib
from wpilib.drive import DifferentialDrive


class MyRobot(wpilib.TimedRobot):
  def robotInit(self):
    """Robot initialization function"""

    # object that handles basic drive operations
    self.frontLeftMotor = wpilib.Spark(2)
    self.rearLeftMotor = wpilib.Spark(4)
    self.frontRightMotor = wpilib.Spark(3)
    self.rearRightMotor = wpilib.Spark(5)

    self.left = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
    self.right = wpilib.SpeedControllerGroup(
      self.frontRightMotor, self.rearRightMotor
    )

    self.myRobot = wpilib.drive.DifferentialDrive(self.left, self.right)
    # joysticks 1 & 2 on the driver station
    self.stick = wpilib.Joystick(0)
    self.timer = wpilib.Timer()
  def autonomousInit(self):
    """Runs once each time bot enters auto mode"""
    self.timer.reset()
    self.timer.start()

  def teleopPeriodic(self):
    """Runs the motors with tank steering"""
    # exponential response
    # self.myRobot.arcadeDrive(self.stick.getRawAxis(1)**3, self.stick.getRawAxis(4)**3)
    # Linear Response
    self.myRobot.arcadeDrive(self.stick.getRawAxis(1), self.stick.getRawAxis(4))


if __name__ == "__main__":
  wpilib.run(MyRobot)
