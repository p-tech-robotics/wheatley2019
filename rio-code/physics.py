import math

from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units

class PhysicsEngine(object):
  """
    Simulates drivetrain for pathfinder
  """

  def __init__(self, physics_controller):
    """
      :param physics_controller: 'pyfrc.physics.core.PhysicsInterface' object
                              to communicate sim effects
    """

    self.physics_controller = physics_controller

    # change these params to fit robot
    bumper_width = 3.25 * units.inch

    # fmt: off
    self.drivetrain = tankmodel.TankModel.theory(
            motor.cfgs.MOTOR_CFG_CIM,               # motor configuration
            110 * units.lbs,                        # robot mass
            10.75,                                  # gear ratio
            2,                                      # motors per side
            24* units.inch,                         # dist between wheelbase
            (28+6.5) * units.inch,                         # robot width
            (28+6.5) * units.inch,                         # robot length
            6 * units.inch
            )

    #fmt: on

  def update_sim(self, hal_data, now, tm_diff):
    """
        :param now: current time (float)
        :param tm_diff: delta_t
    """

    # simulate the drivetrain
    lr_motor = hal_data["pwm"][1]["value"]
    rr_motor = hal_data["pwm"][2]["value"]

    x, y, angle = self.drivetrain.get_distance(lr_motor, rr_motor, tm_diff)
    self.physics_controller.distance_drive(x, y, angle)
