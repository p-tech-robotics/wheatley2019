import math

from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units

class PhysicsEngine(object):
  """
    Simulates drivetrain for pathfinder
  """

  def __init__(self, phys_controller):
    """
      :param phys_controller: 'pyfrc.physics.core.PhysicsIntergace' object
                              to communicate sim effects
    """

    self.phys_controller = phys_controller
    self.pos = 0


    # change these params to fit robot
    bumper_width = 3.25 * units.inch
