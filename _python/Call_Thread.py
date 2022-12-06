import Threads
import UI_Update
import General
import Functions


# call thread for motion control
def motion(self):
    General
    self.Motion_Thread = Threads.Motion()
    self.Motion_Thread.stop_motor.connect(lambda: Functions.disable_motor())
    self.Motion_Thread.started.connect(
        lambda: UI_Update.motion_control_frame_toggle(self)
    )

    self.Motion_Thread.finished.connect(
        lambda: UI_Update.motion_control_frame_toggle(self)
    )

    self.Motion_Thread.start()
