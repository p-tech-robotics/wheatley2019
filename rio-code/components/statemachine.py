import wpilib

from robotpy_ext.autonomous import StatefulAutonomous

"""
\ r3l          | c3l       c3r |          r3r /
 |             | c2l       c2r |             |
 |  r2l        | c1l       c1r |       r2r   |
/ r1l          |   c0l   c0r   |          r1r \
               |-------|-------|

 ls_l                                      ls_r
---|---___________________________________--|--

"""





class StateMachine(StatefulAutonomous):
  MODE_NAME = "Drive Forward"

  def initialize(self):
    pass

  '''
  # @timed_state(duration=0.5, next_state= 'next_state_name', first=True)
  def state_method_name(self, initial_call):
    pass
  '''
  def teleop(self):

  def ls_a(self):
    """
    Go to loading station from cargo ship A
    """



