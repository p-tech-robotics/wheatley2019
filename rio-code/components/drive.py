import wpilib
from wpilib import Spark

class Drivetrain:
  """
  Robot Drivetrain
  """
  def __init__(self,
      l_f_port=0,
      l_r_port=1,
      r_f_port=2,
      r_r_port=3):
    """
    Initialize ports for bot

    var naming scheme: (side)_(position)_(object), ex: l_f_port is left_front_port
    """

    # Motors on Left Side
    l_f_motor = Spark(l_f_port)
    f_r_motor = Spark(l_r_port)

    # Motors on Right Side
    r_f_motor = Spark(r_f_port)
    r_r_motor = Spark(r_r_port)

    # Motor groups




