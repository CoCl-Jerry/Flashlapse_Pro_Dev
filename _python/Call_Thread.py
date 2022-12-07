import Threads
import UI_Update
import General
import Functions
import Imaging


# call thread for motion control
def motion(self):
    self.Motion_Thread = Threads.Motion()
    self.Motion_Thread.stop_motor.connect(lambda: Functions.disable_motor())
    self.Motion_Thread.sensor_read.connect(lambda: UI_Update.TOF_update(self))
    self.Motion_Thread.started.connect(lambda: UI_Update.motion_frames_toggle(self))

    self.Motion_Thread.finished.connect(lambda: UI_Update.motion_frames_toggle(self))

    self.Motion_Thread.start()
    General.motion_thread_running = True


def snapshot(self):

    Imaging.imaging_settings_update(self)
    self.Snap_Thread = Threads.Snap()
    self.Snap_Thread.started.connect(lambda: UI_Update.imaging_frame_toggle(self))
    self.Snap_Thread.finished.connect(lambda: UI_Update.imaging_frame_toggle(self))
    self.Snap_Thread.finished.connect(
        lambda: UI_Update.update_frame_snapshot(self, "../_temp/snapshot.jpg")
    )
    self.Snap_Thread.start()
