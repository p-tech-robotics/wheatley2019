from ctre.pigeonimu import PigeonIMU

class IMU:
  def __init__(self, can_id):
    imu = PigeonIMU(can_id)

  def getHeading(self):
    return self.imu.getYawPitchRoll()[0] # gets yaw

  @property
  def getYPR(self):
    """
    returns [yaw, pitch, roll]
    """
    #return self.imu.getYawPitchRoll()
    return self.imu.getFusedHeading()["heading"]

  # getfusedheading
