import Threads
import UI_Update
import General
import Functions


# call thread for motion control
def motion(self):
    General
    self.motion_Thread = Threads.Motion()
    self.motion_Thread.stop_motor.connect(lambda: Functions.disable_motor())
    self.motion_Thread.started.connect(
        lambda: UI_Update.motion_control_frame_toggle(self)
    )

    self.motion_Thread.finished.connect(
        lambda: UI_Update.motion_control_frame_toggle(self)
    )

    self.motion_Thread.start()
