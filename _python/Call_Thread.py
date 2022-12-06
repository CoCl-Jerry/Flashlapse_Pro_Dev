import Threads
import UI_Update
import General
import Functions


# call thread for motion control
def motion(self):
    self.motion_Thread = Threads.Motion()
    self.motion_Thread.stop_motor.connect(lambda: Functions.disable_motor())
    self.motion_Thread.sensor_read.connect(lambda: UI_Update.TOF_update(self))
    self.motion_Thread.started.connect(
        lambda: UI_Update.motion_frames_toggle(self)
    )


    self.motion_Thread.finished.connect(
        lambda: UI_Update.motion_frames_toggle(self)
    )

    self.motion_Thread.start()
    General.motion_thread_running = True
