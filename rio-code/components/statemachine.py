import wpilib

from robotpy_ext.autonomous import StatefulAutonomous

class StateMachine(StatefulAutonomous):
  MODE_NAME = "Drive Forward"

  def initialize(self):
    pass

  '''
  # @timed_state(duration=0.5, next_state= 'next_state_name', first=True)
  def state_method_name(self, initial_call):
    pass
  '''




