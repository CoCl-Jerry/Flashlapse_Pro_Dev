import Threads
import UI_Update
import General
import Motion
import Imaging

import os


# call thread for motion control
def motion(self):
    self.Motion_Thread = Threads.Motion()
    self.Motion_Thread.stop_motor.connect(lambda: Motion.disable_motor())
    self.Motion_Thread.sensor_read.connect(lambda: UI_Update.TOF_update(self))
    self.Motion_Thread.started.connect(lambda: UI_Update.motion_frames_toggle(self))

    self.Motion_Thread.finished.connect(lambda: UI_Update.motion_frames_toggle(self))
    General.motion_thread_running = True
    self.Motion_Thread.start()


def snapshot(self):

    Imaging.imaging_settings_update(self)
    self.Snap_Thread = Threads.Snap()
    self.Snap_Thread.started.connect(lambda: UI_Update.imaging_frame_toggle(self))
    self.Snap_Thread.finished.connect(lambda: UI_Update.imaging_frame_toggle(self))
    self.Snap_Thread.finished.connect(
        lambda: UI_Update.update_preview_frame(self, "../_temp/snapshot.jpg")
    )
    self.Snap_Thread.finished.connect(lambda: UI_Update.error_UI_update(self))

    self.Snap_Thread.start()


def preview(self):

    Imaging.imaging_settings_update(self)
    self.Preview_Thread = Threads.Preview()
    self.Preview_Thread.started.connect(lambda: UI_Update.imaging_frame_toggle(self))
    self.Preview_Thread.finished.connect(lambda: UI_Update.imaging_frame_toggle(self))
    if General.image_format:
        self.Preview_Thread.finished.connect(
            lambda: UI_Update.update_preview_frame(self, "../_temp/preview.jpg")
        )
        self.Preview_Thread.finished.connect(
            lambda: os.system("gpicview ../_temp/preview.jpg")
        )
    else:
        self.Preview_Thread.finished.connect(
            lambda: UI_Update.update_preview_frame(self, "../_temp/preview.png")
        )
        self.Preview_Thread.finished.connect(
            lambda: os.system("gpicview ../_temp/preview.png")
        )
    self.Preview_Thread.finished.connect(lambda: UI_Update.error_UI_update(self))

    self.Preview_Thread.start()


def livefeed(self):
    Imaging.imaging_settings_update(self)
    self.Livefeed_Thread = Threads.Livefeed()
    self.Livefeed_Thread.started.connect(lambda: UI_Update.imaging_frame_toggle(self))
    self.Livefeed_Thread.finished.connect(lambda: UI_Update.imaging_frame_toggle(self))
    self.Livefeed_Thread.start()


def timelapse(self):

    if not General.timelapse_thread_running:
        Imaging.imaging_settings_update(self)
        self.Timelapse_Thread = Threads.Timelapse()
        self.Timelapse_Thread.started.connect(
            lambda: UI_Update.timelapse_UI_update(self)
        )
        self.Timelapse_Thread.finished.connect(
            lambda: UI_Update.timelapse_UI_update(self)
        )
        self.Timelapse_Thread.imaging.connect(
            lambda: UI_Update.imaging_frame_toggle(self)
        )
        self.Timelapse_Thread.complete.connect(
            lambda: UI_Update.imaging_frame_toggle(self)
        )
        self.Timelapse_Thread.complete.connect(
            lambda: UI_Update.update_preview_frame(self)
        )
        self.Timelapse_Thread.countdown.connect(
            lambda: UI_Update.timelapse_countdown(self)
        )
        General.timelapse_thread_running = True
        self.Timelapse_Thread.start()
    else:
        General.timelapse_thread_running = False
        UI_Update.timelapse_UI_update(self)
